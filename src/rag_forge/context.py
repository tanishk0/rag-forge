def build_context(chunks: list[dict]) -> str:
    return "\n\n".join(
        chunk["content"]
        for chunk in chunks
    )