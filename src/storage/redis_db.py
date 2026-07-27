import asyncio
import redis.asyncio as aioredis
from src.core.config import settings

class RedisManager:
    def __init__(self):
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(settings.redis_url)

    async def set_market_data(self, symbol: str, data: dict):
        if self.redis:
            await self.redis.setex(f"market:{symbol}", 3600, str(data))

    async def get_market_data(self, symbol: str):
        if self.redis:
            data = await self.redis.get(f"market:{symbol}")
            return eval(data) if data else None

redis_manager = RedisManager()
