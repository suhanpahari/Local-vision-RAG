import open_clip
import torch
from PIL import Image

# Load the OpenCLIP model
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
tokenizer = open_clip.get_tokenizer('ViT-B-32')

# Test the model with an image
image_path = "img/frame_0705.jpg"
image = Image.open(image_path).convert("RGB")
image_input = preprocess(image).unsqueeze(0)  # Preprocess and add batch dimension

with torch.no_grad():
    image_features = model.encode_image(image_input)
    print(f"Image features: {image_features}")