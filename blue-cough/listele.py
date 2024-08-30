import bluetooth

def discover_devices():
    print("Tarama yapılıyor...")
    devices = bluetooth.discover_devices(lookup_names=True, lookup_class=False)

    if devices:
        print(f"Bulunan {len(devices)} cihazlar:")
        for addr, name in devices:
            print(f"  {name} - {addr}")
            services = bluetooth.find_service(address=addr)
            if services:
                print(f"    {name} üzerindeki servisler:")
                for svc in services:
                    print(f"      Servis ismi: {svc['name']}, Port: {svc['port']}")
            else:
                print(f"    {name}.")
    else:
        print("Cihaz bulunamadı")

discover_devices()
