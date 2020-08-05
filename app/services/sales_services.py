from sqlalchemy.orm import Session
from fastapi import HTTPException

# model imports
from models.inventories import InventoryModel
from models.sales import SaleModel
# schema imports
from schemas.sale_schema import SaleCreate

class SalesService:

    @staticmethod
    def make_sale(db: Session, inv_id: int, sale: SaleCreate):
        """Make a sale of an inventory"""
        the_inventory = db.query(InventoryModel).filter(InventoryModel.id == inv_id).first()

        if the_inventory is None:
            raise HTTPException(status_code=404, details="Inventory does not exist")

        new_sale =  SaleModel(**sale.dict())

        db.add(new_sale)
        db.commit()
        db.refresh(new_sale)
        return new_sale