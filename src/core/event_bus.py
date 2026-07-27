import json
import asyncio
from typing import Callable, Dict, Any
from src.core.config import settings

class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, list] = {}
        self.queue = asyncio.Queue()
        self.running = False

    async def publish(self, event_type: str, payload: Dict[str, Any]):
        message = {
            "type": event_type,
            "payload": payload,
            "timestamp": asyncio.get_event_loop().time()
        }
        await self.queue.put(message)

    async def subscribe(self, event_type: str, callback: Callable):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    async def _start_listener(self):
        self.running = True
        while self.running:
            msg = await self.queue.get()
            if msg["type"] in self.subscribers:
                for callback in self.subscribers[msg["type"]]:
                    try:
                        await callback(msg["payload"])
                    except Exception as e:
                        print(f"Error in subscriber {callback.__name__}: {e}")
            self.queue.task_done()

    def start(self):
        asyncio.create_task(self._start_listener())

    def stop(self):
        self.running = False
