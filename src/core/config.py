from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    alpaca_key: str
    alpaca_secret: str
    alpaca_endpoint: str
    postgres_url: str
    redis_url: str
    log_level: str = "INFO"
    assets: List[str] = ["SPY", "QQQ"]

    class Config:
        env_file = ".env"

settings = Settings()
