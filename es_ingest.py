# es_ingest.py

from pymongo import MongoClient
from elasticsearch import Elasticsearch, helpers

def migrate_to_elasticsearch(
    mongo_uri="mongodb://localhost:27017/",
    db_name="harcelement",
    collection_name="posts",
    es_host="http://localhost:9200",
    index_name="harcelement_posts"
):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    documents = list(collection.find())

    es = Elasticsearch(es_host)

    # Supprimer l’index s’il existe déjà
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    # Préparer les documents à indexer
    actions = []
    for doc in documents:
        action = {
            "_index": index_name,
            "_id": str(doc["_id"]),
            "_source": {
                "id_post": doc.get("id_post"),
                "text": doc.get("Text"),
                "type": doc.get("Type"),
                "label": doc.get("Label"),
                "cleaned_text": doc.get("cleaned_text"),
                "language": doc.get("language"),
                "sentiment": doc.get("sentiment")
            }
        }
        actions.append(action)

    # Indexation dans Elasticsearch
    helpers.bulk(es, actions)
    print(f"{len(actions)} documents indexés dans Elasticsearch.")

if __name__ == "__main__":
    migrate_to_elasticsearch()
