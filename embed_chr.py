import os
import open_clip
import torch
from PIL import Image

# Load the OpenCLIP model
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
tokenizer = open_clip.get_tokenizer('ViT-B-32')

def embed_image(image_path):
    """Embed an image using OpenCLIP."""
    image = Image.open(image_path).convert("RGB")
    image_input = preprocess(image).unsqueeze(0)  # Preprocess and add batch dimension
    with torch.no_grad():
        image_features = model.encode_image(image_input)
    return image_features.squeeze().numpy()  # Convert to numpy array

def embed_text(text):
    """Embed a text query using OpenCLIP."""
    text_input = tokenizer([text])
    with torch.no_grad():
        text_features = model.encode_text(text_input)
    return text_features.squeeze().numpy()  # Convert to numpy array

def embed_images_in_folder(folder_path):
    """Embed all images in a folder and return a dictionary of {image_path: embedding}."""
    embeddings = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(root, file)
                embeddings[image_path] = embed_image(image_path)
    print(f"Generated embeddings for {len(embeddings)} images.")  # Debugging
    return embeddings

import os
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'