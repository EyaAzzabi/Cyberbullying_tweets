# test_scraper.py

import unittest
import pandas as pd
import os
import sys

# Ajouter le dossier scripts au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from scraper import load_and_clean_csv

class TestScraper(unittest.TestCase):
    def setUp(self):
        # Crée un mini fichier CSV de test
        self.test_csv = "test_scraper_data.csv"
        df = pd.DataFrame({
            "Text": ["Message 1", None],
            "Label": ["Bullying", "Not-Bullying"],
            "Types": ["Sexual", None]
        })
        df.to_csv(self.test_csv, index=False)

    def tearDown(self):
        # Supprime le fichier test après exécution
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_load_and_clean_csv(self):
        df_clean = load_and_clean_csv(self.test_csv)
        
        # Vérifie que la colonne id_post est bien créée
        self.assertIn("id_post", df_clean.columns)

        # Vérifie qu’il n’y a pas de valeurs manquantes dans Label
        self.assertFalse(df_clean["Label"].isnull().any())

        # Vérifie que les lignes invalides ont été supprimées
        self.assertEqual(len(df_clean), 1)

if __name__ == "__main__":
    unittest.main()
