from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def instagram_login_and_action(username, password, action, target_user):
    service = Service(executable_path=driver_path)
    browser = webdriver.Chrome(service=service)
    wait = WebDriverWait(browser, 10)

    try:
        browser.get("https://instagram.com/")
        time.sleep(bekle)

        kullanici = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        sifre = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))

        kullanici.send_keys(username)
        sifre.send_keys(password)

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()
        time.sleep(bekle)

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Şimdi Değil')]"))).click()
            time.sleep(bekle)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Şimdi Değil')]"))).click()
            time.sleep(bekle)
        except:
            pass

        browser.get(f"https://instagram.com/{target_user}")
        time.sleep(bekle)

        if action == "follow":
            follow_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button")))
            follow_button.click()
            print(f"{username} kullanıcısı {target_user} kullanıcısını takip etti.")
        elif action == "unfollow":
            wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button/div/div[1]"))).click()
            time.sleep(bekle)
            wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div[1]/div/div"))).click()
            print(f"{username} kullanıcısı {target_user} kullanıcısını takipten çıktı.")
        
        time.sleep(bekle)
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div[3]/span/div/a/div/div[2]/div/div/span/span"))).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[6]/div[1]/div/div/div[1]/div/div"))).click()
    except Exception as e:
        print(f"{username} ile işlem yapılırken bir hata oluştu: {e}")
    finally:
        browser.quit()

print(r'''
       __
   _  |@@|
  / \ \--/ __
  ) O|----|  |   __
 / / \ }{ /\ )_ / _\
 )/  /\__/\ \__O (__
|/  (--/\--)    \__/
/   _)(  )(_
   `---''---`
Instagram bota hoş geldiniz. Sürüm: v2
Seçenekler:
1-) Takip ettir
2-) Takipten çıkar
3-) Nasıl kullanılır? (Bu seçeneği açarken soru soruyorsa 1 e basa basa geçiniz)
''')

secim = input("Seçiminizi yazınız > ")
print("Bekleme süresini arttırmak daha kesin sonuçlar verir fakat işlem süresini uzatır.")
bekle = int(input("İşlemler arası bekleme süresi giriniz (ideal 6): "))
driver_path = input("Selenium Web Driver yolunu belirtiniz \\ yerine \\\\ yazınız > ")

with open('hesaplar.txt', 'r+') as f:
    usernames = [line.strip() for line in f]

with open('sifreler.txt', 'r+') as f:
    passwords = [line.strip() for line in f]
if len(usernames) != len(passwords):
    print("Hesaplar ve şifreler dosyalarında eşit sayıda giriş bulunmalıdır.")
    exit()

target_user = input("İşlem yapılacak hedef kullanıcı adını giriniz > ")

for username, password in zip(usernames, passwords):
    try:
        if secim == "1":
            instagram_login_and_action(username, password, "follow", target_user)
        elif secim == "2":
            instagram_login_and_action(username, password, "unfollow", target_user)
        elif secim == "3":
            print("""Bu bot, art arda onlarca hesabınızdan istediğiniz hesabı takip etmek veya da takipten çıkmak için kullanılır.
Hesaplarınıza giriş yapar ve istediğiniz işlemi gerçekleştirir. Otomasyon projesidir.
Botu kullanmak için hesaplar.txt dosyasının adına alt alta hesap isimlerini,
sifreler.txt dosyasına ise bu hesapların şifrelerini yazınız. Örneğin a, b ve c adında 3 hesabınız varsa
ve bu hesapların şifreleri sırasıyla 1, 2 ve 3 ise hesaplar dosyasının içi:
a
b
c
Şifreler dosyasının içi:
1
2
3
Şeklinde olmalıdır.
Ekstra hiçbir şey yazmayınız. Unutmayın, hesabınıza çok fazla giriş yaparsanız ban yiyebilir. Bu yüzden dikkatli olunuz.
Yaptığınız işlemlerden, hesabınızda sorun çıkmasından veya da başınıza gelecek herhangi bir olaydan araç yapımcısı sorumlu değildir.
Tüm sorumluluklar size aittir.""")
        else:
            print("Geçersiz seçim!")
            break
    except Exception as e:
        print(f"{username} kullanıcısı için işlem yapılırken bir hata oluştu: {e}")
        continue 

print("İşlemler tamamlandı.")
