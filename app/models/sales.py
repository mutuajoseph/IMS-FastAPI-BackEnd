from db.config import Base
from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func

class SaleModel(Base):
    __tablename__ = 'sales'
    id =Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    created_on = Column(DateTime(timezone=True), default=func.now(), nullable=True)
    inv_id =Column(Integer, ForeignKey('inventories.id'))
    inventory = relationship('InventoryModel', back_populates='sales')