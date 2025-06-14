# test_nlp_pipeline.py

import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from nlp_pipeline import detect_language, analyze_sentiment

class TestNLPPipeline(unittest.TestCase):
    def test_detect_language(self):
        english = "This is a test."
        french = "Ceci est un test."
        unknown = "😊😂👍"

        self.assertEqual(detect_language(english), "en")
        self.assertEqual(detect_language(french), "fr")
        self.assertEqual(detect_language(unknown), "unknown")

    def test_analyze_sentiment(self):
        positive = "I love this"
        negative = "I hate this"
        neutral = "It is a table"

        self.assertEqual(analyze_sentiment(positive), "positive")
        self.assertEqual(analyze_sentiment(negative), "negative")
        self.assertEqual(analyze_sentiment(neutral), "neutral")

if __name__ == "__main__":
    unittest.main()
