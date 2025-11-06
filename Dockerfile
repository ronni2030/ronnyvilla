# Imagen base de Python
FROM python:3.10-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos al contenedor
COPY . .

# Instalar pytest
RUN pip install pytest

# Comando por defecto al ejecutar el contenedor
CMD ["pytest", "-v"]
