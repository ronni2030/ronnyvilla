FROM python:3.10-slim

WORKDIR /app

# copiar requirements primero para cachear pip install
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# gunicorn servirá la app en la variable $PORT que Render proporciona
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:${PORT:-5000}", "--workers", "2"]
