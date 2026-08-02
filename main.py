from contextlib import asynccontextmanager
from fastapi import FastAPI

try:
    from src.storage.redis_db import redis_manager
except Exception:
    redis_manager = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.core.logger import setup_logger

logger = setup_logger("Main")

    if redis_manager:
        try:
            await redis_manager.connect()
            logger.info("Redis connected.")
        except Exception as e:
            logger.warning(f"Redis unavailable: {e}")
    logger.info("Starting Trading Bot...")
    

    yield

    logger.info("Trading Bot shutting down.")


app = FastAPI(
    title="AI Trading Bot",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "AI Trading Bot"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
