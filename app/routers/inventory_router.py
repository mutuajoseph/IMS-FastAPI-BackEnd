from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

# db imports
from db.config import get_db

# import schemas
from schemas.inventory_schema import InventoryCreate, InventoryOut

router = APIRouter()

@router.get('',
summary='return a list of all inventories',
response_model = List[InventoryOut],
response_description = 'all inventories',
status_code = 200
)
async def get_all_inventories(db: Session = Depends(get_db)):
    pass


@router.get('/{inv_id}',
summary='return an inventory that matches the given id',
response_model = InventoryOut,
response_description = 'the inventory',
status_code = 200
)
async def get_a_single_inventory(inv_id: int, db: Session = Depends(get_db)):
    pass


@router.post('',
summary='creates a new inventory ',
response_model = InventoryOut,
response_description = 'the new inventory',
status_code = 201
)
async def create_a_new_inventory(inventory: InventoryCreate, db: Session = Depends(get_db)):
    pass

@router.put('/{inv_id}',
summary='updates an inventory that matches the given id',
response_model = InventoryOut,
response_description = 'the inventory',
status_code = 200
)
async def update_inventory(inv_id: int, inventory: InventoryCreate, db: Session = Depends(get_db)):
    pass

@router.delete('/{inv_id}',
summary='deletes an inventory that matches the given id',
response_model = InventoryOut,
response_description = 'the inventory',
status_code = 200
)
async def delete_inventory(inv_id: int, db: Session = Depends(get_db)):
    pass