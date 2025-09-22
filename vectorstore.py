from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
client = chromadb.Client()
collection = client.get_or_create_collection("edugenie_docs")
embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def add_document(doc_id, text):
    embedding = embed_model.encode(text).tolist()
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[doc_id]
    )

def search(query, top_k=3):
    query_embedding = embed_model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results['documents'][0] if results['documents'] else []