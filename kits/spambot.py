import time
import pyautogui
zaman = float(input("Kaç saniye sonra yazsın? "))
kere = int(input("Kaç kere yazsın? "))
yazidosyasi = input("Metin dosyası ismi ve uzantısını giriniz:")
spamaraligi = float(input("Yazılar arası kaç saniye beklensin? (varsayılan:0) "))
if spamaraligi == "": spamaraligi=0
okuma = open(yazidosyasi, 'r')
time.sleep(zaman)
for word in okuma:
	for i in range(0,kere):
		pyautogui.typewrite(word)
		pyautogui.press('enter')
		time.sleep(spamaraligi)
