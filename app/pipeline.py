from retriever import get_retriever
from llm import get_llm_client, get_model_name


def generate_answer(query):
    retriever = get_retriever()
    llm_client = get_llm_client()
    model_name = get_model_name()

    docs = retriever.invoke(query)
    context = "\n\n".join([doc["page_content"] for doc in docs])

    prompt = f"""
You are a senior AI strategy consultant.

Provide:
- Executive Summary (2-3 lines)
- Key Insights (bullet points)
- Risks & Concerns
- Recommendations

Base strictly on context.

Context:
{context}

Question:
{query}
"""

    response = llm_client.models.generate_content(
        model=model_name,
        contents=prompt,
    ).text
    sources = "\n".join(
        f"- {doc['metadata'].get('source', 'Unknown source')} (page {doc['metadata'].get('page', '?')})"
        for doc in docs
    )
    return f"{response}\n\nSources:\n{sources}"
