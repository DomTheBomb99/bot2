import alpaca_trade_api as tradeapi
from src.core.config import settings

class BrokerAdapter:
    def __init__(self):
        self.api = tradeapi.REST(
            settings.alpaca_key,
            settings.alpaca_secret,
            settings.alpaca_endpoint
        )

    def submit_order(self, symbol: str, qty: float, side: str):
        try:
            self.api.submit_order(symbol, qty, side, 'market', 'day')
            print(f"Order submitted: {side} {qty} {symbol}")
        except Exception as e:
            print(f"Order failed: {e}")
