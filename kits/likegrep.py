def kelime_ara(dosya, kelime, icermeyen=False, satir_numarasi=True, buyukkucuk=True):
    satir_no = 0
    for satir in dosya:
        satir_no += 1
        satir_karsilastirma = satir
        kelime_karsilastirma = kelime

        if not buyukkucuk:
            satir_karsilastirma = satir.lower()
            kelime_karsilastirma = kelime.lower()

        if (kelime_karsilastirma not in satir_karsilastirma and icermeyen) or \
           (kelime_karsilastirma in satir_karsilastirma and not icermeyen):
            if satir_numarasi:
                print(f"{satir_no}: {satir.strip()}")
            else:
                print(satir.strip())



def belli_satir_yazdir(dosya, n):
    try:
        satirlar = dosya.readlines()
        print(satirlar[n - 1].strip())
    except IndexError:
        print("Hatalı satır numarası!")

def belli_satirlar_yazdir(dosya, bas, son):
    try:
        satirlar = dosya.readlines()
        for i in range(bas - 1, son):
            print(satirlar[i].strip())
    except IndexError:
        print("Hatalı aralık!")

def bastan_satirlar(dosya, x):
    for i in range(x):
        print(dosya.readline().strip())

def sondan_satirlar(dosya, x):
    satirlar = dosya.readlines()
    for satir in satirlar[-x:]:
        print(satir.strip())

print("""Veri Analizi Programına Hoş Geldiniz!
1 - Bir dosyada belli kelimeyi ara
2 - Dosyanın belli satırını yazdır
3 - Dosyanın belli satırlarını yazdır
4 - Dosyanın baştan x satırlarını yazdır
5 - Dosyanın sondan x satırlarını yazdır
""")

secim = input("Seçeneğinizi giriniz: ")
dosyaadi = input("Hangi dosya üzerinde işlem yapmak istiyorsunuz: ")

try:
    with open(dosyaadi, "r", encoding="utf-8") as dosya:
        if secim == "1":
            kelime = input("Aranacak kelime: ")
            negatif = input("İçermeyen satırları mı görmek istiyorsun? (e/h): ").lower() == "e"
            numarali = input("Satır numaralarını da görmek ister misin? (e/h): ").lower() == "e"
            buyukkucuk = input("Büyük harf ve küçük harfi birbirinden ayıralım mı (e/h): ").lower() == "e"
            kelime_ara(dosya, kelime, negatif, numarali, buyukkucuk)
        elif secim == "2":
            n = int(input("Hangi satır: "))
            belli_satir_yazdir(dosya, n)
        elif secim == "3":
            bas = int(input("Başlangıç satırı: "))
            son = int(input("Bitiş satırı: "))
            belli_satirlar_yazdir(dosya, bas, son)
        elif secim == "4":
            x = int(input("Kaç satır: "))
            bastan_satirlar(dosya, x)
        elif secim == "5":
            x = int(input("Kaç satır: "))
            sondan_satirlar(dosya, x)
        else:
            print("Geçersiz seçim!")
except FileNotFoundError:
    print("Dosya bulunamadı!")
