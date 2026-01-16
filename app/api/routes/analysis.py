from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import re

router = APIRouter()


class AnalysisRequest(BaseModel):
    text: str


class AnalysisResponse(BaseModel):
    sentiment: str
    confidence: float
    keywords: list[str]
    word_count: int


def simple_sentiment_analysis(text: str) -> tuple[str, float]:
    """
    Análisis de sentimiento heurístico simple para demostración sin dependencias pesadas.
    En producción, usaríamos modelos Transformer (BERT/RoBERTa) vía PyTorch.
    """
    positive_words = {
        "good", "great", "excellent", "amazing", "love", "like", "best", "perfect", 
        "happy", "wonderful", "cool", "nice", "awesome", "bueno", "bien", "excelente", 
        "genial", "amor", "gusta", "mejor", "perfecto", "feliz"
    }
    negative_words = {
        "bad", "terrible", "awful", "worst", "hate", "dislike", "poor", "sad", "angry", 
        "boring", "useless", "malo", "terrible", "peor", "odio", "triste", "enojado", 
        "aburrido", "inutil", "feo"
    }
    
    words = re.findall(r'\w+', text.lower())
    if not words:
        return "neutral", 0.0
        
    pos_count = sum(1 for w in words if w in positive_words)
    neg_count = sum(1 for w in words if w in negative_words)
    
    total_emotional_words = pos_count + neg_count
    
    if total_emotional_words == 0:
        return "neutral", 0.5
        
    if pos_count > neg_count:
        confidence = 0.5 + (pos_count / (len(words) + 1))
        return "positive", min(confidence, 0.99)
    elif neg_count > pos_count:
        confidence = 0.5 + (neg_count / (len(words) + 1))
        return "negative", min(confidence, 0.99)
    else:
        return "neutral", 0.5


@router.post("/sentiment", response_model=AnalysisResponse)
async def analyze_sentiment(payload: AnalysisRequest) -> AnalysisResponse:
    """
    Analiza el sentimiento de un texto dado.
    Demuestra procesamiento de texto básico (NLP).
    """
    if not payload.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
        
    sentiment, confidence = simple_sentiment_analysis(payload.text)
    
    # Extracción simple de keywords (palabras largas)
    words = re.findall(r'\w+', payload.text.lower())
    keywords = list(set([w for w in words if len(w) > 5]))[:5]
    
    return AnalysisResponse(
        sentiment=sentiment,
        confidence=confidence,
        keywords=keywords,
        word_count=len(words)
    )
