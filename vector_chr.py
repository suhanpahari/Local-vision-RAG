import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction

# Initialize ChromaDB client
client = chromadb.Client()

# Create or load a collection
collection = client.get_or_create_collection(
    name="image_search",
    embedding_function=OpenCLIPEmbeddingFunction()
)

def save_embeddings_to_chroma(embeddings):
    """Save image embeddings to ChromaDB."""
    ids = []
    embeddings_list = []
    metadatas = []

    for i, (image_path, embedding) in enumerate(embeddings.items()):
        ids.append(str(i))
        embeddings_list.append(embedding)
        metadatas.append({"image_path": image_path})

    collection.add(ids=ids, embeddings=embeddings_list, metadatas=metadatas)
    print(f"Saved {len(ids)} embeddings to ChromaDB.")  # Debugging

def query_chroma(query_embedding, top_k=5):
    """Query ChromaDB for the nearest images."""
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results["metadatas"]