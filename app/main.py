import time
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.auth import router as auth_router
from app.api.routes.recommendations import router as recommendations_router
from app.api.routes.analysis import router as analysis_router
from app.api.routes.chat import router as chat_router
from app.config import get_settings
from app.db.session import Base, engine


settings = get_settings()
app = FastAPI(
    title=settings.app_name,
    description="Backend inteligente con IA, ML y NLP.",
    version="1.0.0"
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

# Configuración de templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.on_event("startup")
async def on_startup() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])
app.include_router(analysis_router, prefix="/analysis", tags=["analysis"])

