from fastapi import APIRouter, Depends, status

from app.api.deps import get_sentiment_engine, verify_api_key
from app.schema.sentiment import SentimentRequest, SentimentResponse
from app.services.sentiment_engine import SentimentEngine

router = APIRouter()


@router.post(
    "/analyse",
    response_model=SentimentResponse,
    status_code=status.HTTP_200_OK,
    summary="Analyses sentiment",
    dependencies=[Depends(verify_api_key)],
)
def analyse_sentiment(
    payload: SentimentRequest,
    engine: SentimentEngine = Depends(get_sentiment_engine),
):
    return engine.analyse(payload.text)
