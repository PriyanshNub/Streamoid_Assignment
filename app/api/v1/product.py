from sqlalchemy.orm import Session
from app.db.session import get_db, engine
from app.models.product import Base as ProductBase
from app.schemas.product import ProductRead
from app.utils.csv_loader import parse_and_validate_csv
from app.crud.product import create_product, get_products, count_products, search_products
from fastapi import File, UploadFile, Depends
from fastapi import APIRouter, HTTPException, Query
from typing import List
import io
import pandas as pd




router = APIRouter()


ProductBase.metadata.create_all(bind=engine)




@router.post("/upload")
async def upload_products(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if file.content_type not in ("text/csv", "application/vnd.ms-excel"):
        raise HTTPException(status_code=400, detail="CSV file required")

    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    required_columns = {"SKU", "Name", "Brand", "Color", "Size", "MRP", "Price", "Quantity"}
    missing_cols = required_columns - set(df.columns)
    if missing_cols:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required columns: {', '.join(missing_cols)}"
        )

    stored, failed = 0, []

    for _, row in df.iterrows():
        try:
            product_data = {
                "sku": str(row["SKU"]).strip(),
                "name": str(row["Name"]).strip(),
                "brand": str(row["Brand"]).strip(),
                "color": str(row["Color"]).strip(),
                "size": str(row["Size"]).strip(),
                "mrp": float(row["MRP"]),
                "price": float(row["Price"]),
                "quantity": int(row["Quantity"])
            }


            create_product(db, product_data)
            stored += 1

        except Exception as e:
            failed.append({"row": row.to_dict(), "reason": str(e)})

    return {"stored": stored, "failed": failed}





@router.get("/products", response_model=dict)
def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
    ):
    skip = (page - 1) * limit
    products = get_products(db, skip=skip, limit=limit)
    total = count_products(db)

    results = [ProductRead.from_orm(p).dict() for p in products]
    return {"total": total, "page": page, "limit": limit, "products": results}




@router.get("/products/search", response_model=List[ProductRead])
def search(
    brand: str = Query(None),
    color: str = Query(None),
    minPrice: float = Query(None, alias="minPrice"),
    maxPrice: float = Query(None, alias="maxPrice"),
    db: Session = Depends(get_db),
    ):
    results = search_products(db, brand=brand, color=color, min_price=minPrice, max_price=maxPrice)

    return [ProductRead.from_orm(p) for p in results]
