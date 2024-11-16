# sentiment-news-analysis-api (Puerto 8082)

API de análisis de sentimiento en noticias sobre las acciones desarrollada en Python y FastAPI.

## Pasos para levantar en local

### 1. Crear archivo .env en la raíz del proyecto

![image](https://github.com/user-attachments/assets/cb0e2513-6cc0-45de-8be1-744ea921ad2e)

![image](https://github.com/user-attachments/assets/a99648eb-da51-43a0-82ef-b016cffd34bc)

### 2. Instalar librerías

```bash
pip install -r requirements.txt
```

### 3. Levantar el proyecto en el puerto 8082

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8082
```
