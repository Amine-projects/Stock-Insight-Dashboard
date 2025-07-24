from pydantic import BaseModel
from typing import Optional

class StockQuery(BaseModel):
    period: str = "1y"
    include_news: bool = False
    include_valuation: bool = False

class ValuationInput(BaseModel):
    ticker: str
    growth_rate: float = 0.05
    discount_rate: float = 0.1
    terminal_growth: float = 0.02
    years: int = 5

class StockDataResponse(BaseModel):
    symbol: str
    current_price: float
    moving_averages: dict
    rsi: Optional[float]

class NewsSentimentResponse(BaseModel):
    average_sentiment: float
    classification: str
    positive_articles: int
    negative_articles: int