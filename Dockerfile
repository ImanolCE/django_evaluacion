# Usa una imagen de Python
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000 para Django
EXPOSE 8000

# Comando para iniciar Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
