import bluetooth
import time

def connect_device(address, attempts, port=1, retry_delay=2):
    retry_delay = int(input("Bağlantılar arası bekleme süresi giriniz (ideal 2):"))
    for attempt in range(1, attempts + 1):
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            print(f"Deneme {attempt}: {address} adresine {port} portundan bağlantı kurulmaya başlandı...")
            sock.connect((address, port))
            print(f"Deneme {attempt}: {address} adresine bağlantı başarılı!")
            time.sleep(retry_delay) 
            break  
        except bluetooth.btcommon.BluetoothError as err:
            print(f"Deneme {attempt}: Bağlantı başarısız {err}")
        except Exception as ex:
            print(f"Deneme {attempt}: Tanımlanamayan hata {ex}")
        finally:
            sock.close()
            print(f"Deneme {attempt}: Bağlantı kesildi.\n")

        time.sleep(retry_delay)
print("Cihaz adresini öğrenmek için tarama programını çalıştırabilirsiniz.")
device_address = input("Bluetooth cihaz adresini giriniz:")
num_attempts = int(input("Kaç bağlantı isteği gönderilsin:"))
print("Hangi port numarasını gireceğinizi bilmiyorsanız ana menüden 'nasıl kullanılır?' seçeneğini seçiniz.")
port_num = int(input("Port numarası giriniz:"))
connect_device(device_address, num_attempts, port_num)
