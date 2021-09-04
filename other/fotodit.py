import cv2
import numpy as np

print('''\033[94m 

FotoDit'e Hoşgeldiniz!

1-Resmi yeniden boyutlandır

2-Resmi gri yap

3-Resim buğulaştır

4-Çiziliresim

''')
kernel = np.ones((5,5),np.uint8)
secim = input("Seçiminizi yapınız: ")
resimsec = input("Resim yolunu giriniz: ")
resim = cv2.imread(resimsec)
if secim=="1":
    width,height = 800,800
    #width = input("Genişlik giriniz: ")
    #height = input("Yükseklik giriniz: ")
    imgres = cv2.resize(resim,(width,height))
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad+".jpg",resim)

elif secim=="2":
    imggray = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad+".jpg",imggray)

elif secim=="3":
    #bugu = input("bugu seviyesi giriniz örneğin 5,5 : ") 
    imgbugu = cv2.GaussianBlur(resim,(5,5),5)
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad+".jpg",imgbugu)

elif secim=="4":
    imgbugu = cv2.GaussianBlur(resim,(5,5),5)
    imgcanny = cv2.Canny(imgbugu,100,100)
    resimad = input("Oluşacak resim adını giriniz: ")
    cv2.imwrite(resimad+".jpg",imgcanny)
    













    
