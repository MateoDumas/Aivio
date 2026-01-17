
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
    <img src="/favicon.svg" alt="Aivio Logo" style="width: 100px; height: 100px; margin-bottom: 15px; filter: drop-shadow(0 0 10px rgba(139, 92, 246, 0.5));">
    <h1 style="color: var(--primary); font-weight: bold; font-size: 2.5rem; margin-bottom: 10px;">Aivio API</h1>
    <p style="font-size: 1.2rem; opacity: 0.8;">Intelligent Backend for Modern AI Applications</p>
</div>

Bienvenido a la documentación interactiva de **Aivio**. Este backend integra Inteligencia Artificial y Machine Learning directamente en el flujo de trabajo de tu aplicación y está pensado para desarrolladores que trabajan con **FastAPI**, **PyTorch**, **PostgreSQL**, **JWT** y **OAuth2**.

## ✨ Características Principales

* **Autenticación Segura**: OAuth2 con Password Flow y JWT.
* **Machine Learning**: Modelos de PyTorch sirviendo predicciones en tiempo real.
* **NLP Analysis**: Procesamiento de texto para análisis de sentimiento.
* **High Performance**: Construido sobre **FastAPI** (ASGI) y **PostgreSQL Async**.

## 📚 Guía Rápida de la API

### 1. Autenticación
- Endpoint: `POST /auth/login`
- Body (form-data): `username`, `password`
- Response:

```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer",
  "expires_in": 3600
}
```

Utiliza el botón **Authorize** y pega tu `access_token` como `Bearer <token>` para probar los endpoints protegidos desde aquí mismo.

### 2. Motor de Recomendaciones (PyTorch)
- Endpoint: `POST /recommendations/`
- Auth: **Requerida** (JWT)
- Request:

```json
{
  "item_ids": [1, 2, 3, 4]
}
```

- Response:

```json
{
  "user_id": 1,
  "recommendations": [
    {"item_id": 4, "score": 0.91},
    {"item_id": 2, "score": 0.87},
    {"item_id": 3, "score": 0.62}
  ]
}
```

### 3. Análisis de Sentimiento (NLP)
- Endpoint: `POST /analysis/sentiment`
- Auth: **No requerida**
- Request:

```json
{
  "text": "Aivio hace que integrar IA en mi backend sea increíblemente fácil"
}
```

- Response:

```json
{
  "sentiment": "positive",
  "confidence": 0.93,
  "keywords": ["backend", "increíblemente"],
  "word_count": 9
}
```

### 4. Chatbot Inteligente
- Endpoint: `POST /chat`
- Auth: **No requerida**
- Request:

```json
{
  "message": "Hola, ¿qué puedes hacer?",
  "context": "docs_sandbox"
}
```

- Response:

```json
{
  "response": "¡Hola! Soy el asistente virtual de Aivio. Puedo ayudarte a explorar nuestra API de IA, generar recomendaciones o analizar textos. ¿Por dónde empezamos?",
  "intent": "greeting",
  "suggested_actions": [
    "¿Qué puedes hacer?",
    "Analizar sentimiento",
    "Recomendar productos"
  ]
}
```

## 🔢 Versionado de la API

La versión pública actual es **v1**. 

- Los endpoints estables viven en el espacio actual (`/auth`, `/recommendations`, `/analysis`, `/chat`).
- Cambios incompatibles en el futuro se liberarán en un nuevo espacio de nombres (por ejemplo, `/v2/...`), manteniendo **v1** disponible durante un periodo de deprecación para facilitar migraciones.

## 🧪 Sandbox embebido

En la esquina inferior derecha verás un panel **"Sandbox /chat"** que te permite enviar mensajes de prueba al endpoint `POST /chat` sin necesidad de herramientas externas. Es ideal para mostrar rápidamente cómo responde el chatbot de Aivio directamente desde esta página de documentación.

## 🧰 SDKs y clientes generados

