"""Suite de tests pour le module métier.

Ce module valide les calculs mathématiques et la lecture de structures
de données Pandas en utilisant les fonctions de mon_module.py.
"""

import pandas as pd
import pytest

from app.modules.mon_module import add, print_data, square, sub

# --- Section Mathématiques ---


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 12),
        (20, 2, 22),
        (0, 2, 2),
    ],
)
def test_add(a, b, expected):
    """Teste la fonction d'addition avec plusieurs scénarios."""
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 5, 5),
        (5, 10, -5),
    ],
)
def test_sub(a, b, expected):
    """Teste la fonction de soustraction."""
    assert sub(a, b) == expected


def test_square():
    """Teste la fonction de mise au carré."""
    assert square(4) == 16


# --- Section Data / CSV ---


@pytest.fixture
def mock_csv_data():
    """Fixture simulant le contenu de moncsv.csv.

    Permet de tester print_data sans dépendre du fichier physique.
    """
    return pd.DataFrame({"id": [1, 2], "nom": ["Alice", "Bob"], "valeur": [100, 200]})


def test_print_data_with_fixture(mock_csv_data, capsys):
    """Vérifie que print_data traite correctement un DataFrame simulé."""
    result = print_data(mock_csv_data)

    # Vérification du retour (nombre de lignes)
    assert result == 2

    # Vérification de l'affichage console
    captured = capsys.readouterr()
    assert "Alice" in captured.out
