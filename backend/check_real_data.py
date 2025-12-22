import os
import sys
import django
from neomodel import config, db

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from scouting.models import Club, Player

print(f"--- Database Check: {config.DATABASE_URL} ---")
print(f"Total Players: {len(Player.nodes.all())}")
print(f"Total Clubs: {len(Club.nodes.all())}")

print("\n--- Sample Players ---")
for p in Player.nodes.all()[:5]:
    print(f"- {p.name} ({p.position})")

print("\n--- Clubs List ---")
for c in Club.nodes.all():
    print(f"- {c.name} (Email: {c.email})")
