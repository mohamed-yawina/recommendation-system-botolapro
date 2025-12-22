from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Player, Club, Quality, Style, Weakness

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ClubSerializer(serializers.Serializer):
    uid = serializers.CharField(read_only=True)
    name = serializers.CharField()
    city = serializers.CharField()
    league = serializers.CharField()
    founded = serializers.IntegerField()

class QualitySerializer(serializers.Serializer):
    label = serializers.CharField()
    category = serializers.CharField(required=False)

class StyleSerializer(serializers.Serializer):
    type = serializers.CharField()

class PlayerSerializer(serializers.Serializer):
    uid = serializers.CharField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField(required=False, allow_null=True)
    position = serializers.CharField(required=False, allow_null=True)
    nationality = serializers.CharField(required=False, allow_null=True)
    contract_end = serializers.DateField(required=False, allow_null=True)
    
    # Nested fields for read
    qualities = serializers.SerializerMethodField()
    style = serializers.SerializerMethodField()
    club = serializers.SerializerMethodField()

    def get_qualities(self, obj):
        return [q.label for q in obj.qualities.all()]

    def get_style(self, obj):
        styles = obj.style.all()
        return styles[0].type if styles else None

    def get_club(self, obj):
        clubs = obj.plays_for.all()
        return clubs[0].name if clubs else None

    def create(self, validated_data):
        # creation logic handled in view due to relationships
        return Player(**validated_data).save()
