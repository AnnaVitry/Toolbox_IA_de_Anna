from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

# Toujours repartir de la racine du package app_api
from app_api.maths.mon_module import add
from app_api.models.database import Base, Calcul
from app_api.modules.connect import engine, get_db

# Création des tables (pour le test local en SQLite)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/compute/add")
def compute_add(a: float, b: float, db: Session = Depends(get_db)):
    """Fait  le calcule l'addition de deux nombres et enregistre le résultat."""
    res = add(a, b)
    # On enregistre en base de données
    nouveau_calcul = Calcul(a=a, b=b, resultat=res)
    db.add(nouveau_calcul)
    db.commit()

    return {"result": res, "saved": True}


@app.get("/data")
def get_history(db: Session = Depends(get_db)):
    """Récupère l'historique des calculs."""
    return db.query(Calcul).all()
