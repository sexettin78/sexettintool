from scapy.all import IP, ICMP, sr1
import socket
import time

def traceroute(destination, max_hops=30, timeout=2):
    print(f"\nTraceroute başlatıldı: {destination} (maksimum {max_hops} hop)\n")

    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=destination, ttl=ttl) / ICMP()
        start_time = time.time()
        reply = sr1(pkt, verbose=0, timeout=timeout)
        end_time = time.time()

        if reply is None:
            print(f"{ttl:2} *  (zaman aşımı)")
        else:
            try:
                hostname = socket.gethostbyaddr(reply.src)[0]
            except socket.herror:
                hostname = reply.src  
            if reply.type == 0:
                print(f"{ttl:2} {hostname} [{reply.src}]  {round((end_time - start_time)*1000)} ms  (hedefe ulaşıldı)")
                break
            else:
                print(f"{ttl:2} {hostname} [{reply.src}]  {round((end_time - start_time)*1000)} ms")

if __name__ == "__main__":
    hedef = input("Hedef IP veya domain girin: ")
    traceroute(hedef)
