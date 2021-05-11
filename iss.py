from __future__ import unicode_literals	
from pytube import YouTube
from moviepy.editor import *
import os
import youtube_dl
os.system("figlet Sexettin Tool")
print('''

1-) Videodan müziğe dönüştürücü

2-) Müzik indirici

3-) Video indirici

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

