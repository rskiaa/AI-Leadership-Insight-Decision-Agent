from google import genai
from config import GEMINI_API_KEY, MODEL_NAME


def get_llm_client():
    if not GEMINI_API_KEY:
        raise ValueError("Missing GEMINI_API_KEY in environment")
    return genai.Client(api_key=GEMINI_API_KEY)


def get_model_name():
    return MODEL_NAME
