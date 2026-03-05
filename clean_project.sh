#!/bin/bash

echo "--- 🧹 Nettoyage de l'architecture Toolbox IA ---"

# 1. Arrêt des conteneurs et suppression des réseaux/volumes
echo "Stopping Docker containers and removing volumes..."
docker compose down -v

# 2. Nettoyage des fichiers de cache Python (Hygiène)
echo "Cleaning Python caches..."
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.py[co]" -delete

# 3. Suppression de la base de données SQLite locale (Phase B relic)
if [ -f "app_api/test.db" ]; then
    echo "Removing local SQLite database..."
    rm app_api/test.db
fi

# 4. Nettoyage des environnements virtuels locaux (Optionnel)
# Décommente la ligne suivante si tu veux aussi supprimer les .venv
# find . -type d -name ".venv" -exec rm -rf {} +

# 5. Nettoyage du cache de build Docker
echo "Pruning Docker builder cache..."
docker builder prune -f

echo "--- ✨ Projet nettoyé et prêt pour un nouveau build ! ---"