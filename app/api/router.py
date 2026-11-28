from fastapi import APIRouter

from app.api.endpoints import health, sentiment

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(sentiment.router, tags=["Sentiment"])
