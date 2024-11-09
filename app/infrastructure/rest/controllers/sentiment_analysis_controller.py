# app/infrastructure/rest/controllers/sentiment_analysis_controller.py

from fastapi import APIRouter, Depends, Query
from app.infrastructure.configuration.dependencies import get_sentiment_analysis_service
from app.application.service.sentiment_analysis_service import SentimentAnalysisService
from fastapi.responses import JSONResponse
from datetime import date

router = APIRouter()

@router.post("/analyze")
async def analyze_sentiment(
    ticker: str = Query(..., title="Símbolo de Acción", description="Ticker del cual se van a obtener noticias y realizar análisis de sentimiento."),
    max_results: int = Query(3, title="Máximo de Resultados", description="Número máximo de noticias a recuperar.", ge=1),
    analyzer: SentimentAnalysisService = Depends(get_sentiment_analysis_service)
):
    try:
        fetch_news, sentiment_analysis_result = analyzer.news_and_sentimental_analyzer_exec(ticker, max_results)
        return JSONResponse(content={"news": fetch_news, "result": sentiment_analysis_result}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"timestamp": date.today().isoformat(), "messages": [str(e)]}, status_code=500)
