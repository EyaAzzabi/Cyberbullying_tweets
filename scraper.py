#scraper.py

import pandas as pd
from pymongo import MongoClient
import uuid

def load_and_clean_csv(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["Text", "Label"])  # supprime les lignes avec texte ou label manquant
    df["Label"] = df["Label"].str.replace(" ", "").str.lower()  # uniformise le label
    df["Type"] = df["Types"].fillna("Unknown")  # remplace les types manquants
    df["id_post"] = [str(uuid.uuid4()) for _ in range(len(df))]  # id unique
    return df[["id_post", "Text", "Type", "Label"]]

def insert_into_mongodb(df, mongo_uri="mongodb://localhost:27017/", db_name="harcelement", collection_name="posts"):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    records = df.to_dict(orient="records")
    collection.delete_many({})  # vide la collection si déjà existante
    collection.insert_many(records)
    print(f"{len(records)} documents insérés dans MongoDB.")

if __name__ == "__main__":
    csv_file = "Cyberbullying_tweets.csv"  # chemin à adapter
    df_clean = load_and_clean_csv(csv_file)
    insert_into_mongodb(df_clean)
