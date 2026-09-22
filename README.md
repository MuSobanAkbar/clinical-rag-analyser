# Clinical Summary RAG Analyser

# What this is 

# How It Works
Starts by loading .env file, then it adds it on to the placeholder for Groq's API key.

It then uses PyPDFLoader to open the PDF file of the patient. If you are on terminal accessing this application, you can 
simply use the pdf provided in the repo (summary.pdf).

We are using a RecursiveCharacterSplitter, so that once the PDF Is loaded by PyPDFLoader, we can split/chunk the masisve document up for the small language model to read through one at a time, rather than go at it all once. In this specific program, we are making each chunk about 1,000 characters. With a 200 overlap, so there is sufficient context. 

We are also using ChromaDB to store the PDF in "collection". ChromaDB helps us here with semantic search since it takes the PDF and converts it into mathematical vectors, or embeddings.

"metadatas=[{"page": c.metadata.get("page", 0)} for c in chunks],", this is for citing the page to make sure we can cross verify any claims made by the AI. It then takes the question and searches chromaDB (the collection) 

We then pass the context, question, and temperature to the model for the final answer.





## Update 1st June
- containerized with Docker and deployed to K8s.
- k8s was with 3 replicas, service, config map, secret
- Github CI/CD
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
