from fastapi import APIRouter, Depends, HTTPException
from fastapi_limiter.depends import RateLimiter
from typing import Optional
from app.services import (
    stock_service,
    news_service,
    valuation_service
)
from app.models.schemas import (
    StockQuery,
    ValuationInput,
    NewsSentimentResponse
)

router = APIRouter()

@router.get("/stocks/{ticker}", 
           dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def get_stock_data(
    ticker: str,
    query: StockQuery = Depends()
):
    try:
        stock_data = await stock_service.get_stock_data(ticker, query.period)
        
        if query.include_news:
            news_data = await news_service.get_news_sentiment(ticker)
            stock_data["news"] = news_data
            
        if query.include_valuation:
            valuation_data = await valuation_service.dcf_valuation(ticker)
            stock_data["valuation"] = valuation_data
            
        return {
            "data": stock_data,
            "meta": {
                "symbol": ticker,
                "period": query.period
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/valuation/dcf", response_model=ValuationInput)
async def perform_dcf_valuation(
    input_data: ValuationInput
):
    try:
        result = await valuation_service.dcf_valuation(
            input_data.ticker,
            input_data.growth_rate,
            input_data.discount_rate,
            input_data.terminal_growth,
            input_data.years
        )
        return {"data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))