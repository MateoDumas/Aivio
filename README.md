# 🧠 Aivio - Intelligent AI Backend

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

Aivio es un backend moderno y escalable diseñado para integrar capacidades de **Inteligencia Artificial** y **Machine Learning** en aplicaciones de producción. Combina la velocidad de FastAPI con la potencia de PyTorch.

🔗 **Live Demo:** [https://aivio-nu.vercel.app](https://aivio-nu.vercel.app)  
📚 **API Docs:** [https://aivio-nu.vercel.app/docs](https://aivio-nu.vercel.app/docs)

---

## 🚀 Características Principales

- **🤖 Motor de Recomendaciones ML:** Sistema basado en PyTorch que aprende de las interacciones del usuario para sugerir items relevantes.
- **💬 Chatbot Inteligente:** Asistente virtual integrado capaz de entender contexto y guiar a los usuarios.
- **📊 Análisis de Sentimiento (NLP):** Procesamiento de lenguaje natural para detectar emociones en textos (Positivo/Negativo/Neutral).
- **🔒 Seguridad Robusta:** Autenticación completa con JWT (OAuth2 Password Flow) y hashing de contraseñas.
- **📈 Métricas en Tiempo Real:** Headers de rendimiento (`X-Process-Time`) y monitoreo de salud.
- **☁️ Multi-Cloud Deploy:** Configurado para desplegarse automáticamente en **Vercel** (Serverless) y **Render** (Contenedores).

---

## 🛠️ Tech Stack

- **Lenguaje:** Python 3.11+
- **Framework Web:** FastAPI
- **Machine Learning:** PyTorch (CPU optimized for cloud)
- **Base de Datos:** PostgreSQL (con SQLAlchemy 2.0 Async + Alembic)
- **Validación:** Pydantic V2
- **Infraestructura:** Docker & Docker Compose

---

## ⚡ Quick Start

### 1. Clonar el repositorio
```bash
git clone https://github.com/MateoDumas/Aivio.git
cd Aivio
```

### 2. Configurar entorno local
Crea un archivo `.env` en la raíz:
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/aivio_db
SECRET_KEY=tu_clave_secreta_super_segura
```

### 3. Ejecutar con Docker (Recomendado)
```bash
docker-compose up --build
```
La API estará disponible en `http://localhost:8000`.

### 4. Instalación Manual
```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

# Instalar dependencias
pip install -r requirements.txt
pip install -r requirements-ml.txt

# Ejecutar migraciones
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload
```

---

## 📡 API Usage Examples

### Health Check
```bash
curl -X GET "https://aivio-nu.vercel.app/health"
```

### Análisis de Sentimiento (NLP)
```bash
curl -X POST "https://aivio-nu.vercel.app/analysis/sentiment" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love using this API, it is amazing!"}'
```

### Chatbot
```bash
curl -X POST "https://aivio-nu.vercel.app/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "¿Qué puedes hacer?"}'
```

---

## 🌍 Despliegue

### Opción A: Render (Full ML)
Este proyecto incluye un `render.yaml` listo para usar.
1. Conecta tu repo a Render.
2. Render detectará la configuración Blueprints.
3. Desplegará la base de datos y el servicio web automáticamente.

### Opción B: Vercel (Serverless)
Optimizado para funcionar en el Free Tier de Vercel.
1. Importa el proyecto en Vercel.
2. Vercel usará `vercel.json` y `api/index.py`.
3. **Nota:** En Vercel, el modelo de PyTorch usa una versión ligera (fallback) para cumplir con los límites de tamaño serverless.

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un PR.

## 📄 Licencia

MIT License - Creado por [MateoDumas](https://github.com/MateoDumas)
