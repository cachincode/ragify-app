import os
from llama_index.core.indices import vector_store
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

chroma_db_name = os.getenv("CHROMA_DATABASE", "./dummy_db")
chroma_collection_name = os.getenv("CHROMA_COLLECTION", "dummy_collection")

def build_chroma_vector_store():
    exists = os.path.isdir(chroma_db_name)

    db = chromadb.PersistentClient(path=chroma_db_name)
    collection = db.get_or_create_collection(chroma_collection_name)
    vector_store = ChromaVectorStore(chroma_collection=collection)

    return vector_store, exists
