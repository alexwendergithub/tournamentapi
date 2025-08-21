from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional

class Tournament(BaseModel):
    id: Optional[str] = Field(default=None,alias="_id")
    name: str
    description: str | None = None
    pairing_system: int
    scoring: int