# AI Leadership Insight Agent - Solution Overview

## Problem Understanding
The goal is to build an AI system that can:
- Ingest company documents
- Answer leadership-level questions
- Provide structured, decision-friendly insights grounded in internal context

This directly maps to the coding task requirement:
- understand company documents
- answer leadership questions about current working, performance, and status
- generate concise, factual responses grounded in internal documents

## Approach

### 1. Document Processing
- Input: company reports, strategy notes, and operational updates stored in `data/raw_docs/`
- Supported formats: `.txt`, `.md`, and `.pdf`
- Documents are split into smaller chunks for better retrieval quality

### 2. Embedding and Storage
- Text chunks are converted into vector embeddings using Gemini embeddings
- Embeddings are stored in a FAISS vector database for fast semantic similarity search

### 3. Retrieval (RAG)
- User query is embedded using the same embedding model
- Top relevant chunks are retrieved from FAISS
- Retrieved context is passed into the response-generation step

### 4. LLM Reasoning
- Gemini is used to generate structured leadership insights
- Responses are designed to include:
  - Executive Summary
  - Key Insights
  - Risks and Concerns
  - Recommendations
  - Source references

## Architecture Summary
- `app/ingest.py`: loads documents, chunks text, generates embeddings, builds FAISS index
- `app/retriever.py`: retrieves top-k relevant chunks for a given leadership query
- `app/pipeline.py`: assembles prompt, calls the model, and formats the final answer
- `app/streamlit_app.py`: interactive UI for leadership questions

## Assumptions
- Northstar Dynamics is a simulated enterprise dataset used for demonstration
- Documents are semi-structured and contain enough business context for leadership Q&A
- User questions are strategic or operational, not transactional row-level queries
- The system is intended for grounded insight generation, not authoritative financial reporting

## Example Leadership Questions From the Prompt
- What is our current revenue trend?
- Which departments are underperforming?
- What were the key risks highlighted in the last quarter?

## Sample Queries and Example Outputs

### Query
`What is our current revenue trend?`

### Example Output
- Revenue is growing at a healthy year-over-year pace
- Annual performance shows 16 percent growth, while Q4 shows 14 percent year-over-year growth
- Enterprise renewals and cross-sell activity are the main growth drivers
- SMB demand is softer and should be monitored

### Query
`Which departments are underperforming?`

### Example Output
- No department is explicitly labeled as underperforming in the documents
- However, operational pressure is visible in implementation, professional services, and AI deployment support
- Hiring gaps in AI engineering and solutions architecture are slowing delivery capacity
- Sales-to-implementation handoff quality is also creating execution friction

### Query
`What are the key risks highlighted in the last quarter?`

### Example Output
- Implementation backlog is rising and may delay onboarding
- Delivery staffing remains tight, especially in Europe
- Slower ramp-up for new sales hires could affect future conversion
- Revenue recognition risk exists if implementations slip into later quarters

### Query
`Which areas appear operationally constrained?`

### Example Output
- Professional services capacity is stretched
- AI engineering and solutions architecture hiring are behind plan
- Sales-to-implementation handoff quality is still a weakness
- Enterprise deployment demand is stronger than current delivery capacity

## Enhancements Added
- Streamlit UI for interactive usage
- Modular architecture with separate ingestion, retrieval, and generation layers
- Configurable environment-based model setup
- Example enterprise documents across annual, quarterly, strategy, and operational categories
- Source citations in generated answers

## Future Scope
- Multi-agent decision support for deeper strategy analysis
- Automated recommendation chains and action tracking
- Dashboard analytics and trend visualization
- Role-specific views for executives, operations, and finance leaders
