# app/infrastructure/configuration/dependencies.py

from app.infrastructure.open_ai.openai_client import OpenAIClient
from app.infrastructure.open_ai.sentiment_analyzer import SentimentAnalyzer
from app.infrastructure.tavily.tavily_client import TavilyClientApi
from app.infrastructure.tavily.news_fetcher import NewsFetcher
from app.application.service.sentiment_analysis_service import SentimentAnalysisService
from fastapi import Depends

def get_openai_client() -> OpenAIClient:
    return OpenAIClient()

def get_tavily_client() -> TavilyClientApi:
    return TavilyClientApi()

def get_sentiment_analyzer(openai_client: OpenAIClient = Depends(get_openai_client)) -> SentimentAnalyzer:
    return SentimentAnalyzer(openai_client)

def get_news_fetcher(tavily_client: TavilyClientApi = Depends(get_tavily_client)) -> NewsFetcher:
    return NewsFetcher(tavily_client)

def get_sentiment_analysis_service(
    sentiment_analyzer: SentimentAnalyzer = Depends(get_sentiment_analyzer),
    news_fetcher: NewsFetcher = Depends(get_news_fetcher)
) -> SentimentAnalysisService:
    return SentimentAnalysisService(sentiment_analyzer, news_fetcher)