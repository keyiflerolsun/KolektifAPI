# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

# Docker Python İmajı
FROM python:3.10.6-slim-buster

WORKDIR /usr/src/app
COPY ./ /usr/src/app

# Gerekli Paketlerin Yüklenmesi
RUN apt-get -y update && \
    apt-get -y upgrade && \
    rm -rf /var/lib/apt/lists/*

# Pip Güncellemesi ve Kütüphane Kurulumları
RUN python3 -m pip install -U pip

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -Ur requirements.txt

# FLASK Başlatılması
CMD ["python3", "basla.py"]