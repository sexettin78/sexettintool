import os
print("""\033[34m

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢠⡾⠃⠀⠀⠀⠀⠀⠀⠰⣶⡀⠀⠀
 1-) Port Tara ⠀⢠⡿⠁⣴⠇⠀⠀⠀⠀⠸⣦⠈⢿⡄⠀
⠀2-) Saldır ⠀⠀⠀ ⣾⡇⢸⡏⢰⡇⠀⠀⢸⡆⢸⡆⢸⡇⠀
⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢹⡇⠘⣧⡈⠃⢰⡆⠘⢁⣼⠁⣸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠈⢿⣄⠘⠃⠀⢸⡇⠀⠘⠁⣰⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠙⠃⠀⠀⢸⡇⠀⠀⠘⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀3-) Port Kılavuzu⠀⠀ ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀4-) Nasıl Kullanılır ⠘⠃⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⣟⠉⢻⡟⠉⢻⡟⠉⣻⣿⣿⣿BLUE COUGH⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣷⣿⣿⣶⣿⣿⣾⣿⣿⣿⣿ SEXETTIN ⣿⣿⣿⡇⠀
⠀⠈⠉⠉⢉⣉⣉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣉⣉⡉⠉⠉⠁⠀
⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀

""")
blue_cough_secim = input("Seçiminizi giriniz:")
blue_cough_portlar = '''
Port 1: RFCOMM (Radio Frequency Communication) üzerinden genel amaçlı seri port emülasyonu için kullanılır. Bu port, Bluetooth cihazları arasında seri veri aktarımı sağlamak amacıyla kullanılır. Özellikle, eski cihazlar, endüstriyel ekipmanlar ve çeşitli Bluetooth geliştirme veya test uygulamaları için uygundur. Seri port iletişimi gereken durumlarda, cihazlar arasında kablosuz bir bağlantı kurmak için kullanılır.
Port 2: Headset Gateway servisi, genellikle kulaklıklar ve hoparlörler için kullanılır.
Port 3: Handsfree Gateway servisi, araç kitleri veya eller serbest cihazlar için kullanılır.
Port 25: Advanced Audio servisi, müzik yayını ve sesli içerikler için kullanılır.
Port 23: AV Remote Control Target servisi, sesli cihazları veya medya oynatıcıları uzaktan kumanda etmek için kullanılır.
Port 15: Android Network Access Point ve Android Network User servisleri, cihazın internet bağlantısını paylaşmak veya bir PAN (Personal Area Network) ağı kurmak için kullanılır.
Port 12: OBEX Object Push, genellikle dosya gönderimi için kullanılır.
Port 19: OBEX Phonebook Access Server servisi, telefon rehberine erişim sağlamak için kullanılır.
Port 26: SMS/MMS servisi, SMS ve MMS mesajlarını işlemek için kullanılır.

Eğer bir port üzerinden saldırı başarısız olursa farklı portlar üzerinden deneyiniz.
'''

kullanim_kilavuzu_blue = '''
Eğer Windows makinenizde pybluez kütüphanesini indiremiyorsanız 
ilk önce https://git-scm.com/downloads adresinden git'i indirip
daha sonra pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez
komutunu kullanınız. 
Cihazınızın bluetooth servisini açıp port taramaya başlayın. Sonrasında saldır
seçeneğine girip saldırı yapacağınız cihazın adresini giriniz. Tarama sonucunda
elde ettiğiniz port numaraları üzerinden işlem yapınız.
Araç içindeki tüm sorumluluk size aittir.  
'''

if blue_cough_secim == "1":
    os.system("python3 blue-cough/listele.py")
elif blue_cough_secim =="2":
    os.system("python3 blue-cough/saldir.py")
elif blue_cough_secim =="3":
    print(blue_cough_portlar)
elif blue_cough_secim =="4":
    print(kullanim_kilavuzu_blue)
else:
    print("Hatalı seçim yaptınız")