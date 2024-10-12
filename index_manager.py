from llama_index.core import (
    StorageContext,
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings
)
from llama_index.core.base.base_query_engine import BaseQueryEngine
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

from utils.vector_database import build_chroma_vector_store

Settings.llm = Ollama(model="llama3.1", request_time=360.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

vector_store, vector_store_exists = build_chroma_vector_store()

storage_context = StorageContext.from_defaults(
    vector_store = vector_store,
)

def initialize_index() -> BaseQueryEngine:
    if vector_store_exists:
        index = VectorStoreIndex.from_vector_store(vector_store=vector_store, storage_context=storage_context)
    else:
        documents = SimpleDirectoryReader(input_dir="./data").load_data(show_progress=True)
        index = VectorStoreIndex.from_documents(documents=documents, storage_context=storage_context)

    query_engine = index.as_query_engine(similarity_top_k=5)

    return query_engine
