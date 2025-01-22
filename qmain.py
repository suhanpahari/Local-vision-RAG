from embedding import embed_text
from pinecone import Pinecone
from query import search_images


if __name__ == "__main__":
    query = "two rhino in the grass land"
    results = search_images(query)
    for result in results:
        print(f"Filename: {result['filename']}, File Path: {result['file_path']}") #