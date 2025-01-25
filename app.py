from flask import Flask, render_template, request, jsonify
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
import chromadb
import os
import base64
import io
from matplotlib import pyplot as plt

app = Flask(__name__)

class ImageSearchEngine:
    def __init__(self):
        self.embedding_function = OpenCLIPEmbeddingFunction()
        self.data_loader = ImageLoader()
        self.client = chromadb.Client()
        self.collection = None
        self.image_uris = []

    def process_folder(self, folder_path):
        try:
            # Validate folder path
            if not os.path.isdir(folder_path):
                return False, "Invalid folder path"

            # Create or reset collection
            if self.collection:
                self.client.delete_collection(name='multimodal_collection')
            
            self.collection = self.client.create_collection(
                name='multimodal_collection',
                embedding_function=self.embedding_function,
                data_loader=self.data_loader
            )

            # Get image URIs
            self.image_uris = sorted([os.path.join(folder_path, image_name) 
                                      for image_name in os.listdir(folder_path) 
                                      if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))])
            
            # Add images to collection
            ids = [str(i) for i in range(len(self.image_uris))]
            self.collection.add(ids=ids, uris=self.image_uris)
            
            return True, f"Processed {len(self.image_uris)} images"
        except Exception as e:
            return False, str(e)

    def search_images(self, query, n_results=1):
        if not self.collection:
            return []

        try:
            retrieved = self.collection.query(query_texts=[query], include=['data'], n_results=n_results)
            
            # Convert images to base64 for web display
            base64_images = []
            for img in retrieved['data'][0]:
                # Convert matplotlib image to base64
                buf = io.BytesIO()
                plt.figure(figsize=(8, 8))
                plt.imshow(img)
                plt.axis('off')
                plt.tight_layout()
                plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
                buf.seek(0)
                base64_image = base64.b64encode(buf.getvalue()).decode('utf-8')
                plt.close()
                base64_images.append(base64_image)
            
            return base64_images
        except Exception as e:
            print(f"Search error: {e}")
            return []

# Global search engine instance
search_engine = ImageSearchEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_folder', methods=['POST'])
def process_folder():
    folder_path = request.json.get('folderPath')
    success, message = search_engine.process_folder(folder_path)
    return jsonify({'success': success, 'message': message})

@app.route('/search_images', methods=['POST'])
def search_images():
    query = request.json.get('query')
    images = search_engine.search_images(query)
    return jsonify({'images': images})

if __name__ == '__main__':
    app.run(debug=True)