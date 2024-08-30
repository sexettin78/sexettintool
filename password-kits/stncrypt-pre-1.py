def karakter_listesi_olustur():
    karakterler = []
    karakterler.extend("abcdefghijklmnopqrstuvwxyzçğıöşü")
    karakterler.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZÇĞİÖŞÜ")
    karakterler.extend("0123456789")
    karakterler.extend("!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~")

    return karakterler

def metin_sifrele(metin, karakterler):
    ters_metin = metin[::-1] 
    sifreli_metin = ""

    for i, harf in enumerate(ters_metin):
        if harf in karakterler: 
            indeks = karakterler.index(harf)
            if i % 2 == 0:  
                yeni_indeks = (indeks + 3) % len(karakterler)
            else: 
                yeni_indeks = (indeks + 5) % len(karakterler)
            sifreli_metin += karakterler[yeni_indeks]
        else:
            sifreli_metin += harf  

    return sifreli_metin

def metin_sifre_coz(sifreli_metin, karakterler):
    cozulmus_metin = ""

    for i, harf in enumerate(sifreli_metin):
        if harf in karakterler: 
            indeks = karakterler.index(harf)
            if i % 2 == 0: 
                yeni_indeks = (indeks - 3) % len(karakterler)
            else: 
                yeni_indeks = (indeks - 5) % len(karakterler)
            cozulmus_metin += karakterler[yeni_indeks]
        else:
            cozulmus_metin += harf 

    cozulmus_metin = cozulmus_metin[::-1]  
    return cozulmus_metin


print("""STNCRYPT PRE 1
Seçenekler:
1-) Metin Şifrele
2-) Dosya Şifrele
3-) Metin Şifre Çöz
4-) Dosya Şifre Çöz""")

secim = input("Seçiminizi giriniz: ")
karakterler = karakter_listesi_olustur()

if secim == "1":
    metin = input("Metin giriniz:")
    sifreli_metin = metin_sifrele(metin, karakterler)
    print("Şifrelenmiş Metin:", sifreli_metin)

elif secim == "2":
    dosya_adi = input("Şifrelenecek dosyanın ismini giriniz: ")
    sifreli_dosya_adi = input("Şifreli dosyanın ismi ne olsun istersiniz: ")
    with open(dosya_adi, 'r', encoding='utf-8') as dosya:
        metin = dosya.read()

    sifreli_metin = metin_sifrele(metin, karakterler)

    with open(sifreli_dosya_adi, 'w', encoding='utf-8') as dosya:
        dosya.write(sifreli_metin)

    print(f"Dosya '{dosya_adi}' başarıyla '{sifreli_dosya_adi}' olarak şifrelendi.")

elif secim == "3":
    sifreli_metin = input("Şifrelenmiş metni giriniz:")
    cozulmus_metin = metin_sifre_coz(sifreli_metin, karakterler)
    print("Çözülmüş Metin:", cozulmus_metin)

elif secim == "4":
    sifreli_dosya_adi = input("Çözülecek dosyanın ismini giriniz: ")
    cozulmus_dosya_adi = input("Çözülmüş dosyanın ismini giriniz: ")
    with open(sifreli_dosya_adi, 'r', encoding='utf-8') as dosya:
        sifreli_metin = dosya.read()

    cozulmus_metin = metin_sifre_coz(sifreli_metin, karakterler)

    with open(cozulmus_dosya_adi, 'w', encoding='utf-8') as dosya:
        dosya.write(cozulmus_metin)

    print(f"Dosya '{sifreli_dosya_adi}' başarıyla '{cozulmus_dosya_adi}' olarak çözüldü.")

else:
    print("Geçersiz bir seçenek girdiniz.")
