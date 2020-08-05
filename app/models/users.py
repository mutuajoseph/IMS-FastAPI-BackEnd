from db.config import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import func

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password =  Column(String, nullable=False)
    created_on = Column(DateTime(timezone=True), default=func.now(), nullable=True)
    active = Column(Boolean, default=True)
    inventories = relationship('InventoryModel', back_populates='owner')
