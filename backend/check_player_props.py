import os
import sys
import django
from neomodel import config, db

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from scouting.models import Player

print("Checking Player properties...")
query = "MATCH (p:Player) RETURN p.name, p.contract_end LIMIT 5"
results, _ = db.cypher_query(query)
for row in results:
    print(f"Name: {row[0]}, Contract End: {row[1]} (Type: {type(row[1])})")
