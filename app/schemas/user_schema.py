from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# schema imports
from schemas.inventory_schema import InventoryOut

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserOut(UserCreate):
    id: int
    active: bool
    created_on: Optional[datetime]
    inventories: List[InventoryOut] = []

    class Config:
        orm_mode = True