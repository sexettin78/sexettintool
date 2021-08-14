from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.utils import find_connectable_ip

print('''

instagram bota hoşgeldiniz sürümv1
Seçenekler;

1-) Takip ettir

2-) Takipten çıkar

''')

secim = input("Seçiminizi yazınız > ")
takipkontrol = 0

if(secim=="1"):
    kadi = input("Takip edilecek kullanıcı adını giriniz > ")
    takipkontrol=1
elif(secim=="2"):
    kadi = input("Takipten çıkılacak kullanıcı adı giriniz > ")
    takipkontrol=2

okuma = input("Giriş yapılacak hesabın kullanıcı adı: ")
yazima = input("Giriş yapılacak hesabın şifresi: ")
driver_path = input("Selenium Web Driver yolunu belirtiniz \ yerine \\ yazınız > ")
browser = webdriver.Chrome(executable_path=driver_path)
browser.get("https://instagram.com/")
time.sleep(4)
kullanici = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
sifre = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
kullanici.send_keys(yazima)
sifre.send_keys(okuma)
browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
time.sleep(4)
browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
time.sleep(4)
browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
time.sleep(3)
if(takipkontrol==1):
    browser.get("https://instagram.com/"+kadi)
    time.sleep(5)
    browser.find_element_by_xpath("//button[contains(text(),'Takip Et')]").click()    
elif(takipkontrol==2):
    browser.get("https://instagram.com/"+kadi)
    time.sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button/div/span").click()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
time.sleep(5)
browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()
time.sleep(3)
browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div").click()
time.sleep(5)
browser.close

