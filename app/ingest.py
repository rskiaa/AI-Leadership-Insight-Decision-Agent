import os
import pickle

import faiss
import numpy as np
from google import genai
from pypdf import PdfReader

from config import DATA_PATH, EMBEDDING_MODEL, GEMINI_API_KEY, VECTOR_DB_PATH


def load_documents():
    docs = []
    os.makedirs(DATA_PATH, exist_ok=True)
    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)
        if file.endswith(".pdf"):
            reader = PdfReader(path)
            for page_num, page in enumerate(reader.pages, start=1):
                text = (page.extract_text() or "").strip()
                if text:
                    docs.append(
                        {
                            "page_content": text,
                            "metadata": {
                                "source": file,
                                "page": page_num,
                            },
                        }
                    )
        elif file.endswith((".txt", ".md")):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()
            if text:
                docs.append(
                    {
                        "page_content": text,
                        "metadata": {
                            "source": file,
                            "page": 1,
                        },
                    }
                )
    return docs


def split_text(text, chunk_size=500, chunk_overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end == len(text):
            break
        start = max(0, end - chunk_overlap)
    return chunks


def split_documents(docs):
    chunks = []
    for doc in docs:
        for chunk in split_text(doc["page_content"]):
            chunks.append(
                {
                    "page_content": chunk,
                    "metadata": doc["metadata"],
                }
            )
    return chunks


def embed_texts(chunks):
    if not GEMINI_API_KEY:
        raise ValueError("Missing GEMINI_API_KEY in environment")

    client = genai.Client(api_key=GEMINI_API_KEY)
    embeddings = []
    for chunk in chunks:
        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=chunk["page_content"],
        )
        embeddings.append(response.embeddings[0].values)
    return np.array(embeddings, dtype="float32")


def create_vector_store(chunks):
    vectors = embed_texts(chunks)
    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    os.makedirs(os.path.dirname(VECTOR_DB_PATH), exist_ok=True)
    faiss.write_index(index, f"{VECTOR_DB_PATH}.faiss")
    with open(f"{VECTOR_DB_PATH}.pkl", "wb") as f:
        pickle.dump(chunks, f)


def run_ingestion():
    docs = load_documents()
    if not docs:
        raise ValueError(f"No PDF documents found in {DATA_PATH}")
    chunks = split_documents(docs)
    create_vector_store(chunks)

if __name__ == "__main__":
    run_ingestion()
