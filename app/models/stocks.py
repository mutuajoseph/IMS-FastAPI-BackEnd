from db.config import Base
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import  func

class StockModel(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    stock = Column(Integer, nullable=False)
    created_on = Column(DateTime(timezone=True), default=func.now(), nullable=True)
    inv_id = Column(Integer, ForeignKey('inventories.id'))
    inventory= relationship('InventoryModel', back_populates='stocks')