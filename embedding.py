from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import os
import torch


model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
model.eval()  # Set to evaluation mode


def embed_image(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt", padding=True)
    with torch.no_grad():
        embedding = model.get_image_features(**inputs).squeeze().tolist()
    return embedding


def embed_text(query):
    inputs = processor(text=query, return_tensors="pt", padding=True)
    with torch.no_grad():
        embedding = model.get_text_features(**inputs).squeeze().tolist()
    return embedding


def embed_images_in_folder(folder_path):
    embeddings = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            embeddings[filename] = embed_image(file_path)
    return embeddings
