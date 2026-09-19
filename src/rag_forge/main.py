from fastapi import FastAPI
from .database import test_connection


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

test_connection()