import pymupdf4llm

pdf_file = "sample.pdf"

markdown = pymupdf4llm.to_markdown(pdf_file)

with open("document.md", "w", encoding="utf-8") as f:
    f.write(markdown)

print("PDF converted successfully!")