# app/Dockerfile
FROM python:3.10-slim
RUN apt-get update
# Çalışma dizinini ayarla
WORKDIR /app

RUN pip install --upgrade pip

# Gerekli dosyaları kopyala
COPY requirements.txt requirements.txt
COPY app.py app.py

# Gerekli paketleri yükle
RUN pip install -r requirements.txt

# Uygulamayı başlat
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]

