from retriever import retrieve
from llm import ask_llm

with open("document.md", "r", encoding="utf-8") as f:
    text = f.read()

sections = text.split("# ")

question = input("Ask a question: ")

context = retrieve(question, sections)

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

answer = ask_llm(prompt)

print("\nAnswer:\n")
print(answer)