A partir del archivo OpenAPI (`/openapi.json`) puedes generar SDKs oficiales usando herramientas como [OpenAPI Generator](https://openapi-generator.tech/).

### JavaScript / TypeScript (Node)

```bash
npx @openapitools/openapi-generator-cli generate -i https://aivio-backend.onrender.com/openapi.json -g typescript-axios -o ./sdk/aivio-js
```

### Python

```bash
openapi-generator-cli generate -i https://aivio-backend.onrender.com/openapi.json -g python -o ./sdk/aivio-python
```

### cURL

Puedes consumir cualquier endpoint directamente con `curl`, por ejemplo:

```bash
curl -X POST "https://aivio-backend.onrender.com/chat" -H "Content-Type: application/json" -d "{\"message\": \"Hola Aivio\", \"context\": \"sdk_example\"}"
```

---

💡 **Tip:** Usa el botón **Authorize** con tus credenciales para probar los endpoints protegidos.
"""

# Custom CSS con Variables y Soporte Light/Dark
custom_css = """
/* Theme Variables */
:root {
    --bg-color: #111111;
    --text-color: #e5e5e5;
    --primary: #8b5cf6;
    --primary-soft: rgba(139, 92, 246, 0.1);
    --secondary-bg: #1e1e1e;
    --border-color: #333333;
    --success: #10b981;
    --success-soft: rgba(16, 185, 129, 0.1);
    --get-method: #10b981;
    --post-method: #8b5cf6;
    --put-method: #f59e0b;
    --delete-method: #ef4444;
}

body.light-mode {
    --bg-color: #ffffff;
    --text-color: #1f2937;
    --primary: #7c3aed;
    --primary-soft: rgba(124, 58, 237, 0.1);
    --secondary-bg: #f3f4f6;
    --border-color: #e5e7eb;
    --success: #059669;
    --success-soft: rgba(5, 150, 105, 0.1);
    --get-method: #059669;
    --post-method: #7c3aed;
    --put-method: #d97706;
    --delete-method: #dc2626;
}

/* Global Styles */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

body {
    background-color: var(--bg-color);
    color: var(--text-color);
    font-family: 'Inter', sans-serif;
    transition: background-color 0.3s ease, color 0.3s ease;
}

/* Topbar */
.swagger-ui .topbar {
    background-color: var(--secondary-bg);
    border-bottom: 1px solid var(--border-color);
}
.swagger-ui .topbar a {
    display: none; /* Hide default logo */
}

/* Buttons Container (Theme Toggle & Back to Home) */
#custom-buttons {
    position: absolute;
    top: 15px;
    right: 20px;
    display: flex;
    gap: 10px;
    z-index: 9999;
}

.custom-btn {
    background: transparent;
    border: 1px solid var(--border-color);
    color: var(--text-color);
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
    font-family: 'Inter', sans-serif;
    text-decoration: none;
    transition: all 0.2s;
    display: flex;
    align-items: center;
}

.custom-btn:hover {
    background: var(--primary-soft);
    border-color: var(--primary);
    color: var(--text-color);
}

/* Responsive adjustments */
@media (max-width: 768px) {
    #custom-buttons {
        position: static;
        margin: 10px;
        justify-content: center;
    }
    .swagger-ui .info {
        margin: 20px;
    }
}

/* Info Section */
.swagger-ui .info .title {
    color: var(--primary) !important;
    font-family: 'Inter', sans-serif;
}
.swagger-ui .info p, .swagger-ui .info li {
    color: var(--text-color);
}
.swagger-ui .info h1, .swagger-ui .info h2, .swagger-ui .info h3, .swagger-ui .info h4, .swagger-ui .info h5 {
    color: var(--text-color);
}

/* Operations */
.swagger-ui .opblock {
    border-radius: 8px;
    box-shadow: none;
    border: 1px solid transparent;
    margin-bottom: 15px;
    background: var(--secondary-bg);
}

/* GET */
.swagger-ui .opblock.opblock-get {
    background: var(--success-soft);
    border-color: var(--success);
}
.swagger-ui .opblock.opblock-get .opblock-summary-method {
    background: var(--success);
}

