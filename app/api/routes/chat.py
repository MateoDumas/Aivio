from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    context: str | None = None

class ChatResponse(BaseModel):
    response: str
    intent: str
    suggested_actions: list[str]

@router.post("/", response_model=ChatResponse)
async def chat_bot(payload: ChatRequest) -> ChatResponse:
    """
    Chatbot simple capaz de responder preguntas sobre la API y asistencia general.
    Simula un asistente virtual inteligente.
    """
    msg = payload.message.lower().strip()
    
    # Base de conocimientos simple (Intents)
    if not msg:
        return ChatResponse(
            response="Hola, parece que no has escrito nada. ¿En qué puedo ayudarte?",
            intent="empty_input",
            suggested_actions=["Ver documentación", "Probar recomendaciones"]
        )

    # Saludos
    if any(w in msg for w in ["hola", "hello", "hi", "buenas", "que tal"]):
        return ChatResponse(
            response="¡Hola! Soy el asistente virtual de Aivio. Puedo ayudarte a explorar nuestra API de IA, generar recomendaciones o analizar textos. ¿Por dónde empezamos?",
            intent="greeting",
            suggested_actions=["¿Qué puedes hacer?", "Analizar sentimiento", "Recomendar productos"]
        )

    # Ayuda / Capacidades
    if any(w in msg for w in ["ayuda", "help", "hacer", "capabilities", "funciona"]):
        return ChatResponse(
            response="Soy una API backend potenciada con IA. Mis capacidades principales son:\n1. Sistema de Recomendaciones (ML con PyTorch)\n2. Análisis de Sentimiento (NLP)\n3. Autenticación segura JWT\n4. Historial persistente.",
            intent="help",
            suggested_actions=["Ver endpoints", "Probar NLP"]
        )

    # Preguntas sobre la API
    if "api" in msg or "endpoint" in msg or "docs" in msg:
        return ChatResponse(
            response="Toda nuestra documentación está disponible en /docs. Ahí puedes probar interactivamente todos los endpoints usando Swagger UI.",
            intent="documentation_query",
            suggested_actions=["Ir a /docs"]
        )

    # Preguntas sobre tecnología
    if any(w in msg for w in ["python", "fastapi", "pytorch", "stack", "tecnologia"]):
        return ChatResponse(
            response="Estoy construido sobre un stack moderno: Python 3.11+, FastAPI para el servidor, PyTorch para inferencia de ML, y PostgreSQL para persistencia de datos. ¡Rendimiento puro!",
            intent="tech_stack",
            suggested_actions=["Ver repositorio"]
        )

    # Análisis de sentimiento (redirección)
    if "sentim" in msg or "analis" in msg or "texto" in msg:
        return ChatResponse(
            response="Para análisis de texto, usa el endpoint POST /analysis/sentiment. Envíame un texto y te diré si es positivo o negativo.",
            intent="feature_nlp",
            suggested_actions=["Probar /analysis/sentiment"]
        )

    # Recomendaciones (redirección)
    if "recom" in msg or "predic" in msg:
        return ChatResponse(
            response="El motor de recomendaciones vive en /recommendations. Aprende de tus gustos. ¡Pruébalo enviando una lista de IDs de items!",
            intent="feature_recs",
            suggested_actions=["Probar /recommendations"]
        )

    # Fallback (Respuesta por defecto)
    fallback_responses = [
        "Interesante... Cuéntame más o pregúntame sobre mis funciones de IA.",
        "No estoy seguro de entender eso, pero puedo ayudarte con recomendaciones o análisis de datos.",
        "Aún estoy aprendiendo. ¿Podrías reformular eso? Intenta preguntar '¿qué puedes hacer?'"
    ]
    
    return ChatResponse(
        response=random.choice(fallback_responses),
        intent="unknown",
        suggested_actions=["Ayuda", "Ver documentación"]
    )
