from .retrieval import retrieve
from .context import build_context
from .generation import generate_answer


def ask(question: str):
    chunks = retrieve(question)

    print("RETRIEVED CHUNKS:")
    for chunk in chunks:
        print(chunk["content"])
        print("---")

    context = build_context(chunks)

    return generate_answer(
        question=question,
        context=context
    )