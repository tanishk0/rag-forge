import os 
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine =    create_engine(DATABASE_URL)

def test_connection():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("connected")