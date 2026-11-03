
# NexusRAG — Advanced RAG System

NexusRAG is a prototype Retrieval-Augmented Generation (RAG) system for document question answering.

It retrieves relevant information from PDF documents and uses a Large Language Model (LLM) to generate answers grounded in the retrieved context.

## Features

- PDF text extraction using PyMuPDF
- Text chunking with page metadata
- Multilingual embeddings using multilingual-e5-small
- Dense retrieval with FAISS
- Sparse retrieval with BM25
- Hybrid retrieval using Reciprocal Rank Fusion (RRF)
- Cross-encoder reranking
- Answer generation using Qwen2.5-1.5B-Instruct
- Source-aware answers with page references

## Architecture

PDF → Text Extraction → Chunking → Embeddings

FAISS + BM25 → Hybrid Retrieval → Reranking

→ Qwen LLM → Answer with Sources

## Tech Stack

Python, PyTorch, Hugging Face Transformers,
Sentence Transformers, FAISS, BM25, PyMuPDF, Streamlit

## Test

The core pipeline was manually tested in Google Colab.

A sample question about the Atlas project's embedding dimension returned 384, with relevant source passages retrieved from the PDF.

## Project Status

Prototype / Work in Progress.

The retrieval and generation pipeline has been tested in Google Colab. The Streamlit interface is not yet connected to the RAG pipeline.

## Future Improvements

- Complete Streamlit integration
- Retrieval evaluation using Recall@K, MRR and nDCG
- Automated tests
- Docker deployment
