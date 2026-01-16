from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    app_name: str = "Aivio ML Backend"
    database_url: str = Field(
        default="postgresql+asyncpg://postgres:postgres@db:5432/aivio",
        alias="DATABASE_URL",
    )
    jwt_secret_key: str = Field(default="changeme", alias="JWT_SECRET_KEY")
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    @field_validator("database_url", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: str | None) -> str:
        if not v:
            # Fallback to default if somehow None is passed (though default usually handles this)
            return "postgresql+asyncpg://postgres:postgres@db:5432/aivio"
        
        # Render provides postgres:// or postgresql://, we need postgresql+asyncpg://
        if v.startswith("postgres://"):
            return v.replace("postgres://", "postgresql+asyncpg://", 1)
        if v.startswith("postgresql://") and not v.startswith("postgresql+asyncpg://"):
            return v.replace("postgresql://", "postgresql+asyncpg://", 1)
        return v


def get_settings() -> Settings:
    return Settings()
