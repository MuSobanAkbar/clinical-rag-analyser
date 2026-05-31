# Clinical Summary RAG Analyser

# What this is
This takes clinical summaries pdfs, and gives concise answers to questions ONLY ABOUT the given pdf.

## update 1st june
- containerized with Docker and deployed to K8s.
- k8s was with 3 replicas, service, config map, secret

# How this works
This cuts an uploaded pdf into small chunks that has an overlap as well, to avoid confusion due to lack of context. Then it uses embedding (chromadb), to find similarities in the question to pick out the best part chunk and give it over to Groq's API as context to reply accordingly.

# How to run this
Paste your Groq API key in the .env file, have your PDF in the same folder as this, and run.

# Live Demo
https://huggingface.co/spaces/sobanakbar/client-summary

# Tech Stack
- Python 3.11
- Groq (openai/gpt-oss-120b):  answer generation
- ChromaDB: local vector database (embeds with all-MiniLM-L6-v2, no API key)
- LangChain: PDF loading + chunking
- Gradio: web UI, deployed on Hugging Face Spaces

# Evaluation Test Results
## Pre-tuning
- Correctly answered: 15
- Correctly said "I don't know": 4
- Hallucinated: 1
## After-tuning
- Correctly answered: 16
- Correctly said "I don't know": 4
- Hallucinated: 0
- Temperature was brought down from 0.2 to 0.0
