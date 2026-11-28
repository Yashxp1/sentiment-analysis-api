from fastapi import FastAPI, status
from schema.sentiment import SentimentRequest, SentimentResponse
from services.sentiment_engine import SentimentEngine

app = FastAPI(
    title="Sentiment Analysis API",
    description="An API to analyse input text",
    version="1.0.0",
)

sentiment_engine = SentimentEngine()


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy", "service": "sentiment-analysis-api"}


@app.post(
    "/analyse",
    response_model=SentimentResponse,
    status_code=status.HTTP_200_OK,
    summary="Analyses sentiment",
)
def analyse_sentiment(payload: SentimentRequest):
    return sentiment_engine.analyse(payload.text)
