from embedding import embed_text
import pinecone
import os
from dotenv import load_dotenv
from pinecone import Pinecone 

load_dotenv()

api_key = "pcsk_3G4Aji_2cv5ZwFQG698wvnRotxkozt1HPMxzFcxeubTpjARXq8Ayz5EiiFvqzmkWMWBAst"  # Replace with your Pinecone API key
environment = "us-east-1"
pc = Pinecone(api_key=api_key)

# Connect to the index
index_name = "vision-rag"
index = pc.Index(index_name)

# Function to search for si milar images and return their paths
def search_images(query, top_k=5):
    query_embedding = embed_text(query)
    results = index.query(queries=[query_embedding], top_k=top_k)

    # Extract filenames and file paths from the results
    search_results = []
    for match in results['matches']:
        filename = match['metadata']['filename']
        file_path = match['metadata']['file_path']
        search_results.append({"filename": filename, "file_path": file_path})

    return search_results

