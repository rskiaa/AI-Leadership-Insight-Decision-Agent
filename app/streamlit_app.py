import streamlit as st
from pipeline import generate_answer

st.set_page_config(page_title="AI Leadership Insight Agent")

st.title("AI Leadership Insight Agent")

query = st.text_input("Ask a leadership question")

if st.button("Generate Insight"):
    if query:
        with st.spinner("Analyzing documents..."):
            try:
                response = generate_answer(query)
            except Exception as exc:
                st.error(f"Unable to generate insight: {exc}")
            else:
                st.success("Done!")
                st.markdown("### AI Generated Insight")
                st.write(response)
    else:
        st.warning("Please enter a question")
