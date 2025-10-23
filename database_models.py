from sqlalchemy import Column, Integer, String, Float
from database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
