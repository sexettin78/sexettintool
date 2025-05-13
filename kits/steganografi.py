import base64, os
from PIL import Image
from io import BytesIO
from cryptography.fernet import Fernet

def encrypt_data(data, password=None):
    if not password:
        return data
    key = base64.urlsafe_b64encode(password.ljust(32).encode()[:32])
    f = Fernet(key)
    return f.encrypt(data)

def decrypt_data(data, password=None):
    if not password:
        return data
    key = base64.urlsafe_b64encode(password.ljust(32).encode()[:32])
    f = Fernet(key)
    return f.decrypt(data)

def embed_data_into_image(image_path, secret_file, output_path, password=None):
    with open(secret_file, 'rb') as f:
        secret_data = f.read()

    encoded = encrypt_data(secret_data, password)
    b64_data = base64.b64encode(encoded).decode()

    img = Image.open(image_path)
    img = img.convert("RGBA")
    pixels = img.getdata()

    new_pixels = []
    b64_index = 0

    for pixel in pixels:
        r, g, b, a = pixel
        if b64_index < len(b64_data):
            new_r = ord(b64_data[b64_index])
            b64_index += 1
        else:
            new_r = r
        new_pixels.append((new_r, g, b, a))

    img.putdata(new_pixels)
    img.save(output_path)
    print(f"[+] '{secret_file}' verisi '{output_path}' içine gizlendi.")

def extract_data_from_image(image_path, password=None):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    pixels = img.getdata()

    data = ""
    for pixel in pixels:
        r, g, b, a = pixel
        if 32 <= r <= 126:  
            data += chr(r)
        else:
            break

    try:
        decoded = base64.b64decode(data.encode())
        original = decrypt_data(decoded, password)
        with open("cikarilan_dosya.bin", "wb") as f:
            f.write(original)
        print("[+] Veri başarıyla çıkarıldı → cikarilan_dosya.bin")
    except Exception as e:
        print("[-] Çözme hatası:", e)


print("[1] Sakla (Steghide)")
print("[2] Çıkart")
print("[0] Ana Menü")
secim = input("Seçimin: ")

if secim == "1":
	print("Çok büyük dosyaları küçük resme gömemezsiniz. Ayrıca yalnızca .png uzantılı dosyalar seçiniz.")
	img = input("Kullanılacak resim dosyası (PNG): ")
	dosya = input("Gizlenecek dosya: ")
	cikti = input("Çıktı resim dosyası: ")
	sifre = input("Şifre (opsiyonel): ")
	embed_data_into_image(img, dosya, cikti, sifre if sifre else None)

elif secim == "2":
	steg = input("Gizli veri içeren resim dosyası: ")
	sifre = input("Şifre (opsiyonel): ")
	extract_data_from_image(steg, sifre if sifre else None)

elif secim == "0":
	os.system("python3 main.py")

else:
	print("Hatalı seçim!")

