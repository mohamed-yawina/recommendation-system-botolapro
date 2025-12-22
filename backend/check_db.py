import os
import sys
import django
from neomodel import config, db

# Setup Django
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

print(f"URL: {config.DATABASE_URL}")
try:
    db.set_connection(config.DATABASE_URL)
    results, meta = db.cypher_query("RETURN 1")
    print("Connection successful!")
    
    try:
        results, meta = db.cypher_query("SHOW DATABASES")
        # print("Databases:", results)
        # Check if botolatest is in the list
        found = False
        for row in results:
            # row format depends on neomodel version return
            # usually list of lists
            # name is usually first column
            if 'botolatest' in str(row):
                found = True
                print(f"Database 'botolatest' found in server list: {row}")
        if not found:
            print("Database 'botolatest' NOT found in server list.")
    except Exception as e:
        print(f"Could not list databases: {e}")

except Exception as e:
    print(f"Connection failed: {e}")
