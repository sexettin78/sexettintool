from __future__ import unicode_literals	
from pytube import YouTube
from moviepy.editor import *
import os
import urllib.request
import youtube_dl
os.system("clear")
print("\033[92m")
os.system("figlet Sexettin Tool")
srum = open("surum.txt")
surum = srum.read()
print("\033[96m")
print('''
                    _,;_;/-",_
                 ,")  (  ((O) "  .`,
               ,` (    )  ;  -.,/;`}
             ,"  o    (  ( (  . -_-.
            `.  ;      ;  ) ) \`; \;
              `., )   (  ( _-`   \,'
                 "`'-,,`.jb

1-) Videodan müziğe dönüştürücü

2-) Müzik indirici

3-) Video indirici

4-) Python dosyasını exe dosyasına dönüştür

5-) Dosya indirici

6-) Terminalde müzik aç

7-) Anamenüye dön

''')
iss = input("Hangisini seçiyorsun? ")

if(iss=="1"):
	import os
	os.system("pip install moviepy")
	mp4_file = input("Video yolunu giriniz: ")
	mp3_file = input("Müzik adını giriniz sonuna .mp3 ekleyerek: ")
	videoClip = VideoFileClip(mp4_file)
	audioclip = videoClip.audio
	audioclip.write_audiofile(mp3_file)
	audioclip.close()
	videoClip.close()


elif(iss=="2"):

	os.system("pip install youtube-dl")
	print("Linki yapıştırın")
	link = input ("")
	ydl_opts = {
	    'format': 'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '320',
	    }],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([link])

elif(iss=="3"):

	import os
	os.system("pip install pytube")
	url = input("Urlyi yapıştırın ")
	video = YouTube(url)
	print("\n")

	print("----------------- BAŞLIK --------------------")
	print(" ")
	print("Video Adı: "+video.title)
	print(" ")
	print("----------------- THUMBNAIL --------------------")
	print(video.thumbnail_url)
	print("----------------- Akış --------------------")
	print(video.streams.all)
	print("----------------- VİDEO İNDİRİLİYOR --------------------")

	video.streams.first().download()
	print("Video indirildi")
	altyazi = input("Altyazıları okumak ister misiniz?")
	if(altyazi=="y"):
		print("----------TÜRKÇE-----------")
		caption = video.captions.get_by_language_code('tr')
		print(caption.generate_srt_captions())
		print("----------İNGİLİZCE-----------")
		caption = video.captions.get_by_language_code('en')
		print(caption.generate_srt_captions())

elif(iss=="4"):
	exesec = input("Tek Dosya mı Birden fazla dosya mı olsun? 1 veya 2 > ")
	if(exesec=="1"):
		import os
		os.system("pip install pyinstaller")
		projeadi = input("Python Dosyasının yolunu belirtiniz > ")
		os.system("pyinstaller --onefile "+projeadi)
	elif(exesec=="2"):
		import os
		os.system("pip install pyinstaller")
		projeadi = input("Python Dosyasının yolunu belirtiniz > ")
		os.system("pyinstaller "+projeadi)
	else:
		print("Sadece 1 veya 2 yazacaksın")
		os.system("python3 iss.py")

elif(iss=="5"):
	import urllib.request
	print("\n Dosya adını istediğiniz gibi belirleyebilirsiniz.Dosya uzantısı,indireceğiniz dosya uzantısı ile aynı olmak zorundadır.Bulunduğu dizine indirir\n")
	dosya_linki = input("Dosya linkini giriniz >")
	dosya_adi = input("Dosya adını uzantısı ile beraber giriniz > ")
	urllib.request.urlretrieve(dosya_linki, dosya_adi)

elif(iss=="6"):
	print("Müziği durdurmak için ctrl+c  ayrıca hata alırsanız metforadan tam kurulum yapın")
	mzk = input("Müzik Yolu Giriniz > ")
	os.system("mpv --no-video "+mzk)
elif(iss=="7"):
	os.system("python3 sexettintoolsv"+surum+".py")
else:
	print("Hatalı seçim.Programı tekrar başlatıyorum \n")
	os.system("python3 iss.py")
