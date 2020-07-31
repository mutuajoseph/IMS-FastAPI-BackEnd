from db.config import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy import func


class InventoryModel(Base):
    __tablename__ = 'inventories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    buying_price = Column(Float, nullable=False)
    selling_price = Column(Float, nullable=False)
    inv_type = Column(String, nullable=False)
    created_on = Column(DateTime(timezone=True), default=func.now(), nullable=True)
    stocks = relationship('StockModel', back_populates='inventory')
    sales = relationship('SaleModel', back_populates='inventory')
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('UserModel', back_populates='inventories')