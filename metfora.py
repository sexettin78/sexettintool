import os
print("\033[95m")
os.system("clear")
srum = open("surum.txt")
surum = srum.read()
print('''
                   /|_
                  /   |_
                 /     /     __  __      _    __                 	
                /      >    |  \/  | ___| |_ / _| ___  _ __ __ _ 	
               (      >	    | |\/| |/ _ \ __| |_ / _ \| '__/ _` |
              /      /	    | |  | |  __/ |_|  _| (_) | | | (_| |
             /     /	    |_|  |_|\___|\__|_|  \___/|_|  \__,_|
            /      /
         __/      \_____   Yaptığınız ve yapacağınız herşeyden siz sorumlusunuz
        /'             |	 hiçbir şekilde sorumluluk kabul edilmez.
         /     /-\     /
        /      /  \--/	    1-) Kullanımı göster
       /     /
      /      /		    2-) Toola geri dön 
     (      >
    /      >		    3-) İletişim
   /     _|
  /  __/		    4-) Bu dizine Toolu yükle
 /_/
			    5-) Bu dizinden Toolu sil

			    6-) Tam kurulum (bazı durumlarda kök kullanıcı gerektirir)

			    7-) Toolu güncelle

''')

metfora = input("Hangisini seçiyorsunuz? ")

if(metfora=="1"):
	print('''
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
13. derleme aracıdır py_compile kütüphanesini kullanır,eğer dosyalarınızın içinin açılmasını istemiyorsanız kullanabilirsiniz derlenen dosya çalışır ama içi açılmaz kaynak kodlarına bakılmaz
##############################
14.tool veritabanı çalma aracıdır site ile ilgili bildiklerinizi seçtikten ve doldurduktan sonra işlemleri başlatır sqlmap kullanır  
##############################
15 YERALTI
	|
	|--- 1.Kaç tane isterseniz o kadar nitro üretir şansınıza bağlıdır random üretir
	|
	|--- 2.Size güçlü bir şifre oluşturur
	|
	|--- 3.Size,sizin verdiğiniz haneler ile şifre oluşturur
	|
	|--- 4.Kaç tane isterseniz o kadar play kod üretir şansınıza bağlıdır random üretir
	|
	|--- 5.Kaç tane isterseniz o kadar pubg uc kodu üretir şansınıza bağlıdır random üretir
	|
	|--- 6.Kaç tane isterseniz o kadar pubg uc kodu üretir şansınıza bağlıdır random üretir
	|
	|--- 7.Kaç tane isterseniz o kadar pubg uc kodu üretir şansınıza bağlıdır random üretir
	|
	|--- 8.Kaç tane isterseniz o kadar pubg uc kodu üretir şansınıza bağlıdır random üretir
	|
	|--- 9.Kaç tane isterseniz o kadar pubg uc kodu üretir şansınıza bağlıdır random üretir
	|
	|--- 10.Yazdığınız kullanıcı adını linkler ile bağdaştırır 
	|
	|--- 11.İlk 9 hanesini yazdığınız t¢nin tam halini atar elinize geçen t¢yi doğrulamak için kullanılabilir
	|
	|--- 12.Yazdığınız numaraya yazdığınız mesajı anonim bir numaradan atar çalışmaz ise iletişime geçebilirsiniz
	|
	|--- 13.Telefon numarasından konum bulur amerika numaralarında felan kullanabilirsiniz
	|
	|--- 14.Panelsiz fake email verir istediğiniz sitelerde kullanabilirsiniz
	|
	|--- 15.Admin panelin olabileceği linkler verir
	|
	|--- 16.Yazdığınız yazıyı verdiğiniz süre sonra kaç kere istediyseniz o kadar gönderir

##############################
16.tool kaba kuvvet saldırısı yani brute force yapmaya yarar hydra kullanır
##############################
17.md5 şifrelemeye yarar yazdığınız sözcüğü md5 olarak şifreler
##############################
18.Dos ve ddos saldırısı yapmanıza yarar python ile kodlandı
##############################
19.hedef sitenin kaynak kodunu çeker python ile kodlandı
##############################
20 İş görür
   |
   |-- 1-) Hedef videoyu müziğe çevirir örneğin /home/sexettin/a.mp4 ü a.mp3 yapar
   |
   |-- 2-) Urlsini verdiğiniz müziği,toolun bulunduğu dizine kaydeder 
   |
   |-- 3-) Urlsini verdiğiniz videoyu,toolun bulunduğu dizine kaydeder
   
##############################
21.handshake decrypter aircrack-ng kullanarak şifre çözmeye çalışır
##############################
22.Elinizdeki md5'i,elinizdeki wordlist ile kırmaya çalışır
##############################
23.directory fuzzer, verdiğiniz url ve belirttiğiniz dizin ile güvenlik açığı yakalamak için kullanılır
##############################
Metfora işinizi kolaylaştıracak yapay zekadır toolu kurmak için silmek için hataları gidermek için vb. kullanabilirsiniz
##############################

''')


elif(metfora=="2"):
	os.system("clear")
	os.system("python3 sexettintoolsv"+surum+".py")
elif(metfora=="3"):
	print('''

Telegram = @furkande
Discord = Sexettin#3146
Telegram genel kanal = t.me/sexettin
Instagram = Sexettin

	''')

elif(metfora=="4"):
	os.system("cd ..")
	os.system("git clone https://github.com/sexettin78/sexettintool.git")
elif(metfora=="5"):
	print("\033[91mBu dizindeki Tool ve ilgili herşey kaldırılacak")
	sec = input("Kaldırmak istediğinize emin misiniz? y/n ")
	if(sec=="y"):
		os.system("rm -rf sexettintoolsv2.py")
		os.system("rm -rf sexettintoolsv3.py")
		os.system("rm -rf sexettintoolsv4.py")
		os.system("rm -rf sexettintoolv5.py")
		os.system("rm -rf sexettintoolv6.py")
		os.system("rm -rf sexettintoolv7.py")
		os.system("cd ..")
		os.system("rm -rf sexettintool")
	elif(sec=="n"):
		os.system("python3 sexettintoolsv6.py")

elif(metfora=="7"):
	os.system("git pull")
	os.system("git fetch")
elif(metfora=="6"):
	os.system("apt install python")
	os.system("apt install python2")
	os.system("apt install python3")
	os.system("pkg install python")
	os.system("pkg install python2")
	os.system("pkg install python3")
	os.system("pkg install figlet")
	os.system("pkg install crunch")
	os.system("pip install pyinstaller")
	os.system("pkg install git")
	os.system("pip install requests")
	os.system("pip install phonenumbers")
	os.system("apt install figlet")
	os.system("apt install hydra")
	os.system("pip install youtube-dl")
	os.system("pip install pygeocoder")
	os.system("pip install moviepy")
	os.system("pip install pytube")
	os.system("apt update")
	os.system("pip install pynput")
	os.system("pip install pyautogui")
	os.system("pip install pyzipper")
	os.system("pip install ngrok")
	os.system("sudo apt install mpv")
	os.system("apt install php")
	os.system("apt-get update")
	os.system("pip install selenium")
	os.system("pip install opencv-python")
	os.system("pip install beautifulsoup4")
