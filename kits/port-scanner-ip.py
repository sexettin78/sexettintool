import socket

def port_scanner(ip, port_range):
    print(f"Ip taranıyor: {ip}, aralık: {port_range}")
    open_ports = []

    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"Port {port} açık")
            open_ports.append(port)
        sock.close()

    return open_ports

target_ip = input("Hedef ip adresini giriniz:")
port_range = range(1, 1025)  
open_ports = port_scanner(target_ip, port_range)
print(f"Açık portlar: {open_ports}")
