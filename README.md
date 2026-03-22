# AI Leadership Insight Agent

## Overview
RAG-based AI assistant to analyze company documents and answer leadership questions.

## Setup
1. Install dependencies:
   `python3 -m pip install -r requirements.txt`
2. Create `.env` from `.env.example` and set `GEMINI_API_KEY`.
3. Add PDFs or text documents to `data/raw_docs/`.

## Run Ingestion
`python3 app/ingest.py`

## Run CLI
`python3 app/main.py`

## Run UI
`streamlit run app/streamlit_app.py`
