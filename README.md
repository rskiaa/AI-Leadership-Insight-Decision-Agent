# AI Leadership Insight Agent

## Overview
AI-powered leadership assistant that ingests internal company documents, retrieves relevant business context, and generates grounded strategic insights for leadership questions.

## Features
- Document ingestion from company reports, strategy notes, and operational updates
- FAISS-based semantic retrieval for relevant context lookup
- Gemini-powered answer generation with structured leadership insights
- Streamlit UI for interactive querying

## Model Used
- LLM: `gemini-2.5-flash`
- Embedding Model: `gemini-embedding-001`

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
`python3 -m streamlit run app/streamlit_app.py`

## Example Questions
- What is our current revenue trend?
- Which departments are underperforming?
- What were the key risks highlighted in the last quarter?

## Architecture
- `app/ingest.py`: Loads documents, chunks text, generates embeddings, and stores the FAISS index
- `app/retriever.py`: Retrieves relevant document chunks for each leadership query
- `app/pipeline.py`: Builds the prompt and generates grounded responses with citations
- `app/streamlit_app.py`: Provides the interactive UI
