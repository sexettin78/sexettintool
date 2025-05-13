#pip install Pillow exifread piexif
import exifread
from PIL import Image
import piexif

def exif_verilerini_oku(foto_dosyasi):
    try:
        with open(foto_dosyasi, 'rb') as f:
            exif = exifread.process_file(f, details=True) 
            if not exif:
                print("EXIF bilgisi bulunamadı. Fotoğraf dosyası EXIF verisi içermiyor olabilir.")
                return
            print("\033[92mEXIF bilgileri başarıyla bulundu:")
            for tag in exif.keys():
                print(f"{tag}: {exif[tag]}")
            print("\n\nBiraz yukarı kaydırıp daha fazla veriye ulaşabilirsin!")
    except FileNotFoundError:
        print("Dosya bulunamadı. Lütfen geçerli bir dosya yolu girin.")
    except IOError:
        print("Dosya okunamadı. Fotoğrafın doğru formatta olduğundan emin olun.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def exif_verilerini_sil(foto_dosyasi, kayit_dosyasi):
    try:
        image = Image.open(foto_dosyasi)
        data = list(image.getdata())  
        temiz_resim = Image.new(image.mode, image.size)
        temiz_resim.putdata(data)
        temiz_resim.save(kayit_dosyasi)
        print(f"EXIF verileri başarıyla silindi ve fotoğraf '{kayit_dosyasi}' olarak kaydedildi.")
    except FileNotFoundError:
        print("Dosya bulunamadı. Lütfen geçerli bir dosya yolu girin.")
    except IOError:
        print("Dosya okunamadı. Fotoğrafın doğru formatta olduğundan emin olun.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def exif_verisi_ekle(foto_dosyasi, kayit_dosyasi):
    try:
        image = Image.open(foto_dosyasi)
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

        artist = input("Sanatçı (Artist) adı girin: ")
        copyright_info = input("Telif hakkı bilgisi girin: ")

        exif_dict["0th"][piexif.ImageIFD.Artist] = artist
        exif_dict["0th"][piexif.ImageIFD.Copyright] = copyright_info

        exif_bytes = piexif.dump(exif_dict)
        image.save(kayit_dosyasi, exif=exif_bytes)
        print(f"EXIF verileri eklendi. Yeni dosya: {kayit_dosyasi}")
    except FileNotFoundError:
        print("Dosya bulunamadı. Lütfen geçerli bir dosya yolu girin.")
    except IOError:
        print("Dosya okunamadı. Fotoğrafın doğru formatta olduğundan emin olun.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def ana_menu():
    while True:
        print("\nEXIF Verisi İşlemleri:")
        print("1 - Bir fotoğrafın EXIF verilerini oku ve yazdır")
        print("2 - Bir fotoğrafın EXIF verilerini sil")
        print("3 - Bir fotoğrafa EXIF verisi ekle")
        print("4 - Çıkış")

        secim = input("Bir seçenek seçin (1, 2, 3, 4): ")

        if secim == '1':
            foto_dosyasi = input("EXIF bilgilerini görmek istediğiniz fotoğraf dosyasının yolunu girin: ")
            exif_verilerini_oku(foto_dosyasi)
        elif secim == '2':
            foto_dosyasi = input("EXIF verilerini silmek istediğiniz fotoğraf dosyasının yolunu girin: ")
            kayit_dosyasi = input("EXIF'siz yeni fotoğraf dosyasının kaydedileceği yolu ve adı girin: ")
            exif_verilerini_sil(foto_dosyasi, kayit_dosyasi)
        elif secim == '3':
            foto_dosyasi = input("EXIF eklemek istediğiniz fotoğraf dosyasının yolunu girin: ")
            kayit_dosyasi = input("Yeni fotoğraf dosyasının kaydedileceği yolu ve adı girin: ")
            exif_verisi_ekle(foto_dosyasi, kayit_dosyasi)
        elif secim == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

ana_menu()
