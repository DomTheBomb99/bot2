from abc import ABC, abstractmethod
from src.core.event_bus import EventBus

class BaseAgent(ABC):
    def __init__(self, bus: EventBus, name: str):
        self.bus = bus
        self.name = name
        self.bus.subscribe("all", self.on_error) # Global error handler

    @abstractmethod
    async def process(self, event_data):
        pass

    async def on_error(self, data):
        print(f"[{self.name}] Error: {data}")
