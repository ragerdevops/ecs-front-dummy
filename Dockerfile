# Use una imagen base ligera de Python
FROM python:3.8-slim
WORKDIR /app
# Copia el script y el archivo requirements.txt al contenedor
COPY requirements.txt /app/requirements.txt
COPY continuous_requests.py /app/continuous_requests.py

# Instala las dependencias necesarias
RUN pip install -r requirements.txt

# Ejecuta el script en segundo plano
CMD ["python", "continuous_requests.py"]

