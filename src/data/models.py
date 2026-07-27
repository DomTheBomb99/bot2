from pydantic import BaseModel
from typing import Optional

class MarketData(BaseModel):
    symbol: str
    price: float
    volume: int
    timestamp: float

class Signal(BaseModel):
    symbol: str
    signal_type: str  # LONG, SHORT, NEUTRAL
    confidence: float
    timestamp: float
    source: str

class OrderRequest(BaseModel):
    symbol: str
    action: str  # BUY, SELL
    quantity: float
    timestamp: float
