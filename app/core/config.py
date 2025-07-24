from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Stock Insight API"
    ALPHA_VANTAGE_KEY: str
    FINNHUB_KEY: str
    API_RATE_LIMIT: int = 100
    CACHE_TTL: int = 900  
    
    class Config:
        env_file = ".env"

settings = Settings()