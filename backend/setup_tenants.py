import os
import sys
import django

# Setup Django first
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Then import models and other dependencies
from neomodel import config, db
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from scouting.models import Club

# Full list of Botola Pro clubs (16 teams)
clubs_data = [
    {"name": "Raja CA", "email": "raja@botola.ma", "password": "123456"},
    {"name": "Wydad AC", "email": "wydad@botola.ma", "password": "123456"},
    {"name": "AS FAR", "email": "asfar@botola.ma", "password": "123456"},
    {"name": "RS Berkane", "email": "rsb@botola.ma", "password": "123456"},
    {"name": "FUS Rabat", "email": "fus@botola.ma", "password": "123456"},
    {"name": "Maghreb Fez", "email": "mas@botola.ma", "password": "123456"},
    {"name": "Union Touarga", "email": "uts@botola.ma", "password": "123456"},
    {"name": "Olympic Safi", "email": "ocs@botola.ma", "password": "123456"},
    {"name": "Hassania Agadir", "email": "husa@botola.ma", "password": "123456"},
    {"name": "Moghreb Tetouan", "email": "mat@botola.ma", "password": "123456"},
    {"name": "Renaissance Zemamra", "email": "rca_z@botola.ma", "password": "123456"},
    {"name": "JS Soualem", "email": "jss@botola.ma", "password": "123456"},
    {"name": "Chabab Mohammedia", "email": "sccm@botola.ma", "password": "123456"},
    {"name": "Ittihad Tanger", "email": "irt@botola.ma", "password": "123456"},
    {"name": "Youssoufia Berrechid", "email": "cayb@botola.ma", "password": "123456"}, # Note: Check current season composition if relegation happened
    {"name": "Mouloudia Oujda", "email": "mco@botola.ma", "password": "123456"},
    # Alternatives if teams changed (e.g. COD Meknes, DHJ) - Keeping standard list for now
    # {"name": "COD Meknes", "email": "codm@botola.ma", "password": "123456"},
    # {"name": "DHJ El Jadida", "email": "dhj@botola.ma", "password": "123456"},
]

print("Updating Clubs and Creating Users for all 16 teams...")

for data in clubs_data:
    # 1. Ensure Club exists in Neo4j (Create if missing for robustness)
    club = Club.nodes.get_or_none(name=data["name"])
    if not club:
        print(f"Creating missing club in Neo4j: {data['name']}")
        club = Club(name=data["name"], city="Unknown", league="Botola Pro").save()
    
    # 2. Update Email
    club.email = data["email"]
    club.save()
    print(f"Synced Club: {club.name} ({club.email})")

    # 3. Create/Update Django User
    username = data["email"].split('@')[0]
    try:
        user, created = User.objects.get_or_create(username=username, email=data["email"])
        if created:
            user.set_password(data["password"])
            user.save()
            print(f"Created Django User: {username}")
        else:
            # print(f"User {username} already exists")
            pass
    except IntegrityError:
        print(f"Error handling user {username}")

print("All 16 clubs configured!")
