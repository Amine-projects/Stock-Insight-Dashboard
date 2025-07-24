from datetime import datetime
from app.utils.api_client import YahooFinanceClient
from app.utils.cache import cache
from app.utils.technical_indicators import calculate_rsi, calculate_moving_averages

class StockService:
    def __init__(self):
        self.yahoo_client = YahooFinanceClient()

    @cache(ttl=900)
    async def get_stock_data(self, ticker: str, period: str = "1y"):
        data = await self.yahoo_client.fetch_stock_data(ticker, period)
        
        # Calculate technical indicators
        history = data["history"]
        if not history.empty:
            data["technical_indicators"] = {
                "rsi": calculate_rsi(history['Close']),
                "moving_averages": calculate_moving_averages(history['Close'])
            }
        
        return {
            "info": data["info"],
            "history": history.reset_index().to_dict("records"),
            "technical_indicators": data.get("technical_indicators", {})
        }