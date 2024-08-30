import requests
import random
import string

def random_string(uzunluk):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=uzunluk))

def fuzzing_araci(url, parametre, deneme_sayisi):
    for _ in range(deneme_sayisi):
        random_veri = random_string(10)
        tam_url = f"{url}?{parametre}={random_veri}"
        print(f"Deneme: {tam_url}")
        response = requests.get(tam_url)
        if response.status_code != 200:
            print(f"[!] Farklı bir HTTP durumu kodu tespit edildi: {response.status_code} - Payload: {random_veri}")
        else:
            print(f"[-] Standart yanıt alındı: {response.status_code}")

# Kullanıcıdan giriş al
url = input("Hedef URL'yi girin (örn. http://hedefsite.com/sayfa.php): ")
parametre = input("Fuzzing yapılacak parametreyi girin (örn. id): ")
deneme_sayisi = int(input("Kaç deneme yapılacağını girin: "))

fuzzing_araci(url, parametre, deneme_sayisi)
