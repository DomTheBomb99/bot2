import alpaca_trade_api as tradeapi
from src.data.models import MarketData
from src.core.config import settings

class AlpacaProvider:
    def __init__(self):
        self.api = tradeapi.REST(
            settings.alpaca_key,
            settings.alpaca_secret,
            settings.alpaca_endpoint
        )

    async def get_latest_bars(self, symbol: str) -> MarketData:
        try:
            bars = self.api.get_barset(symbol, '1day', limit=1).df[symbol].iloc[-1]
            return MarketData(
                symbol=symbol,
                price=float(bars.c),
                volume=int(bars.v),
                timestamp=float(bars.t)
            )
        except Exception as e:
            print(f"Data fetch error: {e}")
            return None
