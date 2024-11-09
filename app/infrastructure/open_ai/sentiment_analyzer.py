# app/infrastructure/open_ai/sentiment_analyzer.py

from app.domain.model.value_expression import ValueExpression
from app.infrastructure.open_ai.openai_client import OpenAIClient

class SentimentAnalyzer:
    def __init__(self, openai_client: OpenAIClient):
        self.openai_client = openai_client

    def analyze(self, expression: ValueExpression) -> str:
        prompt = (
            f"You receive multiple titles of news. "
            f"Make a sentiment analysis of the following titles: {expression.content}. "
            f"Only respond with 'POSITIVE' or 'NEGATIVE'."
        )
        return self.openai_client.get_sentiment(prompt)