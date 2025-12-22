import os
import sys
import django
from datetime import date, timedelta

# Setup Django environment to use models
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from scouting.models import Club, Player, Quality, Style, Weakness
from neomodel import db

def clear_db():
    pass # Do not clear everything, we want to keep Clubs and User links

def create_data():
    print("Creating data...")

    # 1. Create Clubs
    clubs_data = [
        {"name": "Raja CA", "city": "Casablanca", "founded": 1949},
        {"name": "Wydad AC", "city": "Casablanca", "founded": 1937},
        {"name": "AS FAR", "city": "Rabat", "founded": 1958},
        {"name": "RS Berkane", "city": "Berkane", "founded": 1938},
        {"name": "FUS Rabat", "city": "Rabat", "founded": 1946},
    ]
    
    clubs = {}
    for c in clubs_data:
        club = Club(**c).save()
        clubs[c["name"]] = club
        print(f"Created Club: {club.name}")

    # 2. Create Qualities
    qualities_data = [
        "Vitesse", "Dribble", "Finition", "Passe courte", "Passe longue",
        "Tacle", "Marquage", "Jeu de tête", "Vision", "Endurance"
    ]
    
    qualities = {}
    for q in qualities_data:
        quality = Quality(label=q, category="Technique").save()
        qualities[q] = quality

    # 3. Create Styles
    styles_data = ["Offensif", "Défensif", "Contre-attaque", "Possession"]
    styles = {}
    for s in styles_data:
        style = Style(type=s).save()
        styles[s] = style

    # 4. Create Players
    players_data = [
        {
            "name": "Yousri Bouzok",
            "age": 27,
            "position": "Ailier",
            "nationality": "Algérie",
            "contract_end": date.today() + timedelta(days=60), # Expiring soon
            "club": "Raja CA",
            "qualities": ["Vitesse", "Dribble", "Finition", "Vision"],
            "style": "Offensif"
        },
        {
            "name": "Yahya Jabrane",
            "age": 32,
            "position": "Milieu Défensif",
            "nationality": "Maroc",
            "contract_end": date.today() + timedelta(days=400),
            "club": "Wydad AC",
            "qualities": ["Passe courte", "Tacle", "Vision", "Endurance"],
            "style": "Possession"
        },
        {
            "name": "Rabie Hrimat",
            "age": 29,
            "position": "Milieu Défensif",
            "nationality": "Maroc",
            "contract_end": date.today() + timedelta(days=120),
            "club": "AS FAR",
            "qualities": ["Passe courte", "Tacle", "Marquage", "Endurance"],
            "style": "Possession"
        },
        {
            "name": "Issoufou Dayo",
            "age": 32,
            "position": "Défenseur Central",
            "nationality": "Burkina Faso",
            "contract_end": date.today() + timedelta(days=30), # Expiring soon
            "club": "RS Berkane",
            "qualities": ["Jeu de tête", "Marquage", "Tacle", "Passe longue"],
            "style": "Défensif"
        },
        {
            "name": "Adam Ennafati",
            "age": 29,
            "position": "Ailier",
            "nationality": "Maroc",
            "contract_end": date.today() + timedelta(days=500),
            "club": "Raja CA",
            "qualities": ["Vitesse", "Dribble", "Passe courte"],
            "style": "Offensif"
        },
         {
            "name": "Hamza Igamane",
            "age": 25,
            "position": "Attaquant",
            "nationality": "Maroc",
            "contract_end": date.today() + timedelta(days=600),
            "club": "AS FAR",
            "qualities": ["Finition", "Vitesse", "Jeu de tête"],
            "style": "Contre-attaque"
        }
    ]

    for p in players_data:
        player = Player(
            name=p["name"],
            age=p["age"],
            position=p["position"],
            nationality=p["nationality"],
            contract_end=p["contract_end"]
        ).save()
        
        # Connect Club
        if p["club"] in clubs:
            player.plays_for.connect(clubs[p["club"]])
            
        # Connect Qualities
        for q in p["qualities"]:
            if q in qualities:
                player.qualities.connect(qualities[q])
                
        # Connect Style
        if p["style"] in styles:
            player.style.connect(styles[p["style"]])
            
        print(f"Created Player: {player.name} ({p['club']})")

if __name__ == '__main__':
    try:
        clear_db()
        create_data()
        print("Database successfully seeded!")
    except Exception as e:
        print(f"Error seeding database: {e}")
