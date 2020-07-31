from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SaleBase(BaseModel):
    quantity: int
    inv_id: int

class SaleCreate(SaleBase):
    pass

class SaleOut(SaleCreate):
    id: int
    created_on: Optional[datetime]
