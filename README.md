# Aivio Backend: AI-Powered Recommendation System

Backend moderno y escalable construido con **FastAPI**, **PyTorch** y **PostgreSQL**. Diseñado para demostrar una arquitectura de ML profesional lista para producción.

## 🚀 Stack Tecnológico

- **Lenguaje:** Python 3.11+
- **API Framework:** FastAPI
- **Machine Learning:** PyTorch
- **Base de Datos:** PostgreSQL
- **ORM:** SQLAlchemy 2.0 (Async)
- **Migraciones:** Alembic
- **Autenticación:** JWT (OAuth2 Password Flow)
- **Infraestructura:** Docker & Docker Compose

## 🛠 Instalación Local

1.  **Clonar repositorio:**
    ```bash
    git clone <url-del-repo>
    cd Aivio
    ```

2.  **Levantar entorno con Docker Compose:**
    ```bash
    docker compose up --build
    ```
    Esto iniciará la API en `http://localhost:8000` y una base de datos PostgreSQL.

3.  **Generar migración inicial (si es necesario):**
    Si estás desarrollando y cambias los modelos:
    ```bash
    # Asegúrate de que la DB esté corriendo
    docker compose exec web alembic revision --autogenerate -m "Cambios en modelos"
    docker compose exec web alembic upgrade head
    ```

## 🌍 Despliegue

### Opción A: Render (Recomendado)

El proyecto incluye un archivo `render.yaml` para "Infrastructure as Code".

1.  Crea un nuevo **Blueprint Instance** en [Render Dashboard](https://dashboard.render.com/blueprints).
2.  Conecta este repositorio.
3.  Render detectará `render.yaml` y desplegará:
    -   Base de datos PostgreSQL.
    -   Servicio Web (FastAPI).
    -   Ejecutará automáticamente las migraciones al iniciar.

### Opción B: Vercel

Configurado mediante `vercel.json`.
*Nota: El soporte de PyTorch en Serverless puede estar limitado por el tamaño del paquete (250MB).*

1.  Instala Vercel CLI: `npm i -g vercel`
2.  Ejecuta `vercel` y sigue las instrucciones.
3.  Configura las variables de entorno `DATABASE_URL` y `JWT_SECRET_KEY`.

## 🧠 Endpoints Clave

Documentación interactiva disponible en `/docs` (Swagger UI).

-   `POST /auth/register`: Registrar nuevo usuario.
-   `POST /auth/token`: Login (obtiene JWT).
-   `POST /recommendations/`: Obtiene recomendaciones personalizadas usando el modelo PyTorch.

## 📁 Estructura

-   `app/api`: Endpoints y lógica de rutas.
-   `app/ml`: Modelos de PyTorch y lógica de inferencia.
-   `app/db`: Modelos SQLAlchemy y sesión de base de datos.
-   `alembic`: Scripts de migración de base de datos.
