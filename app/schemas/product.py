## app/schemas/product.py



from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    sku: str
    name: str
    brand: str
    color: Optional[str] = None
    size: Optional[str] = None
    mrp: float
    price: float
    quantity: int


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    class Config:
        orm_mode = True