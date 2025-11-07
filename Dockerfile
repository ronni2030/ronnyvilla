FROM python:3.10-slim

WORKDIR /app

# Copiar requirements primero para cachear pip install
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer puerto por defecto
EXPOSE 5000

# Variable de entorno con valor por defecto
ENV PORT=5000

# Usar shell form para que las variables de entorno se expandan correctamente
CMD gunicorn main:app --bind 0.0.0.0:$PORT --workers 2