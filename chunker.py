import re

with open("document.md", "r", encoding="utf-8") as f:
    text = f.read()

sections = re.split(r'\n# ', text)

chunks = []

for sec in sections:
    if sec.strip():
        chunks.append(sec.strip())

print("Sections:", len(chunks))