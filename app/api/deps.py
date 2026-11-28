from functools import lru_cache

from fastapi import Depends, HTTPException, Security, status
from fastapi.security import APIKeyHeader

from app.core.config import Settings, get_settings
from app.services.sentiment_engine import SentimentEngine

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)


def verify_api_key(
    api_key: str | None = Security(api_key_header),
    settings: Settings = Depends(get_settings),
) -> str:
    if not api_key or api_key != settings.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
    return api_key


@lru_cache
def get_sentiment_engine() -> SentimentEngine:
    return SentimentEngine()
