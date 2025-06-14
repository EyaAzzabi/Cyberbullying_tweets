# preprocess_mongo.py

from pymongo import MongoClient
import sys
import os

from preprocessing import clean_text

def preprocess_mongo_documents(
    mongo_uri="mongodb://localhost:27017/",
    db_name="harcelement",
    collection_name="posts"
):
    # Connexion à MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Lecture des documents
    documents = collection.find()
    updated_count = 0

    for doc in documents:
        text = doc.get("Text", "")
        cleaned = clean_text(text)

        # Mise à jour du document avec le texte nettoyé
        collection.update_one(
            {"_id": doc["_id"]},
            {"$set": {"cleaned_text": cleaned}}
        )
        updated_count += 1

    print(f"{updated_count} documents mis à jour avec cleaned_text.")

if __name__ == "__main__":
    preprocess_mongo_documents()
