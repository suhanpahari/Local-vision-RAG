from flask import Flask, request, jsonify, send_file
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
import chromadb
import os
from io import BytesIO
from matplotlib import pyplot as plt
from PIL import Image

app = Flask(__name__)

# Initialize ChromaDB
embedding_function = OpenCLIPEmbeddingFunction()
data_loader = ImageLoader()
client = chromadb.Client()

collection = client.create_collection(
    name='multimodal_collection',
    embedding_function=embedding_function,
    data_loader=data_loader
)

# Global variable to store the folder path
IMAGE_FOLDER = None

@app.route('/process-folder', methods=['POST'])
def process_folder():
    global IMAGE_FOLDER
    data = request.json
    IMAGE_FOLDER = data.get('folderPath', '')

    if not os.path.isdir(IMAGE_FOLDER):
        return jsonify({"status": "error", "message": "Invalid folder path."})

    image_uris = sorted([os.path.join(IMAGE_FOLDER, image_name) for image_name in os.listdir(IMAGE_FOLDER)])
    ids = [str(i) for i in range(len(image_uris))]
    collection.add(ids=ids, uris=image_uris)

    return jsonify({"status": "success", "message": "Folder processed successfully!"})


@app.route('/query', methods=['POST'])
def query_images():
    data = request.json
    query_text = data.get('query', '')

    if not query_text:
        return jsonify({"status": "error", "message": "Query text is required."})

    retrieved = collection.query(query_texts=[query_text], include=['data'], n_results=3)
    images = []

    for img_data in retrieved['data'][0]:
        img = Image.open(BytesIO(img_data))
        img_io = BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)
        images.append(img_io)

    return jsonify({"status": "success", "images": [img.getvalue().hex() for img in images]})


@app.route('/image/<int:index>', methods=['GET'])
def serve_image(index):
    image_path = sorted(os.listdir(IMAGE_FOLDER))[index]
    return send_file(os.path.join(IMAGE_FOLDER, image_path))


if __name__ == '__main__':
    app.run(debug=True)