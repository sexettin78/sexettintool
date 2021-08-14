import os
notdosya = open("xsnot.txt","a")
print('''\033[94m
          ,,aadd8888888ba,
       .o8P""'         `""Y8o.
     .88"'       _____     `"88.
   .dP'        /~ /   ~\      `Yb.	Merhaba! Not Defteri uygulamasına hoşgeldiniz!
  .8P        j' f ,   ~/'       "8.
 .8"         |\  d   7'          "8.	Seçenekler:
.8|          |   H  /|            |8
o8           | \`H / |             8b
88           |   H / |             8)	1-)Not Ekle
88           | \ N   |             8)
88           |\ `H / |            .8P	2-)Notları Oku
Y8            \  H' /             o8'
`8|             \H/              a8'	3-)Notları Temizle
 `8o             H              a8'
   Yb.           H            .od'	 
    "8o          V          .dP'
      "V8o,,.          ,,od8"
         ``""YY8888888PP""'
''')
notsecim = input("Hangisini Seçiyorsunuz > ")
if(notsecim=="1"):
	notyaz = input("Notunuzu Yazınız > ")
	notdosya.write(notyaz+" \n")
	print("\033[92mNot Ekleme Başarılı")
elif(notsecim=="2"):
	yazilmis = open("xsnot.txt")	
	print("İşte Notlar: \n")
	print("\033[1m")
	print(yazilmis.read())
elif(notsecim=="3"):
	sil = input("Gerçekten tüm notları silmek istiyor musunuz? e/h ")
	if(sil=="e"):
		notiki = open("xsnot.txt","w+")
		notiki.write(" ")
		print("\033[92mNotlar Temizlendi")
	elif(sil=="h"):
		print("İşlem iptal edildi.")
	else:
		print("İşlem iptal edildi.")
else:
	print("\033[91mYanlış seçim,program tekrar başlatılıyor...")
	os.system("python3 xsnot.py")

