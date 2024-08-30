import os
print('''\033[92m

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣶⣤⣀⣀⣤⣶⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀1-) Telegram Kullanıcı Adından
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀	  Mesaj Çek
⠀⣾⣷⣶⣶⣶⣦⣤⠀⢤⣤⣈⣉⠙⠛⠛⠋⣉⣁⣤⡤⠀⣤⣴⣶⣶⣶⣾⣷⠀ 
⠀⠈⠻⢿⣿⣿⣿⣿⣶⣤⣄⣉⣉⣉⣛⣛⣉⣉⣉⣠⣤⣶⣿⣿⣿⣿⡿⠟⠁⠀2-) Telegram Id Üzerinden Mesaj Çek
⠀⠀⠀⠀⠀⠉⠙⠛⠛⠿⠿⠿⢿⣿⣿⣿⣿⡿⠿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀3-) Whatsapp Dışa Aktarılan Sohbet 
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⠦⠄⢀⣠⡀⠠⣄⡀⠠⠴⣾⡿⠀⠀⠀⠀⠀⣀⡀⠀    Üzerinden Mesaj Çek
⠀⠀⠀⠀⠀⠀⠀⠀⢤⣤⣴⣾⣿⣿⣷⣤⣙⣿⣷⣦⣤⡤⠀⠴⠶⠟⠛⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠺⣷⣄⠀⠀⠀⠀⠀4-) Kullanım Kılavuzu
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣙⣛⣻⣿⣿⣿⡿⠃⠐⠿⠿⣾⣿⣷⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀Unutmayın! Telegram üzerinde böyle
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀uygulamaların ban riski vardır. 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Tüm sorumluluk size ait. Çok mesaj
			      çekmemeye çalışın. Dikkatli olun.
1. Seçenek hem direkt mesajlardaki hem de ortak gruplardaki mesajları çekerken
2. Seçenek bunlardan rastgele birini çekiyor. Tamamını da çekebilir. Eğer 2. seçenek
ile elde edemediğiniz veri varsa programı tekrar çalıştırın veya da mümkünse 1. seçenekten
ilerleyin.
''')
crawler_secim = input("Seçiminizi giriniz:")
if crawler_secim == "1":
	os.system("python3 crawler-x11/cx11-username.py")
elif crawler_secim == "2":
	os.system("python3 crawler-x11/cx11-id.py")
elif crawler_secim == "3":
	os.system("python3 crawler-x11/cx11-wp.py")
elif crawler_secim=="4":
	print('''Öncelikle https://my.telegram.org/ adresine girip oturum açın. 
Bir Desktop uygulaması oluşturun. İsmini siz belirleyebilirsiniz. Sonrasında size
verdiği api id, api hash değerlerini kayıt edin. Bu programı çalıştırın. 
Size verilen değerleri doğru bir şekilde girin. 
Hedefin kullanıcı adını veya da id numarasını girin. Id numarasını bilmiyorsanız
çeşitli botlarla kullanıcıların id numarasını öğrenebilirsiniz. Crawler otomatik olarak
hedef kullanıcının sizinle olan mesajlarını ve ortak gruptaki mesajlarını kayıt edecek.
Ban riskini unutmayınız.
''')
else:
	print("Hatalı seçim")
