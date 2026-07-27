import pandas as pd
from src.agents.base_agent import BaseAgent
from src.data.models import MarketData, Signal
from src.core.event_bus import EventBus

class TechnicalAgent(BaseAgent):
    async def process(self, event_data):
        if not isinstance(event_data, MarketData):
            return

        # Simple heuristic: RSI-like logic based on price change
        # In production, fetch more history and calculate RSI
        price_change = (event_data.price - 100.0) / 100.0 # Placeholder logic
        confidence = min(abs(price_change), 1.0)

        if confidence > 0.05:
            signal_type = "LONG" if price_change > 0 else "SHORT"
            signal = Signal(
                symbol=event_data.symbol,
                signal_type=signal_type,
                confidence=confidence,
                timestamp=event_data.timestamp,
                source="Technical"
            )
            await self.bus.publish("signal_generated", signal.dict())
