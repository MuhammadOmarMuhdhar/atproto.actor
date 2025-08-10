from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    ATPROTO_CLIENT_ID: str
    ATPROTO_CLIENT_SECRET: str
    STRIPE_SECRET_KEY: str
    STRIPE_PUBLISHABLE_KEY: str
    DOMAIN_REGISTRAR_API_KEY: str
    CLOUDFLARE_API_TOKEN: str
    ENVIRONMENT: str = "development"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    class Config:
        env_file = ".env"

settings = Settings()