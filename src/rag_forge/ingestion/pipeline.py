from .loader import load_markdown
from .cleaner import clean_text
from .chunker import chunk_text

def ingest_markdown(path: str) -> list[str]:
    text = load_markdown(path)
    cleaned = clean_text(text)
    chunks = chunk_text(cleaned)

    return chunks


