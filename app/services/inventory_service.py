from sqlalchemy.orm import Session
from fastapi import HTTPException

# import the model
from models.inventories import InventoryModel

# import the schema
from schemas.inventory_schema import InventoryCreate

class InventoryService:

    @staticmethod
    def get_all_inventories(db: Session):
        return db.query(InventoryModel).all()

    @staticmethod
    def get_a_single_inventory(inv_id: int, db: Session):
        inventory = db.query(InventoryModel).filter(InventoryModel.id == inv_id).first()

        if inventory is None:
            raise HTTPException(status_code=404, details="Inventory does not exist")

        return inventory

    @staticmethod
    def create_a_new_inventory(inventory: InventoryCreate, db: Session):
        the_inventory = db.query(InventoryModel).filter(InventoryModel.name == inventory.name).first()

        if the_inventory:
            raise HTTPException(status_code=400, details="Inventory already exists")

        record = InventoryModel(**inventory.dict())
        db.add(record)
        db.commit()
        db.refresh(record)

        return record

    @staticmethod
    def update_inventory(db: Session, inv_id: int, inventory: InventoryCreate):
        """updates an existing inventory"""
        the_inventory = db.query(InventoryModel).filter(InventoryModel.id == inv_id).first()

        if the_inventory is None:
            raise HTTPException(status_code=404, details="Inventory does not exist")

        the_inventory.name = inventory.name
        the_inventory.buying_price = inventory.buying_price
        the_inventory.selling_price = inventory.selling_price
        the_inventory.inv_type = inventory.inv_type

        db.commit()
        return the_inventory

    @staticmethod
    def delete_inventory(db: Session, inv_id: int):
        """deletes an existing inventory"""
        inventory = db.query(InventoryModel).filter(InventoryModel.id == inv_id).first()

        if inventory is None:
            raise HTTPException(status_code=404, detail="Inventory does not exist")

        db.delete(inventory)
        db.commit()
        return {"message" : "Inventory successfully deleted"}