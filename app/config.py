from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str = "redis://localhost:6379"
    SECRET_KEY: str = "dev-secret-key"
    ATPROTO_CLIENT_ID: str = "placeholder"
    ATPROTO_CLIENT_SECRET: str = "placeholder"
    STRIPE_SECRET_KEY: str = "placeholder"
    STRIPE_PUBLISHABLE_KEY: str = "placeholder"
    DOMAIN_REGISTRAR_API_KEY: str = "placeholder"
    CLOUDFLARE_API_TOKEN: str = "placeholder"
    ENVIRONMENT: str = "development"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    class Config:
        env_file = ".env"

settings = Settings()