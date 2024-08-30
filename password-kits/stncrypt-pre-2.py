import random

print("""STNCRYPT PRE 2
Uyarı: Şifre anahtar dosyanızı kaybederseniz şifrenizi çözemezsiniz. Bu yüzden kaybetmemeye özen gösterin.
Seçenekler:
1-) Metin Şifrele
2-) Dosya Şifrele
3-) Metin Şifre Çöz
4-) Dosya Şifre Çöz""")

secim = input("Seçiminizi giriniz:")

def sifrele(metin, anahtar_dosya):
    sifreli_metin = ""
    anahtarlar = []
    
    for harf in metin:
        if harf.isalpha() or harf.isdigit() or harf in "çğıöşüÇĞİÖŞÜ": 
            kaydirma = random.randint(0, 9)
            sifreli_harf = chr(ord(harf) + kaydirma)
            sifreli_metin += sifreli_harf
            anahtarlar.append(str(kaydirma))
        else:
            sifreli_metin += harf
            anahtarlar.append('0')  
    
    with open(anahtar_dosya, 'w') as dosya:
        dosya.write(','.join(anahtarlar))
    
    return sifreli_metin

def sifre_coz(sifreli_metin, anahtar_dosya):
    with open(anahtar_dosya, 'r') as dosya:
        anahtarlar = dosya.read().split(',')
    
    cozulmus_metin = ""
    
    for i, harf in enumerate(sifreli_metin):
        kaydirma = int(anahtarlar[i])
        cozulmus_harf = chr(ord(harf) - kaydirma)
        cozulmus_metin += cozulmus_harf
    
    return cozulmus_metin

if secim == "1":
    metin = input("Metin giriniz:")
    anahtar_dosya = input("Anahtar dosyasının adını giriniz:")
    sifreli_metin = sifrele(metin, anahtar_dosya)
    print("Şifrelenmiş Metin:", sifreli_metin)

elif secim == "2":
    dosya_adi = input("Şifrelenecek dosyanın adını giriniz:")
    anahtar_dosya = input("Anahtar dosyasının adını giriniz:")
    
    with open(dosya_adi, 'r', encoding='utf-8') as dosya:
        metin = dosya.read()
    
    sifreli_metin = sifrele(metin, anahtar_dosya)
    
    sifreli_dosya_adi = input("Şifrelenmiş dosyanın adını ne olsun:")
    with open(sifreli_dosya_adi, 'w', encoding='utf-8') as dosya:
        dosya.write(sifreli_metin)
    
    print(f"Dosya '{sifreli_dosya_adi}' olarak şifrelendi.")

elif secim == "3":
    sifreli_metin = input("Şifrelenmiş metni giriniz:")
    anahtar_dosya = input("Anahtar dosyasının adını giriniz:")
    cozulmus_metin = sifre_coz(sifreli_metin, anahtar_dosya)
    print("Çözülmüş Metin:", cozulmus_metin)

elif secim == "4":
    sifreli_dosya_adi = input("Şifrelenmiş dosyanın adını giriniz:")
    anahtar_dosya = input("Anahtar dosyasının adını giriniz:")
    
    with open(sifreli_dosya_adi, 'r', encoding='utf-8') as dosya:
        sifreli_metin = dosya.read()
    
    cozulmus_metin = sifre_coz(sifreli_metin, anahtar_dosya)
    
    cozulmus_dosya_adi = input("Çözülmüş dosyanın ismi ne olsun:")
    with open(cozulmus_dosya_adi, 'w', encoding='utf-8') as dosya:
        dosya.write(cozulmus_metin)
    
    print(f"Dosya '{cozulmus_dosya_adi}' olarak çözüldü.")
else:
    print("Geçersiz bir seçenek girdiniz.")
