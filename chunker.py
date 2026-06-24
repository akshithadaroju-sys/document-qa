import re


def chunk_text(text: str):
    sections = re.split(r"\n# ", text)

    chunks = []
    for sec in sections:
        if sec.strip():
            chunks.append(sec.strip())

    return chunks
