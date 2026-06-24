from retriever import Retriever
from llm import ask_llm

# Load document
with open("document.md", "r", encoding="utf-8") as f:
    text = f.read()

# Split into sections
sections = text.split("# ")

# Create retriever object
retriever = Retriever()

# Ask question
question = input("Ask a question: ")

# Retrieve context
context = retriever.retrieve(question, sections)

# Build prompt
prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

# Get LLM response
answer = ask_llm(prompt)

print("\nAnswer:\n")
print(answer)
