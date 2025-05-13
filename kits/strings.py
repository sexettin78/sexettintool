import re

def string_cek(dosya_yolu, min_uzunluk=4):
    try:
        with open(dosya_yolu, 'rb') as f:
            data = f.read()

        ascii_strings = re.findall(rb'[\x20-\x7E]{%d,}' % min_uzunluk, data)
        ascii_texts = [s.decode('utf-8', errors='ignore') for s in ascii_strings]

        utf16_strings = re.findall((b'(?:[\x20-\x7E]\x00){%d,}' % min_uzunluk), data)
        utf16_texts = [s.decode('utf-16le', errors='ignore') for s in utf16_strings]

        with open("veri_ciktisi1.txt", "w", encoding='utf-8') as f1:
            for line in ascii_texts:
                f1.write(line + "\n")
        with open("veri_ciktisi2.txt", "w", encoding='utf-8') as f2:
            for line in utf16_texts:
                f2.write(line + "\n")

        print("[+] ASCII stringler 'ASCII_veri_ciktisi.txt' dosyasına kaydedildi.")
        print("[+] UTF-16 stringler 'UTF-16_veri_ciktisi.txt' dosyasına kaydedildi.")

    except FileNotFoundError:
        print("[-] Dosya bulunamadı!")
    except Exception as e:
        print(f"[-] Hata oluştu: {e}")
import re

def string_cek(dosya_yolu, min_uzunluk=4):
    try:
        with open(dosya_yolu, 'rb') as f:
            data = f.read()

        ascii_strings = re.findall(rb'[\x20-\x7E]{%d,}' % min_uzunluk, data)
        ascii_texts = [s.decode('utf-8', errors='ignore') for s in ascii_strings]

        utf16_strings = re.findall((b'(?:[\x20-\x7E]\x00){%d,}' % min_uzunluk), data)
        utf16_texts = [s.decode('utf-16le', errors='ignore') for s in utf16_strings]

        with open("ASCII_veri_ciktisi.txt", "w", encoding='utf-8') as f1:
            for line in ascii_texts:
                f1.write(line + "\n")

        with open("UTF-16_veri_ciktisi.txt", "w", encoding='utf-8') as f2:
            for line in utf16_texts:
                f2.write(line + "\n")

        print("[+] ASCII stringler 'ASCII_veri_ciktisi.txt' dosyasına kaydedildi.")
        print("[+] UTF-16 stringler 'UTF-16_veri_ciktisi.txt' dosyasına kaydedildi.")

    except FileNotFoundError:
        print("[-] Dosya bulunamadı!")
    except Exception as e:
        print(f"[-] Hata oluştu: {e}")
dosya = input("Tarama yapılacak dosya yolu: ")
string_cek(dosya)
