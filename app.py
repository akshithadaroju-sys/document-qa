import streamlit as st
import fitz
from retriever import Retriever
from llm import ask_llm

st.set_page_config(page_title="Local Document Q&A", page_icon="📄", layout="wide")

st.title("📄 Local-First Document Q&A Assistant")
st.caption("PyMuPDF + Groq Llama 3")

# ----------------------------
# Initialize session state
# ----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "sections" not in st.session_state:
    st.session_state.sections = None

retriever = Retriever()

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.header("Controls")

    mode = st.radio("Choose Mode", ["📄 Document Q&A", "🤖 General AI Chat"])

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# ----------------------------
# Upload PDF
# ----------------------------
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    doc = fitz.open("temp.pdf")

    text = ""
    for page in doc:
        text += page.get_text()

    pages = len(doc)
    doc.close()

    st.session_state.sections = text.split("\n\n")

    st.success("✅ PDF Loaded Successfully")

    st.info(
        f"""
📄 Pages: {pages}
📝 Characters: {len(text)}
📚 Sections: {len(st.session_state.sections)}
"""
    )

    # ----------------------------
    # Summary
    # ----------------------------
    if st.button("📄 Generate Summary"):

        with st.spinner("Generating Summary..."):

            summary_prompt = f"""
Summarize the following document in 5-10 bullet points.

Document:
{text[:10000]}
"""

            summary = ask_llm(summary_prompt)

            st.subheader("📄 Document Summary")
            st.write(summary)

    with st.expander("📖 Document Preview"):
        st.write(text[:2500])

# ----------------------------
# Show chat history
# ----------------------------
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# Chat input
# ----------------------------
question = st.chat_input("Ask anything...")

if question:

    st.session_state.chat_history.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    # ----------------------------
    # Document Q&A Mode
    # ----------------------------
    if mode == "📄 Document Q&A":

        if not st.session_state.sections:
            st.warning("⚠️ Please upload a PDF first.")
            st.stop()

        context = retriever.retrieve(question, st.session_state.sections)

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

    # ----------------------------
    # General AI Chat Mode
    # ----------------------------
    else:

        context = ""

        prompt = f"""
You are a helpful AI assistant.

Question:
{question}
"""

    # ----------------------------
    # LLM response
    # ----------------------------
    with st.spinner("Thinking..."):
        answer = ask_llm(prompt)

    st.session_state.chat_history.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)

    # Show retrieved context
    if mode == "📄 Document Q&A":
        with st.expander("🔍 Retrieved Context"):
            st.write(context)

# ----------------------------
# Download chat
# ----------------------------
if st.session_state.chat_history:

    chat_text = "\n".join(
        f"{msg['role']}: {msg['content']}" for msg in st.session_state.chat_history
    )

    st.download_button(
        label="⬇ Download Chat",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain",
    )
