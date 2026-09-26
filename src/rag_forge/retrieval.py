from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Chunk
from .database import engine
from .embedding import create_embedding

def retrieve(query: str, top_k: int =5):
    query_embedding = create_embedding(query)

    with Session(engine) as session:
        results = session.execute(
            select(Chunk).order_by(Chunk.embedding.cosine_distance(query_embedding)).limit(top_k)
        ).scalars().all()

        return [
            {
                "content": chunk.content,
                "metadata": chunk.meta,
                "chunk_index": chunk.chunk_index,
            }
            for chunk in results
        ]