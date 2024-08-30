import cv2
import numpy as np

print('''\033[94m 

FotoDit'e Hoş Geldiniz!
Seçenekler:
1- Resmi yeniden boyutlandır
2- Resmi gri yap
3- Resim buğulaştır
4- Çizili resim
5- Resmi döndür
6- Resmi kes
7- Resmi aydınlat
8- Resmin kontrastını ayarla

''')
kernel = np.ones((5,5),np.uint8)
secim = input("Seçiminizi yapınız: ")
resimsec = input("Resim yolunu giriniz: ")
resim = cv2.imread(resimsec)
if secim=="1":
    width = int(input("Genişlik giriniz: "))
    height = int(input("Yükseklik giriniz: "))
    imgres = cv2.resize(resim, (width, height)) 
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad + ".jpg", imgres)
    print("Resim başarıyla oluşturuldu")

elif secim=="2":
    imggray = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad+".jpg",imggray)
    print("Resim başarıyla oluşturuldu")
    
elif secim=="3":
    bugu = int(input("Buğu seviyesi giriniz (1-9): "))
    imgbugu = cv2.GaussianBlur(resim,(bugu,bugu),5)
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad+".jpg",imgbugu)
    print("Resim başarıyla oluşturuldu")
    
elif secim=="4":
    imgbugu = cv2.GaussianBlur(resim,(5,5),5)
    imgcanny = cv2.Canny(imgbugu,100,100)
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad+".jpg",imgcanny)
    print("Resim başarıyla oluşturuldu")
    
elif secim == "5":
    angle = float(input("Döndürme açısını giriniz: "))
    (h, w) = resim.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    imgrot = cv2.warpAffine(resim, M, (w, h))
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad + ".jpg", imgrot)
    print("Resim başarıyla oluşturuldu")
    
elif secim == "6":
    x = int(input("Kestiğiniz bölgenin sol üst köşesinin x koordinatını giriniz: "))
    y = int(input("Kestiğiniz bölgenin sol üst köşesinin y koordinatını giriniz: "))
    w = int(input("Kestiğiniz bölgenin genişliğini giriniz: "))
    h = int(input("Kestiğiniz bölgenin yüksekliğini giriniz: "))
    imgcrop = resim[y:y+h, x:x+w]
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad + ".jpg", imgcrop)
    print("Resim başarıyla oluşturuldu")
    
elif secim == "7":
    beta = int(input("Aydınlatma miktarını giriniz (negatif değerler koyu, pozitif değerler aydınlık yapar): "))
    imgbright = cv2.convertScaleAbs(resim, alpha=1, beta=beta)
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad + ".jpg", imgbright)
    print("Resim başarıyla oluşturuldu")
    
elif secim == "8":
    alpha = float(input("Kontrast seviyesini giriniz (1.0 düz, 0.5 düşük, 1.5 yüksek vb.): "))
    imgcontrast = cv2.convertScaleAbs(resim, alpha=alpha, beta=0)
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad + ".jpg", imgcontrast)
    print("Resim başarıyla oluşturuldu")
    
else:
    print("Seçenek bulunamadı")

    
