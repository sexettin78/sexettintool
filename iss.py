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

4-) Python dosyasını exe formatına dönüştür

5-) Dosya indirici

6-) Terminalde müzik aç

7-) Ana menüye dön

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
	import yt_dlp
	video_url = input("YouTube video URL'sini girin: ")
	download_path = input("Müziği nereye indirmek istersiniz? (varsayılan olarak mevcut dizin): ")
	if not download_path:
		download_path = '.'
	ydl_opts = {
		'outtmpl': f'{download_path}/%(title)s.%(ext)s',  
		'format': 'bestaudio/best',                       
		'postprocessors': [{                            
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
			}],
		'postprocessor_args': [
			'-ar', '16000' 
		],
	}

	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			print("İndiriliyor...")
			ydl.download([video_url])
		print("İndirme ve dönüştürme tamamlandı!")
	except Exception as e:
		print(f"Hata: {e}")


elif(iss=="3"):
	import yt_dlp
	video_url = input("YouTube video URL'sini girin: ")
	download_path = input("Videoyu nereye indirmek istersiniz? (varsayılan olarak mevcut dizin): ")
	if not download_path:
		download_path = '.'
	ydl_opts = {
		'outtmpl': f'{download_path}/%(title)s.%(ext)s', 
		'format': 'bestvideo+bestaudio/best',  
	}
	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			print("İndiriliyor...")
			ydl.download([video_url])
			print("İndirme tamamlandı!")

	except Exception as e:
		print(f"Hata: {e}")



elif(iss=="4"):
	exesec = input("Tek dosya mı birden fazla dosya mı olsun? 1 veya 2 > ")
	if(exesec=="1"):
		import os
		os.system("pip install pyinstaller")
		projeadi = input("Python dosyasının yolunu belirtiniz > ")
		os.system("pyinstaller --onefile "+projeadi)
	elif(exesec=="2"):
		import os
		os.system("pip install pyinstaller")
		projeadi = input("Python dosyasının yolunu belirtiniz > ")
		os.system("pyinstaller "+projeadi)
	else:
		print("Sadece 1 veya 2 seçenekleri mevcuttur.")
		os.system("python3 iss.py")

elif(iss=="5"):
	import urllib.request
	print("\n Dosya adını istediğiniz gibi belirleyebilirsiniz. Dosya uzantısı, indireceğiniz dosya uzantısı ile aynı olmak zorundadır. Bulunduğu dizine indirir\n")
	dosya_linki = input("Dosya linkini giriniz >")
	dosya_adi = input("Dosya adını uzantısı ile beraber giriniz > ")
	urllib.request.urlretrieve(dosya_linki, dosya_adi)
	print("Dosya başarıyla indirildi")

elif(iss=="6"):
	print("Müziği durdurmak için ctrl+c tuş kombinasyonuna basınız. Ayrıca hata alırsanız Metfora üzerinden tam kurulum yapınız.")
	mzk = input("Müzik Yolu Giriniz > ")
	os.system("mpv --no-video "+mzk)
elif(iss=="7"):
	os.system("python3 sexettintoolsv"+surum+".py")
else:
	print("Hatalı seçim. Programı tekrar başlatıyorum \n")
	os.system("python3 iss.py")
