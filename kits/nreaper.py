import os
import re
import time
import requests
from urllib.parse import urlparse
from scapy.all import IP, TCP, UDP, ICMP, DNS, ARP, Raw, sniff, get_if_list

def klasorleri_hazirla():
    os.makedirs("nreaperkayitlar/resimler", exist_ok=True)
    os.makedirs("nreaperkayitlar/linkler", exist_ok=True)

def linkleri_ayikla(icerik):
    url_pattern = re.compile(r"https?://[^\s'\"<>]+")
    return list(set(url_pattern.findall(icerik)))

def url_tamamlama(packet_text):
    host = ""
    path = ""
    for line in packet_text.splitlines():
        if line.lower().startswith("host:"):
            host = line.split(":", 1)[1].strip()
        elif line.startswith("GET") or line.startswith("POST"):
            try:
                path = line.split()[1].strip()
            except IndexError:
                continue
    if host and path.startswith("/"):
        return f"http://{host}{path}"
    return None

def resimleri_indir(resim_linkleri):
    for url in resim_linkleri:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200 and "image" in response.headers.get("Content-Type", ""):
                dosya_adi = os.path.basename(urlparse(url).path)
                if not dosya_adi:
                    dosya_adi = f"resim_{int(time.time())}_{hash(url)}.jpg"
                yol = os.path.join("nreaperkayitlar/resimler", dosya_adi)
                with open(yol, "wb") as f:
                    f.write(response.content)
                print(f"[✓] {url} indirildi.")
            else:
                print(f"[×] Geçersiz resim içeriği: {url}")
        except Exception as e:
            print(f"[×] {url} indirilemedi: {e}")
        time.sleep(1)

def linkleri_kaydet(urls):
    yol = "nreaperkayitlar/linkler/url_listesi.txt"
    oncekiler = set()
    if os.path.exists(yol):
        with open(yol, "r", encoding="utf-8") as f:
            oncekiler = set(line.strip() for line in f)

    yeni_linkler = [url for url in urls if url not in oncekiler]
    if not yeni_linkler:
        return

    with open(yol, "a", encoding="utf-8") as dosya:
        for url in yeni_linkler:
            dosya.write(url + "\n")
    print(f"[+] {len(yeni_linkler)} yeni bağlantı kaydedildi.")

def analiz_dosyasi_isle(dosya_adi="http_trafik.txt"):
    if not os.path.exists(dosya_adi):
        print(f"[×] {dosya_adi} bulunamadı.")
        return

    with open(dosya_adi, "r", encoding="utf-8", errors="ignore") as f:
        icerik = f.read()

    linkler = linkleri_ayikla(icerik)
    bolumler = icerik.split("\n\n")
    for bolum in bolumler:
        url = url_tamamlama(bolum)
        if url:
            linkler.append(url)

    linkler = list(set(linkler))
    if not linkler:
        print("Hiç URL bulunamadı.")
        return

    resim_linkleri = [url for url in linkler if any(url.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"])]
    linkleri_kaydet(linkler)
    resimleri_indir(resim_linkleri)

def paket_yakala(packet):
    basliksiz_dosya = global_dosya_adi.replace(".txt", "") + "_basliksizpaketler.txt"

    try:
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            protokol = "TCP" if packet.haslayer(TCP) else "UDP"

            if packet.haslayer(Raw):
                payload = packet[Raw].load
                icerik = payload.decode(errors="ignore")

                if "HTTP" in icerik or "GET" in icerik or "POST" in icerik:
                    with open(global_dosya_adi, "a", encoding="utf-8") as f:
                        f.write(icerik + "\n\n")
                    url = url_tamamlama(icerik)
                    if url:
                        linkleri_kaydet([url])
                        if any(url.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]):
                            resimleri_indir([url])
                    time.sleep(0.2)
                else:
                    with open(basliksiz_dosya, "a", encoding="utf-8") as f:
                        f.write(f"[{protokol} Raw ama HTTP değil]\n{icerik}\n\n")
            else:
                with open(basliksiz_dosya, "a", encoding="utf-8") as f:
                    f.write(f"[{protokol} Raw yok] {packet.summary()}\n")

    except Exception as e:
        print(f"[!] Paket işleme hatası: {e}")


def arayuzleri_listele():
    arayuzler = get_if_list()
    print("Kullanılabilir ağ arayüzleri:")
    for i, iface in enumerate(arayuzler):
        print(f"{i + 1}. {iface}")

def filtreyardimcisi():
    print("""-------Filtre Yardımcısı-------
boş bırak            → Tüm trafik
tcp                  → Tüm TCP trafiği
udp                  → Tüm UDP trafiği
tcp port 80              → HTTP trafiği
tcp port 443         → HTTPS (içerik görülemez)
ip host 192.168.1.5  → Belirli bir IP
net 192.168.1.0/24   → Belirli bir alt ağ
""")

if __name__ == "__main__":
    klasorleri_hazirla()
    print(r"""
    
    
                _____
               | |   \		 Bu program sadece kendi cihazınızdan gelen/verilen HTTP trafiğini analiz etmek içindir.
               | |    \		 Tüm ağı analiz etmek için ortadaki adam saldırısı gerçekleştirmek gereklidir.
               | |     \___	 MITM (ortadaki adam) saldırısı yapmadan diğer cihazların HTTPS trafiği çözülemez.
               | |         \	 Yalnızca YÖNETİCİ YETKİLERİYLE ve kendi ağınızda kullanınız.
               | |          \	 Veriler 'nreaperkayitlar' klasörüne kaydedilecektir.
      ~~0     _|_|___________|
       /\/  /____|____________)  Kayıtlı Dosyayı Çözümle seçeneği, paket dosyasından linkleri ve resimleri ayrıştırmaya çalışır.
    . /  \_|__________________|
    |/__    | )(            )(   1 - HTTP Trafiğini Dinle
    | |\\  :| )(            )( 	 2 - Kayıtlı Dosyayı Çözümle

""")
    secim = input("Seçiminiz: ").strip()

    if secim == "1":
        arayuzleri_listele()
        arayuz = input("Kullanmak istediğiniz arayüz: (isim giriniz) ").strip()
        if input("Filtre yardımcısını görmek ister misiniz? (e/h): ").lower() == "e":
            filtreyardimcisi()
        filtre = input("Lütfen filtre ifadesi girin: ").strip()
        global_dosya_adi = input("Verilerin kaydedileceği dosya adı: ").strip()
        print(f"{filtre} filtresi ile dinleniyor... [Ctrl+C ile durdurabilirsiniz]")
        sniff(iface=arayuz, filter=filtre, prn=paket_yakala, store=0)

    elif secim == "2":
        analizdosyasi = input("Analiz edilecek dosya adı: ").strip()
        analiz_dosyasi_isle(analizdosyasi)

    else:
        print("Geçersiz seçim.")
