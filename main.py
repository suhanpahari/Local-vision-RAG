from embedding import embed_images_in_folder
from vector import save_embeddings_to_pinecone

folder_path = "img"
embeddings = embed_images_in_folder(folder_path)
save_embeddings_to_pinecone(embeddings, folder_path)

# Example usage
'''if __name__ == "__main__":
    query = "two rhino in the grass land"
    results = search_images(query)
    for result in results:
        print(f"Filename: {result['filename']}, File Path: {result['file_path']}")'''