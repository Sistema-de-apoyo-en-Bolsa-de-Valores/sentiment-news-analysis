from fastapi import FastAPI, Depends

from src.application.new_analyzer import NewAnalyzer
from src.domain.models import ValueExpression
from src.application.sentiment_analyzer import SentimentAnalyzer
from src.infrastructure.openai_client import OpenAIClient
from src.infrastructure.tavily_client import TavilyClientApi

app = FastAPI()


def get_sentiment_analyzer():
    openai_client = OpenAIClient()
    return SentimentAnalyzer(openai_client)


def get_new_analyzer():
    openai_client = TavilyClientApi()
    return NewAnalyzer(openai_client)


@app.post("/sentimental-analyst/")
async def analyze_sentiment(
        expression: ValueExpression,
        analyzer: SentimentAnalyzer = Depends(get_sentiment_analyzer)
):
    result = await analyzer.analyze(expression)
    return {"message": result}


@app.post("/new-analyst/")
async def analyze_sentiment(
        expression: ValueExpression,
        analyzer: NewAnalyzer = Depends(get_new_analyzer)
):
    result = await analyzer.analyze(expression)
    return result
