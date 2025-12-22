import os
import sys
import django
from neomodel import config, db

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from scouting.models import Club, Player

print(f"Connected to: {config.DATABASE_URL}")
print(f"Clubs count: {len(Club.nodes.all())}")
print(f"Players count: {len(Player.nodes.all())}")

clubs = Club.nodes.all()
for c in clubs:
    print(f"- {c.name} (Email: {c.email})")
