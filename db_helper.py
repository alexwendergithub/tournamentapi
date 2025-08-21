from database import db, obj_to_str
from bson import ObjectId
from typing import Optional

def serialize_mongo(doc):
    if not doc:
        return None
    doc["_id"] = str(doc["_id"])
    return doc

async def create_item(collection: str, data: dict):
    result = await db[collection].insert_one(data)
    return serialize_mongo(await db[collection].find_one({"_id": result.inserted_id}))

async def get_item(collection: str, query):
    return serialize_mongo(await db[collection].find_one(query))

async def get_items(collection: str, query: dict = {}):
    items = []
    async for doc in db[collection].find(query):
        items.append(serialize_mongo(doc))
    return items

async def update_item(collection: str, query, data: dict):
    await db[collection].update_one(query, {"$set": data})
    return serialize_mongo(await get_item(collection, data))

async def delete_item(collection: str, query):
    result = await db[collection].delete_one(query)
    return result.deleted_count > 0