import os
import time
from datetime import datetime

def tarih_degistir(dosya_adi, yeni_tarih_str):
    try:
        yeni_timestamp = time.mktime(datetime.strptime(yeni_tarih_str, "%Y-%m-%d %H:%M:%S").timetuple())
        os.utime(dosya_adi, (yeni_timestamp, yeni_timestamp))
        print(f"{dosya_adi} dosyasının tarihi {yeni_tarih_str} olarak değiştirildi.")
    except Exception as e:
        print("Hata:", e)

dosya = input("Zamanı değiştirilecek dosya adı: ")
yeni_tarih = input("Yeni zaman (Yıl-Ay-Gün Saat:Dakika:Saniye): ")
tarih_degistir(dosya, yeni_tarih)
