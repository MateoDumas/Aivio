from fastapi import FastAPI

from app.api.routes.auth import router as auth_router
from app.api.routes.recommendations import router as recommendations_router
from app.config import get_settings
from app.db.session import Base, engine


settings = get_settings()
app = FastAPI(title=settings.app_name)


@app.on_event("startup")
async def on_startup() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "Welcome to Aivio API",
        "docs": "/docs",
        "health": "/health"
    }


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])

