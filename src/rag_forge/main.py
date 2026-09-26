from contextlib import asynccontextmanager
from fastapi import FastAPI

from .database import create_tables, save_document
from .ingestion.pipeline import ingest_markdown


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()

    cleaned, chunks = ingest_markdown("src/rag_forge/test.md")

    save_document(
        source="src/rag_forge/test.md",
        content=cleaned,
        chunks=chunks
    )

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}