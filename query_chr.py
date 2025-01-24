from embed_chr import embed_text
from vector_chr import query_chroma
from matplotlib import pyplot as plt
from PIL import Image

import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction

# Initialize ChromaDB client with persistent storage
client = chromadb.PersistentClient(path="chroma_db")

# Load the collection
collection = client.get_collection(
    name="image_search",
    embedding_function=OpenCLIPEmbeddingFunction()
)

def search_images_by_text(query_text, top_k=5):
    """Search for images using a text query."""
    # Embed the query text
    query_embedding = embed_text(query_text)

    # Query ChromaDB for the nearest images
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)

    # Debugging: Print the results
    print(f"Query results: {results}")

    # Extract image paths from the results
    image_paths = [item["image_path"] for item in results["metadatas"][0]]
    return image_paths

def display_images(image_paths):
    """Display images using matplotlib."""
    fig, axes = plt.subplots(1, len(image_paths), figsize=(15, 5))
    for i, path in enumerate(image_paths):
        img = Image.open(path)
        axes[i].imshow(img)
        axes[i].axis("off")  # Hide axes
    plt.show()

if __name__ == "__main__":
    query_text = "Rhino"
    results = search_images_by_text(query_text)
    print("Search results:")
    for path in results:
        print(path)
    display_images(results)