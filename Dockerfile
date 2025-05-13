FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    sudo \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgtk-3-dev \
    pkg-config \
    unzip \
    zip \
    neofetch \
    figlet \
    mpv \
    chkrootkit \
    wafw00f \
    ncrack \
    nmap \
    lynis \
    crunch \
    ike-scan \
    macchanger \
    net-tools \
    sqlmap \
    hydra \
    aircrack-ng \
    php \
    ffmpeg \
    && apt-get clean

# Python bağımlılıklarını kur
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Proje dosyalarını kopyala
COPY . /app
WORKDIR /app

# Başlangıç komutu
CMD ["python3", "main.py"]
