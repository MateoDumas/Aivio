from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import create_access_token, get_db, get_password_hash, verify_password
from app.config import get_settings
from app.db.models import User


router = APIRouter()
settings = get_settings()


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "description": "Solicitud inválida o email ya registrado.",
            "content": {
                "application/json": {
                    "example": {"detail": "Email already registered"}
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
                                "loc": ["body", "email"],
                                "msg": "value is not a valid email address",
                                "type": "value_error.email",
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
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)) -> UserRead:
    result = await db.execute(select(User).where(User.email == user_in.email))
    user = result.scalar_one_or_none()
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    db_user = User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
        is_active=True,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return UserRead.model_validate(db_user)


@router.post(
    "/token",
    response_model=Token,
    responses={
        400: {
            "description": "Credenciales inválidas.",
            "content": {
                "application/json": {
                    "example": {"detail": "Incorrect username or password"}
                }
            },
        },
        401: {
            "description": "No autorizado.",
            "content": {
                "application/json": {
                    "example": {"detail": "Not authenticated"}
                }
            },
        },
        422: {
            "description": "Error de validación en el formulario de login.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "username"],
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
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
) -> Token:
    result = await db.execute(select(User).where(User.email == form_data.username))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")
