from scapy.all import sniff

def paket_yakala(paket):
    print(paket.show())
hedef_port = input("Dinlemek istediğiniz portu girin (Örneğin 80 veya hepsi için 'hepsi'): ")
if hedef_port.lower() == 'hepsi':
    sniff(prn=paket_yakala)
else:
    sniff(filter=f"tcp port {hedef_port}", prn=paket_yakala)
