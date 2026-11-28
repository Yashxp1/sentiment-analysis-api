from enum import Enum

from pydantic import BaseModel, Field


class SentimentLabel(str, Enum):
    POSITIVE = ("POSITIVE",)
    NEGATIVE = ("NEGATIVE",)
    NEUTRAL = ("NEUTRAL",)


class SentimentRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="The text to be analyzed for sentiment.",
        json_schema_extra={"example": "FastAPI with Python is surprisingly clean!"},
    )


class SentimentResponse(BaseModel):
    text: str = Field(..., description="The original text analysed.")
    sentiment: SentimentLabel = Field(..., description="Detected sentiment category")
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score between 0.0 and 1.0.",
        json_schema_extra={"example": 0.98},
    )
