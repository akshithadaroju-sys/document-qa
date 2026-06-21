import streamlit as st
import pymupdf4llm
from retriever import retrieve
from llm import ask_llm

st.set_page_config(
    page_title="Local Document Q&A",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Local-First Document Q&A Assistant")
st.caption("PyMuPDF4LLM + Llama.cpp")

# Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "sections" not in st.session_state:
    st.session_state.sections = None

# Sidebar
with st.sidebar:
    st.header("Controls")

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    markdown = pymupdf4llm.to_markdown("temp.pdf")

    with open("document.md", "w", encoding="utf-8") as f:
        f.write(markdown)

    st.session_state.sections = markdown.split("# ")

    st.success("✅ PDF Loaded Successfully")

    with st.expander("📖 Document Preview"):
        st.write(markdown[:2500])

# Show Chat History
for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
question = st.chat_input(
    "Ask anything about the document..."
)

if question and st.session_state.sections:

    # Show User Message
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Retrieve Context
    context = retrieve(
        question,
        st.session_state.sections
    )

    # Include previous chat history
    conversation = ""

    for msg in st.session_state.chat_history[-6:]:
        conversation += f"{msg['role']}: {msg['content']}\n"

    prompt = f"""
You are a helpful document assistant.

Conversation:
{conversation}

Document Context:
{context}

Question:
{question}

Answer using only the document context.
"""

    answer = ask_llm(prompt)

    # Save assistant reply
    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

    with st.expander("🔍 Retrieved Context"):
        st.write(context)