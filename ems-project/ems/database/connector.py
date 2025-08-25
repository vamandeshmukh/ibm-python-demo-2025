import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_client() -> MongoClient:
    uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    return MongoClient(uri)

def get_db():
    client = get_client()
    db_name = os.getenv("MONGO_DB", "ems")
    return client[db_name]
