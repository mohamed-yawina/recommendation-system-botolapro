# Scouting Assistant - Botola Pro

Application d'aide à la décision pour les clubs de la Botola Pro, basée sur Neo4j, Django et React.

## Prérequis

- **Python 3.10+**
- **Node.js 18+**
- **Neo4j Server** (Local ou Remote)

## Configuration

### 1. Base de données Neo4j

Assurez-vous que Neo4j est démarré et accessible.
Par défaut, l'application cherche :
- URL: `bolt://localhost:7687`
- User: `neo4j`
- Password: `password`

Vous pouvez modifier ces paramètres dans `backend/config/settings.py`.

### 2. Backend (Django)

Le backend est configuré dans le dossier `backend`.

```bash
cd backend
# Activer l'environnement virtuel
.\venv\Scripts\activate

# Installer les dépendances (déjà fait)
pip install -r requirements.txt

# Configurer la base de données Neo4j (Constraints)
# Assurez-vous que Neo4j est lancé avant de lancer cette commande
python manage.py install_labels

# Lancer le serveur
python manage.py runserver
```

L'API sera accessible sur `http://localhost:8000/api`.

### 3. Frontend (React)

Le frontend est dans le dossier `frontend`.

```bash
cd frontend

# Installer les dépendances (déjà fait)
npm install

# Lancer le serveur de développement
npm run dev
```

L'application sera accessible sur `http://localhost:5173`.

## Fonctionnalités

- **Authentification** : Connexion Club.
- **Dashboard** : Vue d'ensemble et alertes contrats.
- **Joueurs** : Gestion de l'effectif (CRUD).
- **Recommandations** : Moteur de similarité (Neo4j).

## Compte de Démo

- Email: `admin@botola.com`
- Password: `admin`
