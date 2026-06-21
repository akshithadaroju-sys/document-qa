# 📄 Local-First Document Q&A Assistant

A local Retrieval-Augmented Generation (RAG) application built with Streamlit, PyMuPDF4LLM, and TinyLlama running locally through llama.cpp.

## Features

* Upload PDF documents
* Ask questions about uploaded PDFs
* Local LLM inference using TinyLlama
* Chat history support
* Clear chat functionality
* No external API required

## Tech Stack

* Streamlit
* PyMuPDF4LLM
* llama-cpp-python
* TinyLlama GGUF
* Python

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Model

Download a TinyLlama GGUF model and place it inside:

models/

Then update the model path in `llm.py` if needed.
