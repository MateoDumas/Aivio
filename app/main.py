import time
from pathlib import Path

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html

from app.api.routes.auth import router as auth_router
from app.api.routes.recommendations import router as recommendations_router
from app.api.routes.analysis import router as analysis_router
from app.api.routes.chat import router as chat_router
from app.config import get_settings
from app.db.session import Base, engine
from app.docs import tags_metadata, description as api_description, custom_css, custom_js


settings = get_settings()
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

# Configuración CORS (Permisiva para desarrollo/demo)
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
    Devuelve un favicon SVG generado dinámicamente (Cerebro Violeta).
    """
    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
      <style>
        .brain { fill: #8b5cf6; }
      </style>
      <path class="brain" d="M50 10c-15 0-28 8-34 20-3 0-6 2-8 5-2 3-2 7 0 10 1 2 3 3 5 4 0 3 1 6 2 9-2 2-3 5-3 8s1 6 4 8c1 3 4 5 7 6 4 9 14 15 27 15s23-6 27-15c3-1 6-3 7-6 3-2 4-5 4-8s-1-6-3-8c1-3 2-6 2-9 2-1 4-2 5-4 2-3 2-7 0-10-2-3-5-5-8-5-6-12-19-20-34-20zm0 10c10 0 19 6 23 14h-46c4-8 13-14 23-14z"/>
    </svg>
    """
    return Response(content=svg_content, media_type="image/svg+xml")


@app.get("/health", tags=["system"])
async def health() -> dict[str, str]:
    return {"status": "ok"}


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
