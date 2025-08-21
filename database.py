from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DATABASE","tournament_db")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

def obj_to_str(doc):
    """Convert Mongo ObjectId to string."""
    if not doc:
        return None
    doc["_id"] = str(doc["_id"])
    return doc