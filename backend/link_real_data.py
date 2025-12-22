import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from neomodel import db
from django.contrib.auth.models import User
from scouting.models import Club

# Mapping: Real Neo4j Name -> Desired Email/User
# Based on the list I just saw in the terminal
club_mapping = {
    "Raja Club Athletic": "raja@botola.ma",
    "Wydad Casablanca": "wydad@botola.ma",
    "AS FAR Rabat": "asfar@botola.ma",
    "RS Berkane": "rsb@botola.ma",
    "Fath Union Sport": "fus@botola.ma",
    "MAS de Fès": "mas@botola.ma",
    "Union Touarga Sport": "uts@botola.ma",
    "Olympic Safi": "ocs@botola.ma",
    "Hassania d'Agadir": "husa@botola.ma",
    "Ittihad Tanger": "irt@botola.ma",
    "Renaissance Zemamra": "rca_z@botola.ma",
    "Difaâ Hassani El-Jadidi": "dhj@botola.ma",
    "CODM Meknès": "codm@botola.ma",
    "Kawkab Athletic Club Marrakech": "kacm@botola.ma",
    "Union Sportive Yacoub El Mansour": "usym@botola.ma",
    "Olympique Dcheira": "od@botola.ma"
}

print("Linking Real Neo4j Data to Django Users...")

for real_name, email in club_mapping.items():
    # 1. Find Club in Neo4j
    club = Club.nodes.get_or_none(name=real_name)
    if club:
        club.email = email
        club.save()
        print(f"[OK] Linked '{real_name}' to {email}")
        
        # 2. Create Django User
        username = email.split('@')[0]
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password("123456")
            user.save()
            print(f"   -> Created user: {username}")
        else:
            # Ensure password is correct
            user.set_password("123456")
            user.save()
            
    else:
        print(f"[WARN] Club '{real_name}' not found in Neo4j database!")

print("\nMigration complete.")
