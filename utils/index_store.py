import os

from llama_index.storage.index_store.mongodb import MongoIndexStore
from pymongo import MongoClient


mongo_uri = os.getenv("MONGO_URI", "")
mongo_db = os.getenv("MONGO_DATABASE", "")

db = MongoClient(host=mongo_uri).get_database(name=mongo_db)


def get_existing_indexes():
    """
    Get the existing index store
    """
    indexes = []

    items = db['index_store/data'].find({})

    for item in items:
        indexes.append(item)

    return indexes


def build_index_store():
    """
    Build an index store with Llama Index
    """
    return MongoIndexStore.from_uri(uri=mongo_uri, db_name=mongo_db)
