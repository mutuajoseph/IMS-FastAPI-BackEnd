from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StockBase(BaseModel):
    stock: int
    inv_id: int

class StockCreate(StockBase):
    pass

class StockOut(StockCreate):
    id: int
    created_on: Optional[datetime]

    class Config:
        orm_mode = True

