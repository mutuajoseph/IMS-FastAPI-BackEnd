from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

# db imports
from db.config import get_db

# schema imports
from schemas.user_schema import UserCreate, UserOut

router = APIRouter()

@router.get('',
summary='return a list of all users',
response_model=List[UserOut],
response_description ='all users',
status_code=200
)
async def get_all_users(db : Session = Depends(get_db)):
    pass


@router.get('/{user_id}',
summary='return a single user that matches the id provided',
response_model=UserOut,
response_description ='a user',
status_code=200
)
async def get_a_single_user(user_id:int, db:Session=Depends(get_db)):
    pass

@router.post('',
summary='create a new user',
response_model=UserOut,
response_description ='the new user',
status_code=201
)
async def create_user(user: UserCreate, db: Session= Depends(get_db)):
    pass

@router.put('/{user_id}',
summary='updates a user that matches with the id provided',
response_model=UserOut,
response_description ='the user',
status_code=201
)
async def update_user(user: UserCreate, db: Session= Depends(get_db)):
    pass


@router.delete('/{user_id}',
summary='deletes a single user that matches the id provided',
response_model=UserOut,
response_description ='the user',
status_code=200
)
async def delete_user(user_id:int, db:Session=Depends(get_db)):
    pass