from sqlalchemy import Column, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Calcul(Base):
    """Modèle représentant un calcul effectué dans la Toolbox."""

    __tablename__ = "calculs"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    resultat = Column(Float, nullable=False)
