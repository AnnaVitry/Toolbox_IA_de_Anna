# Toolbox IA - Frontend (Streamlit)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)

Ce service est l'interface utilisateur (UI) de la Toolbox IA. Il permet d'interagir avec l'API de calcul et de visualiser l'historique des données stockées dans PostgreSQL.

---

## ʕ•ᴥ•ʔっ · · · ✴ Fonctionnalités

* **Interface de Saisie** : Formulaires interactifs pour envoyer des calculs à l'API.
* **Visualisation** : Affichage dynamique des résultats sous forme de tableaux.
* **Communication REST** : Consommation des endpoints de `app_api`.

---

## Architecture Locale

```text
app_front/
├── main.py            # Point d'entrée de l'application Streamlit
├── Dockerfile         # Configuration pour la conteneurisation
├── pyproject.toml     # Dépendances (Streamlit, Requests, etc.)
└── uv.lock            # Verrouillage des versions
```