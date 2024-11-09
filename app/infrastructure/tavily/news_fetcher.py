# app/infrastructure/tavily/news_fetcher.py

from app.domain.model.value_expression import ValueExpression
from app.infrastructure.tavily.tavily_client import TavilyClientApi

class NewsFetcher:
    def __init__(self, tavily_client: TavilyClientApi):
        self.tavily_client = tavily_client

    def analyze(self, expression: ValueExpression, max_results: int = 3):
        prompt = (
            f"Provide a detailed analysis of systemic risks associated with {expression.content}. "
            f"Focus on how this company influences market indices like the Bloomberg 500 or S&P 500, "
            f"and include significant statistics regarding its performance this year."
        )
        return self.tavily_client.get_info_company(prompt, max_results)