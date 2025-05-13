import os
def tahmini_tarih_bul(id_numarasi, veri):
    en_yakin_id = min(veri.keys(), key=lambda x: abs(x - id_numarasi))
    return veri[en_yakin_id], en_yakin_id

veritabani = {
    1000928788: "2020",
    1309616514: "Ağustos 2020",
    1462935120: "Kasım 2020",
    1570270252: "Ocak 2021",
    1723294586: "Mayıs 2021",
    1790025661: "Nisan 2021",
    1947393076: "Ağustos 2021",
    5455507897: "Ağustos 2022",
    5895100533: "Ocak 2023",
    6754822654: "Ocak 2024",
    6937694442: "Nisan 2024",
    7018845924: "Haziran 2024",
    7047103360: "Eylül 2024",
    7142644753: "Nisan 2024",
    7365203268: "Ağustos 2024",
    7514942639: "Ağustos 2024",
    7534422900: "Ekim 2024",
    7572730093: "Ocak 2025",
    7669689824: "Aralık 2024",
    7672045020: "Aralık 2024",
    7741237816: "Ekim 2024",
    7760803104: "Ekim 2024",
    7764441964: "Kasım 2024",
    7783199053: "Kasım 2024",
    7804148889: "Kasım 2024",
    7812868323: "Ekim 2024",
    7838957477: "Eylül 2024",
    7839003790: "Eylül 2024",
    7854121946: "Eylül 2024",
    7860428419: "Eylül 2024",
    7882260566: "Ekim 2024",
    7884758251: "Ekim 2024",
    7905953883: "Ekim 2024",
    7921607077: "Aralık 2024",
    7922252896: "Ekim 2024",
    8015069284: "Ocak 2025 sonrası",
    8085666993: "Aralık 2024",
    8134268736: "Ocak 2025 sonrası"
}

if __name__ == "__main__":
    print("Bu programın kesin tahmin yapabilmesi için daha fazla veriye ihtiyacımız var! Verilerinizi göndererek destek olabilirsiniz!")
    while True:
        try:
            giris = input("Telegram ID girin (çıkmak için 'q'): ").strip()
            if giris.lower() == "q":
                os.system("python3 main.py")
                break
            id_sayi = int(giris)
            tarih, referans_id = tahmini_tarih_bul(id_sayi, veritabani)
            print(f"Tahmini oluşturulma: {tarih}\n")
        except Exception as e:
            print(f"Hata: {e}")
