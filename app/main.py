"""Script principal de l'application.

Charge les données depuis un fichier CSV et exécute une série de
démonstrations mathématiques via le module métier.
"""

import pandas as pd

from app.modules.mon_module import add, print_data, square, sub


def main():
    """Fonction principale orchestrant la démonstration."""
    print("--- Démarrage de l'application ---")

    # 1. Démonstration mathématique
    val_a, val_b = 10, 5
    print(f"Addition ({val_a} + {val_b}) : {add(val_a, val_b)}")
    print(f"Soustraction ({val_a} - {val_b}) : {sub(val_a, val_b)}")
    print(f"Carré de {val_a} : {square(val_a)}")

    # 2. Manipulation de données
    try:
        # Lecture du CSV (assurez-vous que moncsv.csv existe dans app/)
        df = pd.read_csv("app/moncsv.csv")
        print("\n--- Analyse du fichier CSV ---")
        nb_lignes = print_data(df)
        print(f"Total de lignes analysées : {nb_lignes}")
    except FileNotFoundError:
        print("\n[ERREUR] Le fichier 'app/moncsv.csv' est introuvable.")


if __name__ == "__main__":
    main()
