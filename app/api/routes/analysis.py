from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import re

router = APIRouter()


class AnalysisRequest(BaseModel):
    text: str = Field(
        ...,
        description="Texto libre a analizar.",
        example="Aivio hace que integrar IA en mi backend sea increíblemente fácil",
    )


class AnalysisResponse(BaseModel):
    sentiment: str = Field(..., example="positive")
    confidence: float = Field(..., example=0.93)
    keywords: list[str] = Field(default_factory=list, example=["backend", "increíblemente"])
    word_count: int = Field(..., example=9)


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


@router.post(
    "/sentiment",
    response_model=AnalysisResponse,
    responses={
        400: {
            "description": "Texto vacío o solicitud inválida.",
            "content": {
                "application/json": {
                    "example": {"detail": "Text cannot be empty"}
                }
            },
        },
        422: {
            "description": "Error de validación en el cuerpo de la petición.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "text"],
                                "msg": "field required",
                                "type": "value_error.missing",
                            }
                        ]
                    }
                }
            },
        },
        500: {
            "description": "Error interno del servidor.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Internal server error. Please try again later."
                    }
                }
            },
        },
    },
)
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
