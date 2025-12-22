from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Player, Club, Quality, Style
from .serializers import PlayerSerializer
from neomodel import db
from datetime import datetime

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = None
        
        # 1. Try to find user by email to get the correct username
        try:
            user_obj = User.objects.get(email=email)
            # 2. Authenticate using the found username
            user = authenticate(username=user_obj.username, password=password)
        except User.DoesNotExist:
            pass
        
        # 3. Demo Auto-Registration/Fallback for admin
        if not user:
            if email == 'admin@botola.com' and password == 'admin':
                user, created = User.objects.get_or_create(username='admin', email='admin@botola.com')
                if created:
                    user.set_password('admin')
                    user.save()
                # Re-authenticate to ensure we have the backend attribute set on user object
                user = authenticate(username='admin', password='admin')
            else:
                return Response({'error': 'Identifiants invalides'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        
        # Get Club linked to User email
        club_name = 'Unknown Club'
        club_uid = ''
        
        # Find club by email
        club = Club.nodes.get_or_none(email=user.email)
        if club:
            club_name = club.name
            club_uid = club.uid
        elif user.username == 'admin':
            club_name = 'Admin Demo'
            
        return Response({
            'token': str(refresh.access_token),
            'refresh': str(refresh),
            'club_id': club_uid, 
            'club_name': club_name
        })

class PlayerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # Filter players by logged-in user's club
        user = request.user
        print(f"DEBUG: User {user.username} (Email: {user.email}) requesting players.")
        
        club = Club.nodes.get_or_none(email=user.email)
        
        if club:
             print(f"DEBUG: Found club {club.name} for email {user.email}")
             query = """
             MATCH (p:Player)-[:PLAYS_FOR]->(c:Club)
             WHERE c.email = $email
             RETURN p
             """
             results, meta = db.cypher_query(query, {'email': user.email})
             print(f"DEBUG: Cypher query returned {len(results)} rows.")
             
             players = []
             for row in results:
                 try:
                     players.append(Player.inflate(row[0]))
                 except Exception as e:
                     print(f"ERROR inflating player: {e}")
        else:
            # If admin or no club linked, show all (or handle as needed)
            if user.username == 'admin':
                players = Player.nodes.all()
            else:
                print(f"DEBUG: No club found for {user.email}")
                players = []

        print(f"DEBUG: Serializing {len(players)} players.")
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        try:
            # Parse date
            contract_end = datetime.strptime(data.get('contract_end'), '%Y-%m-%d').date()
            
            player = Player(
                name=data.get('name'),
                age=data.get('age'),
                position=data.get('position'),
                nationality=data.get('nationality'),
                contract_end=contract_end
            ).save()
            
            # Handle relationships
            if 'qualities' in data:
                for q_label in data['qualities']:
                    quality = Quality.nodes.get_or_none(label=q_label)
                    if not quality:
                        quality = Quality(label=q_label).save()
                    player.qualities.connect(quality)
            
            if 'style' in data:
                style = Style.nodes.get_or_none(type=data['style'])
                if not style:
                    style = Style(type=data['style']).save()
                player.style.connect(style)

            return Response(PlayerSerializer(player).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        player = Player.nodes.get_or_none(uid=pk)
        if player:
            return Response(PlayerSerializer(player).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        player = Player.nodes.get_or_none(uid=pk)
        if player:
            player.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class RecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, player_id):
        target = Player.nodes.get_or_none(uid=player_id)
        if not target:
            return Response({'error': 'Joueur non trouvé'}, status=status.HTTP_404_NOT_FOUND)

        # Recommendation Logic: Same Position + Shared Qualities
        # Using parameters for safety
        query = """
        MATCH (target:Player {uid: $player_id})-[:HAS_QUALITY]->(q:Quality)
        MATCH (candidate:Player)-[:HAS_QUALITY]->(q)
        WHERE target <> candidate AND target.position = candidate.position
        RETURN candidate, count(q) as shared_qualities
        ORDER BY shared_qualities DESC
        LIMIT 10
        """
        params = {'player_id': player_id}
        results, meta = db.cypher_query(query, params)
        
        recommendations = []
        for row in results:
            candidate = Player.inflate(row[0])
            score = row[1] 
            
            recommendations.append({
                'player_id': candidate.uid,
                'name': candidate.name,
                'position': candidate.position,
                'similarity_score': score, 
                'qualities': [q.label for q in candidate.qualities.all()],
                'style': candidate.style.all()[0].type if candidate.style.all() else 'Inconnu'
            })
            
        return Response({'recommendations': recommendations})
