import requests
print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠷⠶⢤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⣿⡿⠟⠋⠉⠀⠀⠀⠀⣠⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⡅⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣄⠀⣴⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀	Referans url adresleri: 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀	https://<project-id>.firebaseio.com/
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀	https://<project-id>-default-rtdb.firebaseio.com/
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⡿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣇⠘⢿⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⢻⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉""")
def fetch_firebase_data(url):
    if not url.endswith(".json"): 
        url += ".json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Hata: {e}")
        return None

firebase_url = input("URL > ")
if(firebase_url[len(firebase_url)-1] != "/"): 
	firebase_url+="/"
dosyakaydet = input("Veriler dosyaya kayıt edilsin mi? (e/h): ")
dosyaadi = "freaper.txt"
if dosyakaydet == "e" or dosyakaydet == "E":
	dosyaadi = input("Dosya adı giriniz:")
	
data = fetch_firebase_data(firebase_url)

if data:    
    import json
    if dosyakaydet == "e" or dosyakaydet == "E":
    	dosya = open(dosyaadi, "a")
    	dosya.write(json.dumps(data, indent=4, ensure_ascii=False))
    	dosya.close()
    print(json.dumps(data, indent=4, ensure_ascii=False))  