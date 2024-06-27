# app/Dockerfile
FROM python:3.10-slim

RUN apt-get update

# Çalışma dizinimizi oluşturuyoruz ve belirliyoruz
WORKDIR /app

# Gereksinim dosyamızı container içine kopyalıyoruz
COPY requirements.txt .

# Gereksinim dosyasındaki paketleri yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarımızı container içine kopyalıyoruz
COPY . .

# Container içinde Streamlit uygulamamızı başlatıyoruz
CMD ["streamlit", "run", "app.py"]


