import time
import pyautogui
print("\nYAZI DOSYASINI DEĞİŞTİRMEYİ UNUTMAYIN!!! (nano spambotyazi.txt)")
zaman = int(input("Kaç saniye sonra yazsın? "))
kere = int(input("Kaç kere yazsın? "))
time.sleep(zaman)
okuma = open('spambotyazi.txt', 'r')
for word in okuma:
	for i in range(1,kere):
		pyautogui.typewrite(word)
		pyautogui.press('enter')
