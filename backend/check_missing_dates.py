import os
import sys
import django
from neomodel import config, db

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

print("Checking for players with missing contract_end...")
query = "MATCH (p:Player) WHERE p.contract_end IS NULL RETURN count(p)"
results, _ = db.cypher_query(query)
print(f"Players with missing contract_end: {results[0][0]}")
