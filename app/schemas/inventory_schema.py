from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# import the schemas
from schemas.stock_schema import StockOut
from schemas.sale_schema import SaleOut


class InventoryBase(BaseModel):
    name: str
    inv_type: str
    buying_price: float
    selling_price: float

class InventoryCreate(InventoryBase):
    pass

class InventoryOut(InventoryCreate):
    id: int
    created_on: Optional[datetime]
    stocks: List[StockOut] = []
    sales: List[SaleOut] = []

    class Config:
        orm_mode = True