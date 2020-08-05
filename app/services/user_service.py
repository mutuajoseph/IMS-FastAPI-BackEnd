from sqlalchemy.orm import Session
from fastapi import HTTPException

# import the hashing class
from passlib.context import CryptContext

# import the schemas
from schemas.user_schema import UserCreate

# import the models
from models.users import UserModel


# hashing instance(object)
pwd_context = CryptContext(schemes=['bcrypt'])

class UserService:

    @staticmethod
    def get_all_users(db: Session):
        """return a list of all users"""
        return db.query(UserModel).all()


    @staticmethod
    def get_a_single_user(user_id:int ,db: Session):
        """returns a user that matches the id"""
        user = db.query(UserModel).filter(UserModel.id==user_id).first()

        if user is None:
            raise HTTPException(status_code=404, detail="User does not exist!")
        return user

    @staticmethod
    def create_a_new_user(user: UserCreate, db: Session):
        """returns a new user"""
        the_user = db.query(UserModel).filter(UserModel.email==user.email).first()

        if the_user:
            raise HTTPException(status_code=400, detail="User already exists!")
        else:
            new_user = UserModel(username = user.username, email = user.email, password = pwd_context.hash(user.password))
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user

    @staticmethod
    def update_user(db: Session, user_id:int, payload: UserCreate):
        """Updates a user that matches the id provided"""
        the_user = db.query(UserModel).filter(UserModel.id==user_id).first()

        if the_user is None:
            raise HTTPException(status_code=404, detail="User does not exist!")
        
        the_user.username = payload.username
        the_user.email = payload.email

        db.commit()
        return the_user


    @staticmethod
    def delete_user(db: Session, user_id:int):
        """Deletes a user that matches the id provided"""
        the_user = db.query(UserModel).filter(UserModel.id==user_id).first()

        if the_user is None:
            raise HTTPException(status_code=404, detail="User does not exist!")

        db.delete(the_user)
        db.commit()

        return {"message" : "User successfully deleted"}

