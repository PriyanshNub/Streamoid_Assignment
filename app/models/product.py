



from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    sku = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    brand = Column(String)
    color = Column(String)
    size = Column(String)
    mrp = Column(Float)
    price = Column(Float)
    quantity = Column(Integer)


