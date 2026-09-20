import os 
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from .models import Base

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