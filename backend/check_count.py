from neomodel import db, config
import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from scouting.models import Player

print(f"Player count: {len(Player.nodes.all())}")
