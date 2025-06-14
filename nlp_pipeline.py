# nlp_pipeline.py

from pymongo import MongoClient
from langdetect import detect
from textblob import TextBlob

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            return "positive"
        elif polarity < -0.1:
            return "negative"
        else:
            return "neutral"
    except:
        return "unknown"

def enrich_mongo_documents(
    mongo_uri="mongodb://localhost:27017/",
    db_name="harcelement",
    collection_name="posts"
):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    documents = collection.find()
    updated_count = 0

    for doc in documents:
        text = doc.get("cleaned_text", "")
        lang = detect_language(text)
        sentiment = analyze_sentiment(text)

        collection.update_one(
            {"_id": doc["_id"]},
            {"$set": {
                "language": lang,
                "sentiment": sentiment
            }}
        )
        updated_count += 1

    print(f"{updated_count} documents enrichis avec langue et sentiment.")

if __name__ == "__main__":
    enrich_mongo_documents()
