import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

url = input("Hedef URL'yi girin (https:// ile): ").strip()

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except Exception as e:
    print(f"Hata oluştu: {e}")
    exit()

soup = BeautifulSoup(response.content, "html.parser")

tumunu_mu = input("Tüm etiketleri mi çekmek istiyorsun? (e/h): ").lower() == "e"

etiketler = []
if not tumunu_mu:
    tag_input = input("Hangi etiket(ler)i çekmek istiyorsun? (virgülle ayır): ")
    etiketler = [etiket.strip() for etiket in tag_input.split(",")]

sadece_icerik = input("Etiketle birlikte mi yazdıralım? (e/h): ").lower() != "e"

dosyaya_kaydet = input("Sonuçlar dosyaya kaydedilsin mi? (e/h): ").lower() == "e"
output_file = ""
if dosyaya_kaydet:
    output_file = input("Dosya adı ve uzantısını giriniz: ")

def yazdir_veya_kaydet(veri):
    print(veri)
    if dosyaya_kaydet:
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(veri + "\n")

if tumunu_mu:
    for tag in soup.find_all():
        try:
            veri = tag.get_text(strip=True) if sadece_icerik else str(tag)
            yazdir_veya_kaydet(veri)
        except Exception as e:
            print(f"Hata: {e}")
else:
    for etiket in etiketler:
        bulunanlar = soup.find_all(etiket)
        if not bulunanlar:
            print(f"Uyarı: <{etiket}> etiketi bulunamadı.")
            continue
        for eleman in bulunanlar:
            try:
                veri = eleman.get_text(strip=True) if sadece_icerik else str(eleman)
                yazdir_veya_kaydet(veri)
            except Exception as e:
                print(f"Hata: {e}")

if dosyaya_kaydet:
    print(f"Sonuçlar '{output_file}' dosyasına kaydedildi.")
