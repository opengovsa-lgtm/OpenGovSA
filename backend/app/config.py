from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/opengovsa"

settings = Settings()
