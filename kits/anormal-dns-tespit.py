import socket
import struct
import time

def dns_anomali_tespiti():
    print("Belirlenen sınırdan fazla DNS isteği gönderildiğinde uyarı verilecektir.")
    uyari_istek = int(input("Kaç istekten sonra uyarı versin:"))
    soket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    soket.bind(("0.0.0.0", 53))
    ip_adresleri = {}

    while True:
        try:
            data, addr = soket.recvfrom(65535)
            ip_header = data[0:20]
            ip_hdr = struct.unpack("!BBHHHBBH4s4s", ip_header)

            src_ip = socket.inet_ntoa(ip_hdr[8])
            if src_ip in ip_adresleri:
                ip_adresleri[src_ip] += 1
            else:
                ip_adresleri[src_ip] = 1
            if ip_adresleri[src_ip] > uyari_istek:
                print(f"[!] Anomali tespit edildi! IP: {src_ip} {uyari_istek}'dan fazla DNS isteği gönderdi.")
                ip_adresleri[src_ip] = 0  

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Hata: {e}")

start = input("DNS Anomali Tespit Aracını başlatmak için 'baslat' yazın: ")
if start.lower() == 'baslat':
    dns_anomali_tespiti()
