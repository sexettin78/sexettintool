import os
print('''\033[95m

⠀⢀⣤⣶⣾⣿⣿⣿⣿⣷⣶⣦⣀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣟⣻⣛⣿
⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏	1-) İnsan Kopyala 1
⠀⡇⠀⠀ ⠀⠀⠀
⠀⡇⠀⠀⠀ ⠀⠀        2-) İnsan Kopyala 2
⠀⡇ ⠀	⣠⣄⡀⠀ 
⠀⡇⠀ ⠀⡤⣒⡼⣿⣿⠇ ⠀⠀⠀ 3-) İnsan Modeli Yükle 1
⠀⡇⠀⠀⣼⣿⢿⡅
⠀⡇⠀⠸⣿⣿⣯⣷⣷⠀⠀⠀⠀⠀  4-) İnsan Modeli YÜkle 2
⠀⡇⠀⠀⠈⣩⣿⠗⠙⠁⠀⠀⠀⠀
⠀⡇⠀⠀⠘⣿⠋⠀⠀⠀⠀   	5-) Kullanım Kılavuzu
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⠀⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡀  Bu program, belirtilen kişinin mesajlarını
⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧  öğrenerek o kişinin bir kopyasını oluşturur.
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣶⣾⣶⣿  Örneğin bir insanın kopyasını oluşturup o kişi
gibi merhaba kelimesi ile cümle kurmasını isteyebilirsiniz.
Kişi hakkında yeterli veri toplamak için Crawler-x11 kullanabilirsiniz.
1. seçenekte hata alırsanız diye 2. seçenek eklendi.
''')
imitator_secim = input("Seçiminizi giriniz:")
if imitator_secim == "1":
	os.system("python3 imitator-x11/train-1.py")
elif imitator_secim == "2":
	os.system("python3 imitator-x11/train-2.py")
elif imitator_secim == "3":
	os.system("python3 imitator-x11/resume-1.py")
elif imitator_secim == "4":
	os.system("python3 imitator-x11/resume-2.py")
elif imitator_secim == "5":
	print("""
Programı çalıştırmak için tensorflow kütüphanesine sahip olmanız
gereklidir. Eğer Linux sanal makinenizde illegal hardware şeklinde
bir uyarı alıyorsanız ana makinenizde deneyiniz. 1. seçenek çalışmaz
ise daha gelişmiş olan 2. seçeneği seçiniz. Yapay zekanın epoch
değerini ortalama 60'da tutmanız önerilir. Düzgün bir klonlama için
oldukça fazla veriye ihtiyacınız olduğunu unutmayın. Programı yalnızca
izin aldığınız kişiler üzerinde kullanmaya dikkat edin. Tüm sorumluluk
size aittir.
""")
else:
	print("Hatalı seçim")