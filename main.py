from embed_chr import embed_images_in_folder
from vector_chr import save_embeddings_to_chroma

folder_path = "img"
embeddings = embed_images_in_folder(folder_path)
save_embeddings_to_chroma(embeddings)

# Example  usage
'''if __name__ == "__main__":
    query = "two rhino in the grass land"
    results = search_images(query)
    for result in results:
        print(f"Filename: {result['filename']}, File Path: {result['file_path']}")'''