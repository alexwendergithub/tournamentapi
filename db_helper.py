from database import db, obj_to_str
from bson import ObjectId
from typing import Optional

async def create_item(collection: str, data: dict):
    result = await db[collection].insert_one(data)
    return obj_to_str(await db[collection].find_one({"_id": result.inserted_id}))

async def get_item(collection: str, item_id: str):
    doc = await db[collection].find_one({"_id": ObjectId(item_id)})
    return obj_to_str(doc)

async def get_items(collection: str, query: dict = {}):
    items = []
    async for doc in db[collection].find(query):
        items.append(obj_to_str(doc))
    return items

async def update_item(collection: str, item_id: str, data: dict):
    await db[collection].update_one({"_id": ObjectId(item_id)}, {"$set": data})
    return await get_item(collection, item_id)

async def delete_item(collection: str, item_id: str):
    result = await db[collection].delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0