/* POST */
.swagger-ui .opblock.opblock-post {
    background: var(--primary-soft);
    border-color: var(--primary);
}
.swagger-ui .opblock.opblock-post .opblock-summary-method {
    background: var(--primary);
}

/* PUT */
.swagger-ui .opblock.opblock-put {
    background: rgba(245, 158, 11, 0.1);
    border-color: var(--put-method);
}
.swagger-ui .opblock.opblock-put .opblock-summary-method {
    background: var(--put-method);
}

/* DELETE */
.swagger-ui .opblock.opblock-delete {
    background: rgba(239, 68, 68, 0.1);
    border-color: var(--delete-method);
}
.swagger-ui .opblock.opblock-delete .opblock-summary-method {
    background: var(--delete-method);
}

/* Summary Texts */
.swagger-ui .opblock .opblock-summary-operation-id, 
.swagger-ui .opblock .opblock-summary-path, 
.swagger-ui .opblock .opblock-summary-path__deprecated {
    color: var(--text-color) !important;
    font-weight: 500;
}
.swagger-ui .opblock .opblock-summary-description {
    color: var(--text-color);
    opacity: 0.8;
}

/* Schema & Models */
.swagger-ui .scheme-container {
    background-color: var(--secondary-bg);
    box-shadow: none;
    border: 1px solid var(--border-color);
}
.swagger-ui .model {
    color: var(--text-color);
}
.swagger-ui .model-title {
    color: var(--primary);
}
.swagger-ui table.model tbody tr td:first-of-type {
    color: var(--text-color);
    opacity: 0.7;
}

/* Inputs & Forms */
.swagger-ui select {
    background-color: var(--bg-color);
    color: var(--text-color);
    border: 1px solid var(--border-color);
}
.swagger-ui input[type=text], .swagger-ui textarea, .swagger-ui input[type=password] {
    background-color: var(--bg-color);
    color: var(--text-color);
    border: 1px solid var(--border-color);
}
.swagger-ui .btn {
    background-color: var(--secondary-bg);
    color: var(--text-color);
    border: 1px solid var(--border-color);
}
.swagger-ui .btn.execute {
    background-color: var(--primary);
    color: white;
    border-color: var(--primary);
}
.swagger-ui .btn.authorize {
    color: var(--primary);
    border-color: var(--primary);
}
.swagger-ui .btn.authorize svg {
    fill: var(--primary);
}

/* Tags */
.swagger-ui .opblock-tag {
    color: var(--text-color);
    border-bottom: 1px solid var(--border-color);
}
.swagger-ui .opblock-tag small {
    color: var(--text-color);
    opacity: 0.6;
}

