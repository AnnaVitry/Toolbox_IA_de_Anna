import os

import streamlit as st
from dotenv import load_dotenv

# Charge les variables du fichier .env
load_dotenv()

# Récupère l'URL ou utilise une valeur par défaut
API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("Toolbox IA")
# Utilise ensuite la variable API_URL dans tes requêtes
# response = requests.get(f"{API_URL}/compute/add?a={a}&b={b}")
