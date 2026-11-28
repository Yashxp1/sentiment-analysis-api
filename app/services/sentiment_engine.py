from schema.sentiment import SentimentLabel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentEngine:
    def __init__(self) -> None:
        self.analyzer = SentimentIntensityAnalyzer()

    def analyse(self, text: str) -> dict:
        scores = self.analyzer.polarity_scores(text)
        compound = scores["compound"]

        if compound >= 0.05:
            label = SentimentLabel.POSITIVE
            confidence = scores["pos"]
        elif compound <= -0.05:
            label = SentimentLabel.NEGATIVE
            confidence = scores["neg"]
        else:
            label = SentimentLabel.NEUTRAL
            confidence = scores["neu"]

        return {
            "text": text,
            "sentiment": label,
            "confidence": round(confidence, 2),
        }
