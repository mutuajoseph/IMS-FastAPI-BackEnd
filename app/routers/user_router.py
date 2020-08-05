from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

# db imports
from db.config import get_db

# schema imports
from schemas.user_schema import UserCreate, UserOut

# services imports
from services.user_service import UserService


router = APIRouter()

@router.get('',
summary='return a list of all users',
response_model=List[UserOut],
response_description ='all users',
status_code=200
)
async def get_all_users(db : Session = Depends(get_db)):
    return UserService.get_all_users(db=db)


@router.get('/{user_id}',
summary='return a single user that matches the id provided',
response_model=UserOut,
response_description ='a user',
status_code=200
)
async def get_a_single_user(user_id:int, db:Session=Depends(get_db)):
    return UserService.get_a_single_user(user_id=user_id, db=db)

@router.post('',
summary='create a new user',
response_model=UserOut,
response_description ='the new user',
status_code=201
)
async def create_user(user: UserCreate, db: Session= Depends(get_db)):
    return UserService.create_a_new_user(user=user, db=db)

@router.put('/{user_id}',
summary='updates a user that matches with the id provided',
response_model=UserOut,
response_description ='the user',
status_code=201
)
async def update_user(user_id: int, payload: UserCreate, db: Session= Depends(get_db)):
    return UserService.update_user(db=db, user_id=user_id, payload=payload)


@router.delete('/{user_id}',
summary='deletes a single user that matches the id provided',
response_description ='the user',
status_code=200
)
async def delete_user(user_id:int, db:Session=Depends(get_db)):
    return UserService.delete_user(db=db, user_id=user_id)
