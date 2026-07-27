from src.data.models import OrderRequest
from src.execution.broker_adapter import BrokerAdapter
from src.storage.redis_db import redis_manager

class OrderManager:
    def __init__(self):
        self.broker = BrokerAdapter()

    async def execute(self, order: OrderRequest):
        # Check cache for recent execution to prevent duplicates
        cache_key = f"executed:{order.symbol}:{order.action}:{order.quantity}"
        
        if redis_manager.redis:
            exists = await redis_manager.redis.exists(cache_key)
            if exists:
                print(f"Order already executed: {cache_key}")
                return

        self.broker.submit_order(order.symbol, order.quantity, order.action)
        
        if redis_manager.redis:
            await redis_manager.redis.setex(cache_key, 86400, "1")
