import os
import time

def dosya_degisiklik_monitörü(dizin):
    onceki_durum = dict([(f, None) for f in os.listdir(dizin)])
    
    while True:
        suanki_durum = dict([(f, None) for f in os.listdir(dizin)])
        eklenenler = [f for f in suanki_durum if not f in onceki_durum]
        silinenler = [f for f in onceki_durum if not f in suanki_durum]
        
        if eklenenler:
            print(f"Yeni dosyalar eklendi: {', '.join(eklenenler)}")
        if silinenler:
            print(f"Dosyalar silindi: {', '.join(silinenler)}")
        
        onceki_durum = suanki_durum
        time.sleep(2)

dizin = input("İzlenecek dizin yolunu girin: ")
print("Başladı. Değişiklikler altta görünecek")
dosya_degisiklik_monitörü(dizin)
