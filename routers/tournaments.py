from fastapi import APIRouter, HTTPException
from typing import List
import db_helper
from models import tournament
from bson import ObjectId

router = APIRouter(prefix="/tournaments", tags=["Tournaments"])

@router.post("", response_model=tournament.Tournament)
async def create_tournament(tournament: tournament.Tournament):
    return await db_helper.create_item("tournaments", tournament.dict())

@router.get("", response_model=List[tournament.Tournament])
async def list_tournaments():
    return await db_helper.get_items("tournaments")

@router.get("/{tournament_id}", response_model=tournament.Tournament)
async def get_tournament(tournament_id: str):
    t = await db_helper.get_item("tournaments", {"_id":ObjectId(tournament_id)})
    if not t:
        raise HTTPException(404, "Tournament not found")
    return t

@router.put("/{tournament_id}", response_model=tournament.Tournament)
async def update_tournament(tournament_id: str, tournament_update: dict):
    updated = await db_helper.update_item("tournaments", {"_id":ObjectId(tournament_id)}, tournament_update)
    if not updated:
        raise HTTPException(404, "Tournament not found")
    return updated

@router.delete("/{tournament_id}")
async def delete_tournament(tournament_id: str):
    deleted = await db_helper.delete_item("tournaments", {"_id":ObjectId(tournament_id)})
    if not deleted:
        raise HTTPException(404, "Tournament not found")
    return {"status": "deleted"}