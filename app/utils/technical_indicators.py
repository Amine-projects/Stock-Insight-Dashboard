import pandas as pd

def calculate_rsi(prices: pd.Series, window: int = 14) -> float:
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1] if not rsi.empty else None

def calculate_moving_averages(prices: pd.Series) -> dict:
    return {
        "sma_50": prices.rolling(50).mean().iloc[-1],
        "sma_200": prices.rolling(200).mean().iloc[-1]
    }