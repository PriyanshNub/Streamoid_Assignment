## app/crud/product.py



from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.product import Product




def create_product(db: Session, product_in: dict) -> Product:
    product = Product(**product_in)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product




def get_products(db: Session, skip: int = 0, limit: int = 100) -> List[Product]:
    return db.query(Product).offset(skip).limit(limit).all()




def count_products(db: Session) -> int:
    return db.query(Product).count()




def search_products(
db: Session,
brand: Optional[str] = None,
color: Optional[str] = None,
min_price: Optional[float] = None,
max_price: Optional[float] = None,
) -> List[Product]:
    q = db.query(Product)
    if brand:
        q = q.filter(Product.brand.ilike(f"%{brand}%"))
    if color:
        q = q.filter(Product.color.ilike(f"%{color}%"))
    if min_price is not None:
        q = q.filter(Product.price >= min_price)
    if max_price is not None:
        q = q.filter(Product.price <= max_price)
    return q.all()
