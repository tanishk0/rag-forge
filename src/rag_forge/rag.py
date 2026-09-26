from .retrieval import retrieve
from .context import build_context
from .generation import generate_answer


def ask(question: str) -> str:
    chunks = retrieve(question)
    context = build_context(chunks)

    return generate_answer(
        question=question,
        context=context
    )