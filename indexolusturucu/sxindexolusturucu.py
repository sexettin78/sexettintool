import time
dosya = open("index.html","a")

print("İstediğinizi boş bırakabilirsiniz.")
title = input("Sayfa Başlığı: ")
backresim = input("Arkaplan resminin linki: ")
yazi1 = input("Yazılacak Başlık: ")
yazi2 = input("Yazılacak Yazı: ")
print("UYARI! BAŞLIK VE YAZI RENGİNİ İNGİLİZCE YAZIN VEYA RENK KODU KULLANIN MESELA #00FFFF GİBİ")
renkyazi1 = input("Başlık Rengi: ")
renkyazi2 = input("Yazı Rengi: ")
print("Font büyüklüğünü rakam ile giriniz 9 ideal")
fontbuyuk1 = input("Başlığın font büyüklüğü: ")
fontbuyuk2 = input("Yazının font büyüklüğü: ")
istek1 = input("Font stillerini bilmiyorsanız,font stillerine ve ne iş yaptıklarına bakmak ister misiniz? e/h ")
if(istek1=="h" or istek1=="H"):
	fontstil1 = input("Başlığın font stili: ")
	fontstil2 = input("Yazının font stili: ")
elif(istek1=="e" or istek1=="E"):
	fontdosya = open("indexolusturucu/fontlar.txt")
	print(fontdosya.read())
	time.sleep(4)
	fontstil1 = input("Başlığın font stili: ")
	fontstil2 = input("Yazının font stili: ")
else:
	fontstil1 = input("Başlığın font stili: ")
	fontstil2 = input("Yazının font stili: ")
dosya.write('''<html> 
<head>
<meta charset="utf-8">
<title>'''+title+'''</title>
</head>
<body>
<br>
    <style>
        html { 
              background: url('''+backresim+''') no-repeat center center fixed; 
              -webkit-background-size: cover;
              -moz-background-size: cover;
              -o-background-size: cover;
              background-size: cover;
        }
        
        p{
            font-size: 20px;
            color: whitesmoke;
            
        }
        h1{
            font-size: 35px;
            color: whitesmoke;
        }
    
    
    </style>
<br>

<center>
<font color="'''+renkyazi1+'''" size="'''+fontbuyuk1+'''" face="'''+fontstil1+'''">'''+yazi1+'''</font>

</center> <br> <br>
<center>

<font color="'''+renkyazi2+'''" size="'''+fontbuyuk2+'''" face="'''+fontstil2+'''">'''+yazi2+'''</font>

</center>
</body>
</html>''')