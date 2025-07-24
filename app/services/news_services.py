from textblob import TextBlob
import requests
from app.core.config import settings
from app.models.schemas import NewsSentimentResponse

class NewsService:
    async def get_news_sentiment(self, ticker: str) -> NewsSentimentResponse:
        # Using Finnhub API
        url = f"https://finnhub.io/api/v1/news?category=general&token={settings.FINNHUB_KEY}"
        response = requests.get(url)
        news_items = [item for item in response.json() if ticker in item.get('related', '')][:10]
        
        sentiments = []
        positive = negative = 0
        
        for item in news_items:
            analysis = TextBlob(item['headline'])
            polarity = analysis.sentiment.polarity
            sentiments.append(polarity)
            if polarity > 0.1:
                positive += 1
            elif polarity < -0.1:
                negative += 1
                
        avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
        
        return NewsSentimentResponse(
            average_sentiment=avg_sentiment,
            classification="Positive" if avg_sentiment > 0.1 else 
                          "Negative" if avg_sentiment < -0.1 else "Neutral",
            positive_articles=positive,
            negative_articles=negative
        )