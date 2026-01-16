import time
from pathlib import Path

from fastapi import FastAPI, Request, Response, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.docs import get_swagger_ui_html

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.api.routes.auth import router as auth_router
from app.api.routes.recommendations import router as recommendations_router
from app.api.routes.analysis import router as analysis_router
from app.api.routes.chat import router as chat_router
from app.config import get_settings
from app.db.session import Base, engine
from app.docs import tags_metadata, description as api_description, custom_css, custom_js
from sqlalchemy import text


settings = get_settings()

# Rate Limiter Configuration
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Aivio API",
    description=api_description,
    version="1.0.0",
    openapi_tags=tags_metadata,
    docs_url=None,  # Desactivamos el default para personalizarlo
    redoc_url=None,
    contact={
        "name": "Mateo Dumas",
        "url": "https://github.com/MateoDumas",
        "email": "mateo@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# --- Middlewares ---

# 1. Rate Limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# 2. Trusted Host (Security)
app.add_middleware(
    TrustedHostMiddleware, 
    allowed_hosts=["*"] # Ajustar en producción a dominios reales
)

# 3. GZip Compression (Performance)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# 4. CORS (Permisiva para desarrollo/demo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, restringir a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware de Métricas (Tiempo de proceso)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Configuración de templates
BASE_DIR = Path(__file__).resolve().parent
try:
    templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
except Exception:
    templates = None

@app.on_event("startup")
async def on_startup() -> None:
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except Exception as e:
        print(f"Database connection failed: {e}")
        # No fallamos la app completa para que al menos la home funcione


# --- Custom Docs Route ---
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """
    Renderiza la documentación Swagger UI con tema personalizado (Violet Dark).
    """
    html = get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Docs",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_favicon_url="/favicon.ico",
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1, # Colapsar modelos por defecto
            "docExpansion": "list",         # Mostrar lista expandida
            "filter": True,                 # Barra de búsqueda
            "syntaxHighlight.theme": "obsidian"
        }
    )
    # Inyectar CSS y JS personalizados
    body = html.body.decode("utf-8")
    custom_style = f"<style>{custom_css}</style>"
    
    # Insertar estilo antes de cerrar el head
    body = body.replace("</head>", f"{custom_style}</head>")
    # Insertar script antes de cerrar el body
    body = body.replace("</body>", f"{custom_js}</body>")
    
    return HTMLResponse(body)


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """
    Devuelve un favicon SVG generado dinámicamente (Aivio Hex-Brain).
    """
    svg_content = """
    <svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#a78bfa;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#7c3aed;stop-opacity:1" />
        </linearGradient>
        <filter id="glow">
          <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
          <feMerge>
            <feMergeNode in="coloredBlur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>
      
      <!-- Fondo oscuro squircle (cuadrado redondeado) -->
      <rect x="5" y="5" width="90" height="90" rx="22" fill="#0f172a" stroke="#334155" stroke-width="2" />
      
      <!-- Estructura Hexagonal / Neuronal -->
      <g filter="url(#glow)" transform="translate(50, 50)">
        <!-- Hexágono exterior -->
        <path d="M0 -30 L26 -15 L26 15 L0 30 L-26 15 L-26 -15 Z" fill="none" stroke="url(#grad)" stroke-width="2.5" opacity="0.8" />
        
        <!-- Conexiones internas al núcleo -->
        <line x1="0" y1="0" x2="0" y2="-30" stroke="url(#grad)" stroke-width="1.5" />
        <line x1="0" y1="0" x2="26" y2="-15" stroke="url(#grad)" stroke-width="1.5" />
        <line x1="0" y1="0" x2="26" y2="15" stroke="url(#grad)" stroke-width="1.5" />
        <line x1="0" y1="0" x2="0" y2="30" stroke="url(#grad)" stroke-width="1.5" />
        <line x1="0" y1="0" x2="-26" y2="15" stroke="url(#grad)" stroke-width="1.5" />
        <line x1="0" y1="0" x2="-26" y2="-15" stroke="url(#grad)" stroke-width="1.5" />
        
        <!-- Núcleo de IA -->
        <circle cx="0" cy="0" r="7" fill="url(#grad)" />
        
        <!-- Nodos periféricos -->
        <circle cx="0" cy="-30" r="3" fill="#fff" />
        <circle cx="26" cy="-15" r="3" fill="#fff" />
        <circle cx="26" cy="15" r="3" fill="#fff" />
        <circle cx="0" cy="30" r="3" fill="#fff" />
        <circle cx="-26" cy="15" r="3" fill="#fff" />
        <circle cx="-26" cy="-15" r="3" fill="#fff" />
      </g>
    </svg>
    """
    return Response(content=svg_content, media_type="image/svg+xml")


@app.get("/health", tags=["system"])
@limiter.limit("5/minute")
async def health(request: Request) -> dict[str, str]:
    """
    Health check extendido. Verifica también la conexión a BD.
    """
    db_status = "unknown"
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
            db_status = "connected"
    except Exception as e:
        db_status = f"disconnected: {str(e)}"
        
    return {
        "status": "ok", 
        "database": db_status,
        "version": settings.VERSION if hasattr(settings, "VERSION") else "1.0.0"
    }


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def root(request: Request):
    if templates:
        return templates.TemplateResponse("index.html", {"request": request})
    else:
        # Fallback simple si los templates fallan
        return HTMLResponse(content="""
        <html>
            <head>
                <title>Aivio API</title>
                <link rel="icon" href="/favicon.ico" type="image/svg+xml">
            </head>
            <body style="background:#111111; color:white; font-family:sans-serif; text-align:center; padding:50px;">
                <h1 style="color:#8b5cf6;">🧠 Aivio API is Running</h1>
                <p>Templates not loaded properly.</p>
                <a href="/docs" style="color:#a78bfa;">Go to Documentation</a>
            </body>
        </html>
        """)


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])
app.include_router(analysis_router, prefix="/analysis", tags=["analysis"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
