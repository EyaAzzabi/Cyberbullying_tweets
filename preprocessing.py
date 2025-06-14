# preprocessing.py

import re
import string
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Télécharger les ressources nécessaires une seule fois
nltk.download('stopwords')
nltk.download('wordnet')

# Initialiser les outils NLP
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    # 1. Convertir en minuscules
    text = text.lower()

    # 2. Supprimer les balises HTML
    text = BeautifulSoup(text, "html.parser").get_text()

    # 3. Supprimer les URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # 4. Supprimer les chiffres
    text = re.sub(r"[0-9]+", "", text)

    # 5. Supprimer la ponctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # 6. Supprimer les caractères spéciaux (non-lettres)
    text = re.sub(r"[^a-z\s]", "", text)

    # 7. Séparer les mots
    words = text.split()

    # 8. Supprimer les stopwords
    words = [w for w in words if w not in stop_words]

    # 9. Appliquer la lemmatisation
    words = [lemmatizer.lemmatize(w) for w in words]

    return " ".join(words)
