from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/products_db"
    # For local non-docker runs you can override this with an env var
    APP_NAME: str = "FastAPI Product API"


class Config:
    env_file = ".env"


settings = Settings()