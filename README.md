# Clinical Summary RAG Analyser

# What this is
This takes clinical summaries pdfs, and gives concise feedbacks based on the pdf.

# How this works
This cuts an uploaded pdf into small chunks that has an overlap as well, to avoid confusion due to lack of context. Then it uses embedding (chromadb), to find similarities in the question to pick out the best part chunk and give it over to Groq's API as context to reply accordingly.

# How to run this
Paste your Groq API key in the .env file, have your PDF in the same folder as this, and run.
