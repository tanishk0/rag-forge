def build_context(chunks: list[dict]) -> str:
    return "\n\n".join(
        f"[Source: {chunk['metadata']['source']} | "
        f"Chunk: {chunk['chunk_index']}]\n"
        f"{chunk['content']}"
        for chunk in chunks
    )

