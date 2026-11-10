<div align="center">

# Botola Pro — Football Scouting Assistant

**Football Scouting · Graph-Based Recommendations · Django REST Framework · React · Neo4j**

A full-stack decision-support application for football clubs, combining **player management**, **contract visibility**, and **graph-based similarity recommendations** in the context of Morocco's Botola Pro.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![React](https://img.shields.io/badge/React-18-149ECA?logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?logo=neo4j&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?logo=tailwindcss&logoColor=white)

[Features](#features) · [Architecture](#architecture) · [Local setup](#local-development) · [Security](#security-and-known-limitations)

</div>

## Overview

Botola Pro Scouting Assistant explores how **graph databases** can support player discovery and recruitment decisions. The repository combines a Django REST API with a React / TypeScript frontend and a Neo4j graph data layer.

> **Status:** Academic / portfolio project. This README describes repository structure and documented capabilities; end-to-end behavior and recommendation quality have not been independently tested in this update.

## Features

- **Club authentication:** Login workflows backed by Django REST Framework and JWT configuration.
- **Dashboard:** Overview and contract-related alerts described by the original project documentation.
- **Squad management:** Player listing and CRUD workflows.
- **Recommendations:** Player-similarity and scouting features using Neo4j graph relationships.
- **Web application:** React interface with TypeScript, Tailwind CSS, and Vite.

## Architecture

```text
             React 18 + TypeScript + Vite
                     Frontend UI
                          |
                     HTTP / JSON
                          |
                          v
               Django REST Framework
                 JWT authentication
                 /api/ endpoints
                          |
                          v
                    Neo4j Graph
             Players / clubs / relations
```

| Layer | Technologies |
| :--- | :--- |
| Frontend | React 18, TypeScript, Vite 6, Tailwind CSS, React Router |
| State & networking | Zustand, Axios |
| Backend | Python, Django 6, Django REST Framework |
| Authentication | Simple JWT (configured in Django settings) |
| Graph database | Neo4j, django-neomodel / neomodel |
| Visualization | neovis.js dependency in frontend |

## Repository structure

```text
recommendation-system-botolapro/
├── backend/
│   ├── config/           # Django settings and URL configuration
│   ├── scouting/         # Models, serializers, views, API routes
│   ├── manage.py
│   └── seed_data.py      # Data preparation utility
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
├── infos/
├── .gitignore
└── README.md
```

## Local development

### Prerequisites

- Python version compatible with the repository's Django 6 installation
- Node.js and npm (the original README specifies Node.js 18+; check compatibility with the installed Vite version)
- Running Neo4j server and a database prepared for the project's graph models

### 1. Clone

```bash
git clone https://github.com/mohamed-yawina/recommendation-system-botolapro.git
cd recommendation-system-botolapro
```

### 2. Configure Neo4j and backend

The Django settings are in `backend/config/settings.py`. Review the database URI, database selection, credentials, and development settings before starting.

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment (Windows PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS / Linux:

```bash
source .venv/bin/activate
```

**Dependency note:** The previous README instructed `pip install -r requirements.txt`, but `backend/requirements.txt` was **not found** during this audit. Before installing, create a reviewed dependency manifest from the actual backend environment. Do not assume the project can be installed reproducibly until that file is supplied.

After dependencies and Neo4j are configured, the existing project instructions use:

```bash
python manage.py install_labels
python manage.py runserver
```

The API routes are mounted under **http://localhost:8000/api/** in `backend/config/urls.py`. Verify that any custom management commands are available in your checkout.

### 3. Start the frontend

In another terminal, from the repository root:

```bash
cd frontend
npm ci
npm run dev
```

The original README identifies **http://localhost:5173/** as the development frontend address. The actual port may vary if it is occupied.

### 4. Frontend quality checks

```bash
cd frontend
npm run check
npm run lint
npm run build
```

These commands are defined in `frontend/package.json`; **they have not been executed as part of this documentation update**.

## Security and known limitations

**Security review recommended before deployment or sharing test credentials:**

1. **Django secret:** `backend/config/settings.py` contains a hard-coded Django secret key. Replace it with an environment-provided secret and rotate the exposed value before any real deployment.
2. **Neo4j connection:** The same settings file contains database connection details/credentials. Remove secrets from source control and rotate any real credentials that may have been exposed.
3. **Development configuration:** `DEBUG = True` is enabled and `ALLOWED_HOSTS` is empty. Configure these appropriately for deployment.
4. **Demo login:** The previous README included a plaintext demonstration username/password. Those credentials are intentionally not repeated here. Use freshly configured local test accounts instead.
5. **Dependencies:** A backend requirements manifest is missing from the inspected repository.
6. **Testing:** The repository contains a `backend/scouting/tests.py` module, but passing test results have not been verified.
7. **Data quality:** Graph recommendation outputs depend on the completeness and reliability of the player and club data. Do not treat similarity scores as validated scouting judgments.

The project should be treated as an **educational demonstration**, not a production-ready scouting platform.

## Suggested improvements

- [ ] Externalize and rotate Django / Neo4j secrets
- [ ] Add a reviewed backend `requirements.txt` or lockfile
- [ ] Provide a reproducible Neo4j setup and sample data guide
- [ ] Add backend API tests and frontend verification
- [ ] Document recommendation logic, input features, and evaluation limitations
- [ ] Include genuine application screenshots and a short demo
- [ ] Add GitHub Actions for repeatable checks

## Author

**Mohamed Yawina** · Software Engineering Student, EMSI

[GitHub](https://github.com/mohamed-yawina) · [LinkedIn](https://www.linkedin.com/in/mohamed-yawina/)

---

<div align="center"><sub>Exploring graph databases and data-driven football scouting through full-stack software engineering.</sub></div>
