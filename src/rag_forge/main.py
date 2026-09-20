from fastapi import FastAPI
from .database import test_connection
from .database import test_connection, create_tables




app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

test_connection()
create_tables()