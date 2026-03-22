import pickle

import faiss
import numpy as np
from google import genai

from config import EMBEDDING_MODEL, GEMINI_API_KEY, VECTOR_DB_PATH


class GeminiRetriever:
    def __init__(self, k=5):
        if not GEMINI_API_KEY:
            raise ValueError("Missing GEMINI_API_KEY in environment")
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.index = faiss.read_index(f"{VECTOR_DB_PATH}.faiss")
        with open(f"{VECTOR_DB_PATH}.pkl", "rb") as f:
            self.documents = pickle.load(f)
        self.k = k

    def invoke(self, query):
        response = self.client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=query,
        )
        vector = np.array([response.embeddings[0].values], dtype="float32")
        _, indices = self.index.search(vector, self.k)
        return [self.documents[idx] for idx in indices[0] if idx != -1]


def get_retriever():
    return GeminiRetriever(k=5)
