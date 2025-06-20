# Projet Django - Sondages (Polls)

Ce projet est une application web de sondages réalisée avec Django.  
Les utilisateurs peuvent consulter des sondages, voter, créer leurs propres sondages (si authentifiés), et gérer leurs sondages.

---

## Fonctionnalités

- Liste des sondages disponibles avec images associées  
- Page détail pour voter sur un sondage  
- Création, suppression et gestion des sondages (pour utilisateurs authentifiés)  
- Page de contact, inscription, connexion et déconnexion  
- Affichage des résultats de sondages  

---

## Installation

1. Cloner ce dépôt :

    ```bash
    git clone https://github.com/SlurpyMK3/django_polls.git
    cd djanotutorial
    ```

2. Créer un environnement virtuel et l’activer :

    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows
    ```

3. Installer les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

4. Appliquer les migrations :

    ```bash
    python manage.py migrate
    ```

5. Lancer le serveur de développement :

    ```bash
    python manage.py runserver
    ```

6. Accéder à l’application sur `http://127.0.0.1:8000/`

---

## Structure du projet

- `polls/` : application principale avec les vues, modèles, templates  
- `templates/` : templates HTML  
- `static/` : fichiers CSS, images, scripts JS  
- `media/` : fichiers uploadés (images sondages)  
- `manage.py` : utilitaire Django  