/* Markdown */
.swagger-ui .markdown p, .swagger-ui .markdown li {
    color: var(--text-color);
}
"""

custom_js = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        var container = document.createElement("div");
        container.id = "custom-buttons";
        
        var homeBtn = document.createElement("a");
        homeBtn.innerText = "⬅️ Back to Home";
        homeBtn.className = "custom-btn";
        homeBtn.href = "/";
        
        var themeBtn = document.createElement("button");
        themeBtn.innerText = "🌙 Dark Mode";
        themeBtn.className = "custom-btn";
        
        container.appendChild(homeBtn);
        container.appendChild(themeBtn);
        document.body.appendChild(container);
        
        var currentTheme = localStorage.getItem("theme") || "dark";
        if (currentTheme === "light") {
            document.body.classList.add("light-mode");
            themeBtn.innerText = "☀️ Light Mode";
        }

        themeBtn.addEventListener("click", function() {
            document.body.classList.toggle("light-mode");
            var theme = document.body.classList.contains("light-mode") ? "light" : "dark";
            themeBtn.innerText = theme === "light" ? "☀️ Light Mode" : "🌙 Dark Mode";
            localStorage.setItem("theme", theme);
        });

        var sandbox = document.createElement("div");
        sandbox.id = "docs-sandbox";
        sandbox.style.position = "fixed";
        sandbox.style.bottom = "20px";
        sandbox.style.right = "20px";
        sandbox.style.maxWidth = "360px";
        sandbox.style.width = "90%";
        sandbox.style.background = "var(--secondary-bg)";
        sandbox.style.border = "1px solid var(--border-color)";
        sandbox.style.borderRadius = "8px";
        sandbox.style.padding = "12px 14px";
        sandbox.style.boxShadow = "0 15px 30px rgba(0, 0, 0, 0.35)";
        sandbox.style.zIndex = "9999";
        sandbox.style.boxSizing = "border-box";

        var sandboxTitle = document.createElement("div");
        sandboxTitle.textContent = "Sandbox /chat";
        sandboxTitle.style.fontWeight = "600";
        sandboxTitle.style.fontSize = "14px";
        sandboxTitle.style.marginBottom = "6px";

        var sandboxSubtitle = document.createElement("div");
        sandboxSubtitle.textContent = "Envía un mensaje rápido al chatbot sin salir de /docs.";
        sandboxSubtitle.style.fontSize = "12px";
        sandboxSubtitle.style.opacity = "0.8";
        sandboxSubtitle.style.marginBottom = "8px";

        var sandboxInput = document.createElement("input");
        sandboxInput.type = "text";
        sandboxInput.placeholder = "Ej: ¿Qué puedes hacer?";
        sandboxInput.style.width = "100%";
        sandboxInput.style.boxSizing = "border-box";
        sandboxInput.style.padding = "6px 8px";
        sandboxInput.style.marginBottom = "8px";
        sandboxInput.style.borderRadius = "4px";
        sandboxInput.style.border = "1px solid var(--border-color)";
        sandboxInput.style.background = "var(--bg-color)";
        sandboxInput.style.color = "var(--text-color)";

        var sandboxButton = document.createElement("button");
        sandboxButton.textContent = "Probar /chat";
        sandboxButton.style.width = "100%";
        sandboxButton.style.padding = "6px 8px";
        sandboxButton.style.marginBottom = "8px";
        sandboxButton.style.borderRadius = "4px";
        sandboxButton.style.border = "1px solid var(--primary)";
        sandboxButton.style.background = "var(--primary)";
        sandboxButton.style.color = "#ffffff";
        sandboxButton.style.cursor = "pointer";
        sandboxButton.style.fontSize = "13px";

        var sandboxResult = document.createElement("pre");
        sandboxResult.style.display = "none";
        sandboxResult.style.whiteSpace = "pre-wrap";
        sandboxResult.style.wordBreak = "break-word";
        sandboxResult.style.fontSize = "11px";
        sandboxResult.style.maxHeight = "200px";
        sandboxResult.style.overflow = "auto";
        sandboxResult.style.background = "rgba(0, 0, 0, 0.35)";
        sandboxResult.style.borderRadius = "4px";
        sandboxResult.style.padding = "6px 8px";
        sandboxResult.style.margin = "0";

        sandbox.appendChild(sandboxTitle);
        sandbox.appendChild(sandboxSubtitle);
        sandbox.appendChild(sandboxInput);
        sandbox.appendChild(sandboxButton);
        sandbox.appendChild(sandboxResult);
        document.body.appendChild(sandbox);

        sandboxButton.addEventListener("click", function() {
            var value = sandboxInput.value.trim();
            if (!value) {
                sandboxInput.focus();
                return;
            }
            sandboxButton.disabled = true;
            var originalText = sandboxButton.textContent;
            sandboxButton.textContent = "Enviando...";
            fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: value,
                    context: "docs_sandbox"
                })
            })
            .then(function(res) {
                return res.json();
            })
            .then(function(data) {
                sandboxResult.textContent = JSON.stringify(data, null, 2);
                sandboxResult.style.display = "block";
            })
            .catch(function(err) {
                sandboxResult.textContent = "Error: " + err;
                sandboxResult.style.display = "block";
            })
            .finally(function() {
                sandboxButton.disabled = false;
                sandboxButton.textContent = originalText;
            });
        });
    });
</script>
"""
