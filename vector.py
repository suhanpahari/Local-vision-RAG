import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()



api_key = "pcsk_3G4Aji_2cv5ZwFQG698wvnRotxkozt1HPMxzFcxeubTpjARXq8Ayz5EiiFvqzmkWMWBAst"  # Replace with your Pinecone API key
environment = "us-east-1"  # Replace with your Pinecone environment (e.g., "us-west1-gcp-free")
pc = Pinecone(api_key=api_key)

# Check and create the index if it doesn't exist
index_name = "vision-rag"
if index_name not in [idx.name for idx in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=512,  # Adjust this to match your embedding dimensions
        metric="cosine",  # Use cosine similarity for CLIP embeddings
        spec=ServerlessSpec(cloud="aws", region=environment)  # Correct the region
    )

# Connect to the index
index = pc.Index(index_name)

# Function to save embeddings into Pinecone with image metadata
def save_embeddings_to_pinecone(embeddings, folder_path):
    for i, (filename, embedding) in enumerate(embeddings.items()):
        file_path = os.path.join(folder_path, filename)
        index.upsert(vectors=[(f"img_{i}", embedding, {"filename": filename, "file_path": file_path})])
    print("Embeddings saved successfully.")