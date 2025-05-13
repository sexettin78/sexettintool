import requests
import threading
from urllib.parse import urljoin
import time

def dir_buster(target_url, wordlist_path, timeout=5):
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as wordlist:
            words = [line.strip() for line in wordlist if line.strip()]
    except FileNotFoundError:
        print(f"[!] Wordlist bulunamadı: {wordlist_path}")
        return

    print(f"[*] Hedef: {target_url}")
    print(f"[*] Toplam {len(words)} kelime deneniyor...\n")

    headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    def print_result(url):
        print(f"[+] Bulundu: {url}")

    def check_word(word):
        full_url = urljoin(target_url, word)
        try:
            response = requests.get(full_url, headers=headers, timeout=timeout, allow_redirects=False)
            if response.status_code == 200:
                print_result(full_url)  
            elif response.status_code in [301, 302]:
                print(f"[{response.status_code}] Yönlendirme: {full_url} -> {response.headers.get('Location')}")
        except requests.exceptions.RequestException:
            pass

    def start_threads():
        threads = []
        for word in words:
            t = threading.Thread(target=check_word, args=(word,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    print(f"[*] Tarama başlatıldı...\n")
    start_threads()


target = input("Hedef site (örn: http://10.10.10.10/): ").strip()
wordlist = input("Wordlist dosyası yolu: ").strip()
try:
    timeout = float(input("İstek zaman aşımı (varsayılan 5): ") or 5)
except ValueError:
    timeout = 5

dir_buster(target, wordlist, timeout)
