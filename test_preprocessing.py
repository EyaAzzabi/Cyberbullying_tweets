# test_preprocessing.py

import unittest
import sys
import os

# Ajouter le chemin du dossier scripts au PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from preprocessing import clean_text

class TestPreprocessing(unittest.TestCase):
    def test_clean_text(self):
        input_text = "<b>Hello!</b> Visit https://test.com and call 1234"
        result = clean_text(input_text)
        self.assertTrue("hello" in result)
        self.assertFalse("https" in result)
        self.assertFalse("1234" in result)

if __name__ == "__main__":
    unittest.main()
