
import streamlit as st

st.set_page_config(
    page_title="NexusRAG",
    page_icon="🔎",
    layout="wide"
)

st.title("NexusRAG")
st.subheader("Advanced RAG for Document Question Answering")

st.info(
    "The Streamlit interface is under development. "
    "The working prototype currently runs in Google Colab."
)

st.markdown("""
### RAG Pipeline

1. PDF Text Extraction
2. Text Chunking
3. Multilingual Embeddings
4. FAISS + BM25 Hybrid Retrieval
5. Cross-Encoder Reranking
6. Qwen Answer Generation
""")

st.warning(
    "Question answering is not connected to this interface yet. "
    "Please use the notebook to run the current prototype."
)

pdf = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)

if pdf:
    st.success(f"Selected file: {pdf.name}")
    st.caption("PDF processing will be integrated in a future version.")
