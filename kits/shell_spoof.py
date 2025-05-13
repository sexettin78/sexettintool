import shutil
import os

os.makedirs("spoofed_files", exist_ok=True)

uzanti_listesi = [
    ".php5", ".phtml", ".phar", ".jpg.php", ".png.php", ".php.jpg",
    ".inc", ".txt", ".html", ".htaccess"
]

magic_bytes = {
    "jpg": b"\xFF\xD8\xFF\xE0",        # JPEG
    "png": b"\x89PNG\r\n\x1a\n",       # PNG
    "gif": b"GIF89a",                  # GIF
    "pdf": b"%PDF-",                   # PDF
    "zip": b"PK\x03\x04"               # ZIP
}

def dosya_spoofla(dosya_adi):
    with open(dosya_adi, "rb") as f:
        orijinal_veri = f.read()

    for uzanti in uzanti_listesi:
        yeni_ad = os.path.join("spoofed_files", f"spoofed{uzanti}")
        shutil.copy(dosya_adi, yeni_ad)

    for isim, header in magic_bytes.items():
        yeni_ad = os.path.join("spoofed_files", f"spoofed_{isim}.bin")
        with open(yeni_ad, "wb") as f:
            f.write(header + b"\n" + orijinal_veri)

    print("[+] Dosya spoofing işlemleri tamamlandı!")
    print("[*] Oluşturulan dosyaları deneyin: (spoof_files klasörüne aktarıldı)")
    for uzanti in uzanti_listesi:
        print(f" - spoofed{uzanti}")
    for isim in magic_bytes:
        print(f" - spoofed_{isim}.bin")

dosya = input("Spoof işlemi yapılacak dosyanın adı: ")
dosya_spoofla(dosya)
