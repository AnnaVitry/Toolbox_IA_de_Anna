# Toolbox IA - Architecture Microservices de Anna

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg?style=for-the-badge)

Ce projet est une plateforme de services IA **multi-tiers** conteneurisée. Elle orchestre une interface utilisateur, une API de calcul et une base de données persistante PostgreSQL.

---

## ʕ•ᴥ•ʔっ · · · ✴ Architecture du Projet

L'écosystème est découpé en trois services autonomes communiquant via des réseaux isolés :

* **Frontend (Streamlit)** : Interface de saisie et visualisation.
* **Backend (FastAPI)** : Logique métier et orchestration des données.
* **Database (PostgreSQL)** : Stockage persistant via volumes Docker.



---

## ʕ•ᴥ•ʔっ · · · ✴ Installation & Orchestration

Assurez-vous d'avoir [Docker](https://www.docker.com/) installé.

```bash
git clone [https://github.com/AnnaVitry/Toolbox_IA_Microservice.git](https://github.com/AnnaVitry/Toolbox_IA_Microservice.git)
cd Toolbox_IA_Microservice
# Lancement de tous les services d'un coup
docker compose up --build