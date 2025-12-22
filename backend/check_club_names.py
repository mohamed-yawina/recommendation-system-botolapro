import os
import sys
import django
from neomodel import config, db

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

print("Checking Clubs connected to players...")

query = """
MATCH (p:Player)-[:PLAYS_FOR]->(c:Club)
RETURN DISTINCT c.name, c.email
LIMIT 20
"""
results, _ = db.cypher_query(query)
for row in results:
    print(f"Club: '{row[0]}' - Email: '{row[1]}'")
