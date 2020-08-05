from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# schema imports
from schemas.sale_schema import SaleCreate, SaleOut

# db imports
from db.config import get_db

# services imports
from services.sales_services import SalesService

router = APIRouter()

@router.post('/{inv_id}',
summary='make sale to an inventory ',
response_model = SaleOut,
response_description = 'the new sale',
status_code = 201
)
async def make_sale(sale: SaleCreate, inv_id: int, db: Session = Depends(get_db)):
    return SalesService.make_sale(db=db, inv_id=inv_id, sale=sale)
