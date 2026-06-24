from chunker import chunk_text


def test_chunk_text_basic():
    text = "# Title\nHello world"
    chunks = chunk_text(text)

    assert len(chunks) == 1
    assert "Hello world" in chunks[0]
