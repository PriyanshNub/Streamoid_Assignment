## tests/test_product.py


import os
import io
import json
import pytest
from fastapi.testclient import TestClient


# Use a temporary sqlite DB for tests
os.environ["DATABASE_URL"] = "sqlite:///:memory:"


from main import app
from app.db.session import engine
from app.models.product import Base


# Create tables in the in-memory DB
Base.metadata.create_all(bind=engine)


client = TestClient(app)


CSV = """sku,name,brand,color,size,mrp,price,quantity
sku1,Product One,BrandA,Red,M,100,90,10
sku2,Product Two,BrandB,Blue,L,150,160,5
sku3,Product Three,BrandA,Green,S,200,180,3
"""




def test_upload_and_search():
    response = client.post(
    "/upload",
    files={"file": ("products.csv", CSV, "text/csv")},
    )
    assert response.status_code == 200
    data = response.json()
    # sku2 has price>mrp so should fail; others stored
    assert data["stored"] == 2
    assert isinstance(data["failed"], list)


    # List products
    r = client.get("/products?page=1&limit=10")
    assert r.status_code == 200
    listing = r.json()
    assert listing["total"] == 2


    # Search by brand
    r = client.get("/products/search?brand=BrandA")
    assert r.status_code == 200
    results = r.json()
    assert len(results) == 2


    # Search by price range (only product with price 90 should match)
    r = client.get("/products/search?minPrice=80&maxPrice=100")
    assert r.status_code == 200
    results = r.json()
    assert any(p["sku"] == "sku1" for p in results)