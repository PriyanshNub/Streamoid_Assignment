from fastapi import FastAPI
from app.api.v1 import product as product_router
from app.core.config import settings


app = FastAPI(title=settings.APP_NAME)


app.include_router(product_router.router, prefix="", tags=["products"])


@app.get("/")
def root():
    return {"msg": "FastAPI Product API - alive"}