# app/main.py

from fastapi import FastAPI, Request
from app.infrastructure.rest.controllers.sentiment_analysis_controller import router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from datetime import date

app = FastAPI(
    title="sentiment-news-analysis-api",
    description="Esta API permite realizar análisis de sentimiento a partir de las noticias sobre un ticker.",
    version="1.0.0"
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(content={"timestamp": date.today().isoformat(), "messages": [error['msg'] for error in exc.errors()]}, status_code=400)

app.include_router(router, prefix="/news", tags=["Endpoints sobre el análisis de sentimiento de noticias"])
