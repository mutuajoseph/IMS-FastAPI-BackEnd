from fastapi import FastAPI


# database imports
from db.config import Base, engine, get_db

# models imports
from models.users import UserModel
from models.inventories import InventoryModel
from models.sales import SaleModel
from models.stocks import StockModel

# create the tables
Base.metadata.create_all(bind=engine)

#import the routers
from routers import inventory_router, user_router, auth_router

app = FastAPI(
    title="Inventory Management System API",
    description="Simple IMS API ",
    version="1.0.0"
)


@app.get('/')
def home():
    return{"message":"Inventory Management API"}

app.include_router(
    auth_router.router,
    prefix='/auth',
    tags=['Auth Operations'],
    responses={200:{'description':'Ok'}, 
               201:{'description':'Created'}, 400:{'description':'Bad Request'},
               401:{'description':'Unauthorized'}}
)

app.include_router(
    user_router.router,
    prefix='/users',
    tags=['User Operations'],
    responses={200:{'description':'Ok'}, 
               201:{'description':'Created'}, 400:{'description':'Bad Request'},
               401:{'description':'Unauthorized'}}
)

app.include_router(
    inventory_router.router,
    prefix='/inventories',
    tags=['Inventory Operations'],
    responses={200:{'description':'Ok'}, 
               201:{'description':'Created'}, 400:{'description':'Bad Request'},
               401:{'description':'Unauthorized'}}
)