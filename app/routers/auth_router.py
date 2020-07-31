from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import timedelta, datetime
from jose import JWTError, jwt
from db.config import get_db


# models imports
from models.users import UserModel

pwd_context = CryptContext(schemes=['bcrypt'])

router = APIRouter()

# setups for JWT
SECRET_KEY = 'SOME-SECRET-KEY'
ALGORITHM = 'H256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# setup the security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth')

# auth basemodel
class Token(BaseModel):
    access_token: str
    token_type: str



# CREATE THE DEPENDENCIES TO HANDLE AUTHORIZATION


# verify user
def check_password_hash(password, hashed_passed):
    return pwd_context.verify(password, hashed_passed)

# authenticate user
def authenticate_user(db:Session,username:str, password:str):
    user = db.query(UserModel).filter(UserModel.username==username).first()
    if not user:
        return False
    if not check_password_hash(password=password, hashed_passed=user.password):
        return False
    return user

# create access token
def create_access_token(identity:dict, expires_delta: Optional[timedelta] = None):
    """setup expiry for your tokens"""
    new_identity = identity.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        """default expiry time will be 15 minutes"""
        expire = datetime.utcnow() + timedelta(minutes=15)

    # update the empty dict
    new_identity.update({'exp':expire})

    # encode the token
    encoded_jwt = jwt.encode(claims=new_identity, key=SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


# get current user
async def get_identity(token: str = Depends(oauth2_scheme)):
    exception = HTTPException(
        status_code=401,
        detail='invalid credentials',
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        # decode the token
        payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=ALGORITHM)
        identity:str  = payload.get('sub')
        if identity is None:
            raise exception
    except JWTError:
        raise exception


    return identity

@router.post('', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session= Depends(get_db)):
    user = authenticate_user(db=db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(identity={'sub': user.id}, expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer"}

