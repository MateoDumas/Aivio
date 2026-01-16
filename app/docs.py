
# Metadata para la documentación de la API
tags_metadata = [
    {
        "name": "auth",
        "description": "🔐 **Autenticación y Seguridad**. Manejo de usuarios, registro, login y tokens JWT.",
    },
    {
        "name": "recommendations",
        "description": "🤖 **Motor de Recomendaciones ML**. Inferencia de modelos PyTorch para sugerir items y registro de feedback.",
    },
    {
        "name": "analysis",
        "description": "🧠 **Análisis Cognitivo (NLP)**. Procesamiento de lenguaje natural para detección de sentimientos.",
    },
    {
        "name": "chat",
        "description": "💬 **Chatbot Inteligente**. Asistente virtual capaz de responder preguntas sobre la API y el sistema.",
    },
]

# Descripción detallada (Markdown soportado)
description = """
<div style="text-align: center; padding: 20px;">
    <h1 style="color: #8b5cf6; font-weight: bold; font-size: 2.5rem; margin-bottom: 10px;">🧠 Aivio API</h1>
    <p style="font-size: 1.2rem; color: #d1d5db;">Intelligent Backend for Modern AI Applications</p>
</div>

Bienvenido a la documentación interactiva de **Aivio**. Este backend integra Inteligencia Artificial y Machine Learning directamente en el flujo de trabajo de tu aplicación.

## ✨ Características Principales

* **Autenticación Segura**: OAuth2 con Password Flow y JWT.
* **Machine Learning**: Modelos de PyTorch sirviendo predicciones en tiempo real.
* **NLP Analysis**: Procesamiento de texto para análisis de sentimiento.
* **High Performance**: Construido sobre **FastAPI** (ASGI) y **PostgreSQL Async**.

---

💡 **Tip:** Usa el botón **Authorize** con tus credenciales para probar los endpoints protegidos.
"""

# Custom CSS para tema "Violet/Dark Modern" (Evitando el Azul/Negro repetitivo)
custom_css = """
/* Modern Violet Dark Theme */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

body {
    background-color: #111111; /* Pure Dark Grey */
    color: #e5e5e5;
    font-family: 'Inter', sans-serif;
}

/* Topbar */
.swagger-ui .topbar {
    background-color: #111111;
    border-bottom: 1px solid #2d2d2d;
}
.swagger-ui .topbar a {
    display: none; /* Hide default logo */
}

/* Info Section */
.swagger-ui .info .title {
    color: #a78bfa !important; /* Soft Violet */
    font-family: 'Inter', sans-serif;
}
.swagger-ui .info p, .swagger-ui .info li {
    color: #d4d4d4;
}

/* Operations / Endpoints */
.swagger-ui .opblock {
    border-radius: 8px;
    box-shadow: none;
    border: none;
    margin-bottom: 15px;
}

/* GET Method */
.swagger-ui .opblock.opblock-get {
    background: rgba(16, 185, 129, 0.1); /* Emerald Tint */
    border-left: 4px solid #10b981; /* Emerald */
}
.swagger-ui .opblock.opblock-get .opblock-summary {
    border-color: #10b981;
}
.swagger-ui .opblock.opblock-get .opblock-summary-method {
    background: #10b981;
}

/* POST Method */
.swagger-ui .opblock.opblock-post {
    background: rgba(139, 92, 246, 0.1); /* Violet Tint */
    border-left: 4px solid #8b5cf6; /* Violet */
}
.swagger-ui .opblock.opblock-post .opblock-summary {
    border-color: #8b5cf6;
}
.swagger-ui .opblock.opblock-post .opblock-summary-method {
    background: #8b5cf6;
}

/* PUT/DELETE/PATCH adjustments */
.swagger-ui .opblock.opblock-put {
    background: rgba(245, 158, 11, 0.1);
    border-left: 4px solid #f59e0b;
}
.swagger-ui .opblock.opblock-delete {
    background: rgba(239, 68, 68, 0.1);
    border-left: 4px solid #ef4444;
}

/* Text Colors in Operations */
.swagger-ui .opblock .opblock-summary-operation-id, 
.swagger-ui .opblock .opblock-summary-path, 
.swagger-ui .opblock .opblock-summary-path__deprecated {
    color: #f3f4f6 !important;
    font-weight: 500;
}
.swagger-ui .opblock .opblock-summary-description {
    color: #9ca3af;
}

/* Schema & Models */
.swagger-ui .scheme-container {
    background-color: #171717;
    box-shadow: none;
    border: 1px solid #262626;
}
.swagger-ui .model {
    color: #e5e5e5;
}
.swagger-ui .model-title {
    color: #a78bfa; /* Violet title for models */
}
.swagger-ui table.model tbody tr td:first-of-type {
    color: #d1d5db;
}

/* Inputs & Forms */
.swagger-ui select {
    background-color: #262626;
    color: white;
    border: 1px solid #404040;
}
.swagger-ui input[type=text], .swagger-ui textarea {
    background-color: #262626;
    color: white;
    border: 1px solid #404040;
}
.swagger-ui .btn {
    background-color: #262626;
    color: #e5e5e5;
    border: 1px solid #404040;
}
.swagger-ui .btn.execute {
    background-color: #8b5cf6;
    color: white;
    border-color: #8b5cf6;
}
.swagger-ui .btn.authorize {
    color: #8b5cf6;
    border-color: #8b5cf6;
}
.swagger-ui .btn.authorize svg {
    fill: #8b5cf6;
}

/* Tags */
.swagger-ui .opblock-tag {
    color: #e5e5e5;
    border-bottom: 1px solid #262626;
}
.swagger-ui .opblock-tag small {
    color: #a3a3a3;
}
"""
