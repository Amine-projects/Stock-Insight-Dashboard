import yfinance as yf
import requests
from typing import Dict, Any
from app.core.config import settings

class YahooFinanceClient:
    async def fetch_stock_data(self, ticker: str, period: str) -> Dict[str, Any]:
        stock = yf.Ticker(ticker)
        return {
            "info": stock.info,
            "history": stock.history(period=period)
        }

class AlphaVantageClient:
    def __init__(self):
        self.base_url = "https://www.alphavantage.co/query"
        self.api_key = settings.ALPHA_VANTAGE_KEY

    async def get_technical_indicators(self, ticker: str):
        params = {
            "function": "RSI",
            "symbol": ticker,
            "interval": "daily",
            "time_period": "14",
            "series_type": "close",
            "apikey": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        return response.json()