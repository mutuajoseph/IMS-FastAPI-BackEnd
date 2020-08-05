from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# schema imports
from schemas.stock_schema import StockCreate, StockOut

# db imports
from db.config import get_db

# service import 
from services.stock_service import StockService

router = APIRouter()

@router.post('/{inv_id}',
summary='add stock to an existing inventory ',
response_model = StockOut,
response_description = 'the new stock',
status_code = 201
)
async def add_stock(stock: StockCreate, inv_id: int, db: Session = Depends(get_db)):
    return StockService.add_stock(db=db, inv_id=inv_id, stock=stock)