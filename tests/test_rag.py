from retriever import Retriever


def test_retriever_basic():
    retriever = Retriever()

    sections = [
        "Machine learning is powerful",
        "Python is a programming language",
        "Streamlit builds web apps",
    ]

    question = "What is Python?"

    result = retriever.retrieve(question, sections)

    assert "Python" in result
