# Local Image Search System 🖼️

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![ChromaDB](https://img.shields.io/badge/Vector%20Database-ChromaDB-brightgreen) ![CLIP](https://img.shields.io/badge/Model-OpenAI%20CLIP-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

## Overview

This project is a **local image search system** that enables users to search for images using natural language queries. By leveraging the **OpenAI CLIP model** for multimodal embeddings and **ChromaDB** as the vector database, the system offers efficient and accurate image retrieval based on textual descriptions.

<div align="center">
  <img src="https://github.com/user-attachments/assets/4abeccc6-2cd0-4ac7-a83f-ff6417b05f0b" alt="Image" width="400">
</div>

## Features

-  **Image Embedding:** Automatically embed all images from a specified folder into a vector database.
-  **Text-Based Search:** Input a natural language query to find the most relevant images.
-  **Multimodal Support:** Uses CLIP embeddings for both image and text inputs.
-  **Scalable Storage:** Efficiently stores and retrieves embeddings using ChromaDB.

<div align="center">
  <img src="https://github.com/user-attachments/assets/1f3b6276-7779-433f-b8a8-3e77be0af1b0" alt="Image" width="400">
</div>

## Project Structure

```plaintext
# multimodal_image_search/
├── app.py                # Flask App
├── tamplates/          
│ └── index.html          # UI file Index
│ └── static
|    └── syles.css        # Css File
|    └── script.js        # Script 
├── main.py               # CLI testing file
├── embed_chr.py          # Embedding file through CLIP
├── vector_chr.py         # Store to Chroma DB
├── query_chr.py          # Query processing
├── frame_separation.py   # Video to frame separator
└── requirements.txt      
```

## Installation

1.  **Clone the Repository**:

```bash
git clone https://github.com/suhanpahari/Local-vision-RAG.git
cd Local-vision-RAG
```

2.  **Install Dependencies**:

```bash
pip install -r requirements.txt
```

3.  **Set Up ChromaDB**: The project uses ChromaDB for storing vector embeddings. No additional setup is required as it persists to the local filesystem by default.

4.  **Environment Variables**: Create a `.env` file to configure your environment:

```env
CHROMA_DB_PATH=chroma_data # Path to persist ChromaDB
```

## Usage

### 1. Embed Images

Use the `embedding.py` script to embed all images in a specified folder:

```bash
python  embedding.py  --folder_path  /path/to/images
```

### 2. Save Embeddings to ChromaDB

Run the `vector.py` script to store the embeddings:

```bash
python  vector.py
```

### 3. Search Images

Run the `query.py` script to input a text query and retrieve the most similar images:

```bash
python  query.py  --query  "Frog"
```

### Example Output:

```plaintext
Similar Images:
1. /path/to/images/sunset1.jpg
2. /path/to/images/sunset2.jpg
```

## Requirements

- Python 3.10
- PyTorch
- Transformers
- Pillow
- ChromaDB

Install all dependencies using:

```bash
pip  install  -r  requirements.txt
```

## Technologies Used

-  **[OpenAI CLIP](https://github.com/openai/CLIP):** For generating multimodal embeddings.
-  **[ChromaDB](https://www.trychroma.com/):** As the vector database to store and query embeddings.
-  **PyTorch:** For running the CLIP model.

## License

This project is licensed under the MIT License. See the [LICENSE](https://chatgpt.com/c/LICENSE) file for more details.

## Contributing

Developed by [Soham Pahari](https://suhanxd.github.io/).
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## Acknowledgments

- OpenAI for the CLIP model.
- ChromaDB for providing a lightweight vector database solution.

----------
