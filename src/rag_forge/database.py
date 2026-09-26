import os 
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from .models import Base
from .models import Document, Chunk
from sqlalchemy.orm import Session
from .embedding import create_embedding

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine =    create_engine(DATABASE_URL)

def test_connection():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("connected")


def create_tables():
    with engine.begin() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))

        Base.metadata.create_all(engine)


def save_document(source: str, content: str, chunks: list[dict]):
    with Session(engine) as session:
        document = Document(
            source=source,
            content=content
        )

        session.add(document)
        session.flush() #generates  document.id

        for chunk in chunks: 
            embedding = create_embedding(chunk["content"])
            session.add(
                Chunk(
                    document_id = document.id,
                    content=chunk["content"],
                    chunk_index=chunk["chunk_index"],
                    meta={"source": chunk["source"]},
                    embedding=embedding,
                )
            )

        session.commit()