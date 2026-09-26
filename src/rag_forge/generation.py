import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

def generate_answer(question: str, context: str) -> str: 
    prompt= f"""Answer the following questions onnly using the provided context.
    context={context} 
    question={question}
    If the context does not contain the answer, say:
    "I don't know based on the provided context."
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text