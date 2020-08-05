from fastapi import HTTPException
from sqlalchemy.orm import Session

#  models imports
from models.stocks import StockModel
from models.inventories import InventoryModel

# schema imports
from schemas.stock_schema import StockCreate

class StockService:
 
    @staticmethod
    def add_stock(db: Session, inv_id:int, stock: StockCreate):
        """Adds stock to an inventory"""
        the_inventory = db.query(InventoryModel).filter(InventoryModel.id == inv_id).first()

        if the_inventory is None:
            raise HTTPException(status_code=404, details="Inventory does not exist")

        new_stock = StockModel(**stock.dict())
        db.add(new_stock)
        db.commit()
        db.refresh(new_stock)

        return new_stock
