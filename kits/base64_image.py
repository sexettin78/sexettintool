import base64

print("""1 - Base64'den Resime
2 - Resimden Base64'e """)
secim = input("Hangisini seçiyorsunuz: ")
if secim == "1":
    cikti = input("Base64 Verisi İçeren Dosyasının İsmi ve Uzantısını Giriniz: ")
    f = open(cikti, 'rb') 
    byte = f.read() 
    f.close()
    dosya = input("Oluşacak Resim Dosyasının İsmini ve Uzantısını Belirtiniz: ")
    decode = open(dosya, 'wb') 
    decode.write(base64.b64decode(byte))  
    decode.close()
    print("İşlem Başarılı")

elif secim == "2":
    dosya = input("Resim Dosyası Belirtiniz: ")
    with open(dosya, "rb") as img:
        s = base64.b64encode(img.read())
    cikti = input("Çıktı Dosyasının İsmi ve Uzantısını Giriniz: ")
    with open(cikti, "wb") as f:
        f.write(s)
    print("İşlem Başarılı")

else:
    print("Geçersiz Seçim")