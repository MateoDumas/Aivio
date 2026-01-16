# 🧠 Aivio - Intelligent AI Backend

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**Aivio** es un backend de última generación diseñado para integrar capacidades de **Inteligencia Artificial** y **Machine Learning** en aplicaciones de producción. Combina la velocidad extrema de FastAPI con la potencia analítica de PyTorch, todo envuelto en una arquitectura segura, escalable y estéticamente cuidada.

🔗 **Live Demo (Render):** [https://aivio-backend.onrender.com](https://aivio-backend.onrender.com)  
📚 **API Docs:** [https://aivio-backend.onrender.com/docs](https://aivio-backend.onrender.com/docs)

---

## 🚀 Características Principales

### 🧠 Inteligencia Artificial Core
- **Motor de Recomendaciones ML:** Inferencia en tiempo real con PyTorch para sugerencias personalizadas basadas en historial.
- **Chatbot Contextual:** Asistente virtual capaz de entender intenciones y responder preguntas sobre el sistema.
- **NLP Sentiment Analysis:** Procesamiento de lenguaje natural para detectar emociones en textos (Positivo/Negativo/Neutral).

### 🛡️ Seguridad & Rendimiento
- **Autenticación JWT:** Sistema robusto de usuarios con OAuth2 Password Flow y hashing bcrypt.
- **Rate Limiting:** Protección contra ataques DDoS y abuso de API mediante `slowapi` (Token Bucket algorithm).
- **Middlewares Avanzados:** Compresión GZip automática, cabeceras de seguridad TrustedHost y CORS configurado.
- **Health Checks Profundos:** Monitoreo activo que verifica no solo el servicio web, sino también la conectividad a la base de datos.

### 🎨 Experiencia de Desarrollador (DX)
- **UI/UX Premium:** Página de inicio y documentación con tema **"Violet Dark"**, modo noche/día y diseño responsive.
- **Workflow Visual:** Tutorial interactivo en la home para entender el flujo de datos.
- **Favicon Dinámico:** Identidad visual única con SVG generado por código (Hex-Brain).

---

## 🛠️ Tech Stack

- **Lenguaje:** Python 3.11+
- **Framework Web:** FastAPI (Asynchronous)
- **Machine Learning:** PyTorch (CPU optimized for inference)
- **Base de Datos:** PostgreSQL 15+ (con SQLAlchemy 2.0 Async + Alembic Migrations)
- **Validación:** Pydantic V2
- **Infraestructura:** Docker & Docker Compose
- **Server:** Uvicorn (ASGI)

---

## ⚡ Quick Start

### 1. Clonar el repositorio
```bash
git clone https://github.com/MateoDumas/Aivio.git
cd Aivio
```

### 2. Configurar entorno local
Crea un archivo `.env` en la raíz (puedes copiar el ejemplo):
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/aivio_db
SECRET_KEY=tu_clave_secreta_super_segura
```

### 3. Ejecutar con Docker (Recomendado)
Levanta todo el stack (API + DB) con un solo comando:
```bash
docker-compose up --build
```
La API estará disponible en `http://localhost:8000`.

### 4. Instalación Manual (Local)
Si prefieres no usar Docker:
```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones de base de datos
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload
```

---

## 📡 API Usage Examples

Puedes probar estos comandos directamente en tu terminal:

### Health Check (Con estado de DB)
```bash
curl -X GET "https://aivio-backend.onrender.com/health"
# Respuesta: {"status": "ok", "database": "connected", "version": "1.0.0"}
```

### Análisis de Sentimiento (NLP)
```bash
curl -X POST "https://aivio-backend.onrender.com/analysis/sentiment" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love the new design, it is amazing!"}'
```

### Chatbot Interaction
```bash
curl -X POST "https://aivio-backend.onrender.com/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "¿Cómo funciona la autenticación?"}'
```

---

## 🌍 Despliegue

### Opción A: Render (Recomendado para ML)
Este proyecto incluye un `render.yaml` (Infrastructure as Code).
1. Conecta tu repo a Render.
2. Render detectará la configuración Blueprints.
3. Desplegará automáticamente:
   - Base de datos PostgreSQL gestionada.
   - Servicio Web con Docker.

### Opción B: Vercel
1. Importa el proyecto en Vercel.
2. Configura las variables de entorno (`DATABASE_URL`, `SECRET_KEY`).
3. **Nota:** PyTorch puede exceder los límites de tamaño de las Serverless Functions en el plan gratuito. Se recomienda usar la versión "light" o desplegar el modelo de ML por separado.

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar los modelos de IA o la arquitectura:
1. Haz un Fork.
2. Crea una rama (`git checkout -b feature/AmazingFeature`).
3. Haz Commit (`git commit -m 'Add some AmazingFeature'`).
4. Push a la rama (`git push origin feature/AmazingFeature`).
5. Abre un Pull Request.

---

## 📄 Licencia

MIT License - Creado con 💜 por [MateoDumas](https://github.com/MateoDumas)
