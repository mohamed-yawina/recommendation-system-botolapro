import os
import sys
import django
from neomodel import config, db

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

print("Checking ALL Clubs in DB...")

query = "MATCH (c:Club) RETURN c.name, c.email, count{(c)<-[:PLAYS_FOR]-(:Player)} as player_count"
results, _ = db.cypher_query(query)
for row in results:
    print(f"Name: '{row[0]}' | Email: '{row[1]}' | Players Linked: {row[2]}")
