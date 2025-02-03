#!/bin/bash

echo " Başlatılıyor..."

# İlk docker-compose dosyasını başlat (WordPress + MySQL)
echo " WordPress ve MySQL başlatılıyor..."
docker compose -f docker-compose1.yml up -d

# WordPress'in tamamen ayağa kalkmasını bekle
echo " WordPress'in başlaması bekleniyor..."
while ! curl -s http://localhost:8080/wp-json/wp/v2/posts > /dev/null; do
    echo " Bekleniyor..."
    sleep 5
done

echo " WordPress çalışıyor!"

# İkinci docker-compose dosyasını başlat (PostgreSQL, MongoDB, Redis, Custom Containers)
echo " PostgreSQL, MongoDB, Redis ve özel container'lar başlatılıyor..."
docker compose -f docker-compose2.yml up -d

#  PostgreSQL ve MongoDB'nin hazır olmasını bekle
echo " Veritabanları başlatılıyor..."
sleep 10

#  python-data-loader'ı çalıştır
echo " Veri yükleyici çalıştırılıyor..."
docker run --network mentalarts-24_shared_network python-data-loader

# wordpress-modifier'ı çalıştır
echo " Yeni İmage Build Ediliyor..."
docker build -t wordpress-modifier ./wordpress-modifier
echo " WordPress yazısı değiştiriliyor..."
docker run --network mentalarts-24_shared_network wordpress-modifier

echo " Tüm işlemler tamamlandı!"
