# app/application/service/sentiment_analysis_service.py

from app.infrastructure.open_ai.sentiment_analyzer import SentimentAnalyzer
from app.infrastructure.tavily.news_fetcher import NewsFetcher
from app.domain.model.value_expression import ValueExpression

class SentimentAnalysisService:
    def __init__(self, sentiment_analyzer: SentimentAnalyzer, news_fetcher: NewsFetcher):
        self.sentiment_analyzer = sentiment_analyzer
        self.news_fetcher = news_fetcher

    def news_and_sentimental_analyzer_exec(self, option_company_selected: str, max_results: int = 3):
        value_expression_instance = ValueExpression(content=option_company_selected)
        try:
            fetch_news = self.news_fetcher.analyze(value_expression_instance, max_results)
            concatenated_content = " ".join(item["content"] for item in fetch_news if "content" in item)
            value_expression_fetch_api = ValueExpression(content=concatenated_content)
            sentiment_analysis_result = self.sentiment_analyzer.analyze(value_expression_fetch_api)
            return fetch_news, sentiment_analysis_result
        except Exception as e:
            raise RuntimeError(f"Error in sentiment analysis execution: {str(e)}")