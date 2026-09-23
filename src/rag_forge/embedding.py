import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def create_embedding(text: str) -> list[float]:
    response = client.models.emdeb_content(
        model="gemini-embedding-2",
        contents=text,
        config={"output_dimensionality": 1536},
    )

    return response.embeddings[0].values