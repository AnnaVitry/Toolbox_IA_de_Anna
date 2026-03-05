import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# On récupère l'URL de la base depuis le .env
# En local, on peut tester avec sqlite:///./test.db si Postgres n'est pas prêt
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Générateur de session de base de données."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
