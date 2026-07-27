from contextlib import asynccontextmanager
from fastapi import FastAPI

try:
    from src.storage.redis_db import redis_manager
except Exception:
    redis_manager = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Trading Bot...")

    if redis_manager:
        try:
            await redis_manager.connect()
            print("Redis connected.")
        except Exception as e:
            print(f"Redis unavailable: {e}")

    yield

    print("Trading Bot shutting down.")


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
