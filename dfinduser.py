import os
srum = open("surum.txt")
surum = srum.read()

print("""

0-)Ana Menü
1-)Taramaya Başla

""")
secim = input("Seçiminizi giriniz: ")
if(secim=="0"):
	os.system("python3 sexettintoolsv"+surum+".py")
elif(secim=="1"):
	try:
		import requests
		import time
	except:
		os.system("pip install -r requirements.txt")
	hesapbul = input("\033[93mKullanıcı Adı Giriniz > ")
	print("")
	time.sleep(1)
	print("Hesap mevcut ise link yeşil renkte, hesap yoksa link kırmızı renktedir.Bazı durumlarda siteler robotları engellemek için olmayan hesapları mevcut şeklinde gösterebilir.Twitter,Reddit,Spotify,Steam'de böyle şeylerle karşılaşabilirsiniz.")

	print("")
	x = requests.get("https://www.instagram.com/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://www.instagram.com/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://www.instagram.com/"+hesapbul)
		time.sleep(4)

	print("")
	x = requests.get("https://www.twitter.com/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://www.twitter.com/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://www.twitter.com/"+hesapbul)
		time.sleep(4)
	print("")

	x = requests.get("https://www.youtube.com/c/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://www.youtube.com/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://www.youtube.com/"+hesapbul)
		time.sleep(4)


	print("")

	x = requests.get("https://"+hesapbul+".blogspot.com")
	if(x.status_code==200):
		print("\033[92mhttps://"+hesapbul+".blogspot.com")
		time.sleep(4)
	else:
		print("\033[91mhttps://"+hesapbul+".blogspot.com")
		time.sleep(4)


	print("")
	x = requests.get("https://www.reddit.com/user/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://www.reddit.com/user/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://www.reddit.com/user/"+hesapbul)
		time.sleep(4)

	print("")

	x = requests.get("https://www.github.com/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://www.github.com/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://www.github.com/"+hesapbul)
		time.sleep(4)
	print("")

	x = requests.get("https://steamcommunity.com/id/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://steamcommunity.com/id/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://steamcommunity.com/id/"+hesapbul)
		time.sleep(4)
	print("")

	x = requests.get("https://vk.com/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://vk.com/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://vk.com/"+hesapbul)
		time.sleep(4)
	print("")

	x = requests.get("https://open.spotify.com/user/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://open.spotify.com/user/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://open.spotify.com/user/"+hesapbul)
		time.sleep(4)
	print("")

	x = requests.get("https://www.wattpad.com/user/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://www.wattpad.com/user/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://www.wattpad.com/user/"+hesapbul)
		time.sleep(4)
	print("")

	x = requests.get("https://"+hesapbul+".wordpress.com")
	if(x.status_code==200):
		print("\033[92mhttps://"+hesapbul+".wordpress.com")
		time.sleep(4)
	else:
		print("\033[91mhttps://"+hesapbul+".wordpress.com")
		time.sleep(4)
	print("")

	x = requests.get("https://www.pinterest.com/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://www.pinterest.com/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://www.pinterest.com/"+hesapbul)
		time.sleep(4)
	print("")

	x = requests.get("https://"+hesapbul+".tumblr.com")
	if(x.status_code==200):
		print("\033[92mhttps://"+hesapbul+".tumblr.com")
		time.sleep(4)
	else:
		print("\033[91mhttps://"+hesapbul+".tumblr.com")
		time.sleep(4)

	print("")

	x = requests.get("https://www.flickr.com/people/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://www.flickr.com/people/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://www.flickr.com/people/"+hesapbul)
		time.sleep(4)
	print("")

	x = requests.get("https://soundcloud.com/"+hesapbul)
	if(x.status_code==200):
		print("\033[92mhttps://soundcloud.com/"+hesapbul)
		time.sleep(4)
	else:
		print("\033[91mhttps://soundcloud.com/"+hesapbul)
		time.sleep(4)
	print("")
	os.system("python3 dfinduser.py")