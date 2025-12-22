import os
import sys
import django
from neomodel import config, db

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from scouting.models import Club, Player

print("Checking relationships...")

# Check if ANY player plays for ANY club
query = "MATCH (p:Player)-[r:PLAYS_FOR]->(c:Club) RETURN count(r)"
results, _ = db.cypher_query(query)
print(f"Total PLAYS_FOR relationships: {results[0][0]}")

# Check for Raja specifically
raja_email = "raja@botola.ma"
query_raja = f"MATCH (p:Player)-[:PLAYS_FOR]->(c:Club {{email: '{raja_email}'}}) RETURN count(p)"
results_raja, _ = db.cypher_query(query_raja)
print(f"Players playing for Raja ({raja_email}): {results_raja[0][0]}")

# If 0, check what relationship name is actually used or if there are any relationships
print("\nChecking for ANY relationship between Player and Club:")
query_any = "MATCH (p:Player)-[r]->(c:Club) RETURN type(r), count(r) LIMIT 5"
results_any, _ = db.cypher_query(query_any)
for row in results_any:
    print(f"Rel Type: {row[0]}, Count: {row[1]}")
