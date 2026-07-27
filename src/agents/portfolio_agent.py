from src.agents.base_agent import BaseAgent
from src.data.models import Signal, OrderRequest
from src.core.event_bus import EventBus

class PortfolioAgent(BaseAgent):
    def __init__(self, bus: EventBus):
        super().__init__(bus, "PortfolioAgent")
        self.bus.subscribe("signal_generated", self.on_signal)

    async def on_signal(self, signal_data: dict):
        signal = Signal(**signal_data)
        
        # Simple position sizing: 10% of portfolio
        quantity = 10.0 
        
        order = OrderRequest(
            symbol=signal.symbol,
            action=signal.signal_type,
            quantity=quantity,
            timestamp=signal.timestamp
        )
        
        await self.bus.publish("order_request", order.dict())
