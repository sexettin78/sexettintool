def get_font_info():
    return {
        "Arial": "Temiz ve okunması kolay bir sans-serif font. Genellikle metin ve başlıklar için kullanılır.",
        "Verdana": "Ekran üzerinde okunabilirliği yüksek bir sans-serif font. Özellikle web metinleri için idealdir.",
        "Georgia": "Klasik serif bir font. Yüksek kaliteli metinler ve başlıklar için uygundur.",
        "Times New Roman": "Serif bir font, genellikle akademik ve resmi belgelerde kullanılır.",
        "Tahoma": "Düz bir sans-serif font. Kullanıcı arayüzlerinde tercih edilir.",
        "Courier New": "Monospace bir font. Kod yazımı ve teknik belgeler için uygundur."
    }

def get_user_input():
    dosya_ismi = input("Oluşturulacak HTML dosyasının ismi (örneğin, 'index.html'): ")
    
    title = input("Sayfa Başlığı: ")
    backresim = input("Arkaplan resminin linki: ")
    yazi1 = input("Yazılacak Başlık: ")
    yazi2 = input("Yazılacak Yazı: ")
    print("UYARI! BAŞLIK VE YAZI RENGİNİ İNGİLİZCE YAZIN VEYA RENK KODU KULLANIN MESELA #00FFFF GİBİ")
    renkyazi1 = input("Başlık Rengi: ")
    renkyazi2 = input("Yazı Rengi: ")
    print("Font büyüklüğünü rakam ile giriniz, 30 ideal")
    fontbuyuk1 = input("Başlığın font büyüklüğü: ")
    fontbuyuk2 = input("Yazının font büyüklüğü: ")

    uyarı_isteği = input("Uyarı vermek ister misiniz? (e/h): ")
    if uyarı_isteği.lower() == 'e':
        uyarı_mesajı = input("Uyarı mesajını giriniz: ")
    else:
        uyarı_mesajı = None

    istek1 = input("Font stillerini bilmiyorsanız, font stillerine ve ne iş yaptıklarına bakmak ister misiniz? (e/h) ")
    if istek1.lower() == 'h':
        fontstil1 = input("Başlığın font stili: ")
        fontstil2 = input("Yazının font stili: ")
    elif istek1.lower() == 'e':
        font_info = get_font_info()
        print("Kullanabileceğiniz fontlar ve açıklamaları:")
        for font, description in font_info.items():
            print(f"{font}: {description}")
        fontstil1 = input("Başlığın font stili: ")
        fontstil2 = input("Yazının font stili: ")
    else:
        fontstil1 = input("Başlığın font stili: ")
        fontstil2 = input("Yazının font stili: ")

    return dosya_ismi, title, backresim, yazi1, yazi2, renkyazi1, renkyazi2, fontbuyuk1, fontbuyuk2, fontstil1, fontstil2, uyarı_mesajı

def generate_html(dosya_ismi, title, backresim, yazi1, yazi2, renkyazi1, renkyazi2, fontbuyuk1, fontbuyuk2, fontstil1, fontstil2, uyarı_mesajı):
    uyarı_script = ""
    if uyarı_mesajı:
        uyarı_script = f'''
        <script>
            alert("{uyarı_mesajı}");
        </script>
        '''
    
    return f'''
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="description" content="{title}">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: url('{backresim}') no-repeat center center fixed;
            background-size: cover;
            color: #fff;
            overflow-x: hidden;
        }}
        .container {{
            text-align: center;
            padding: 20px;
            background: rgba(0, 0, 0, 0.6); 
            border-radius: 15px;
            margin: 20px auto;
            max-width: 800px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }}
        h1 {{
            font-size: {fontbuyuk1}px;
            color: {renkyazi1};
            font-family: {fontstil1};
        }}
        p {{
            font-size: {fontbuyuk2}px;
            color: {renkyazi2};
            font-family: {fontstil2};
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{yazi1}</h1>
        <p>{yazi2}</p>
    </div>
    {uyarı_script}
</body>
</html>
'''

def create_html_file(dosya_ismi, html_content):
    with open(dosya_ismi, "w") as dosya:
        dosya.write(html_content)

def main():
    dosya_ismi, title, backresim, yazi1, yazi2, renkyazi1, renkyazi2, fontbuyuk1, fontbuyuk2, fontstil1, fontstil2, uyarı_mesajı = get_user_input()
    html_content = generate_html(dosya_ismi, title, backresim, yazi1, yazi2, renkyazi1, renkyazi2, fontbuyuk1, fontbuyuk2, fontstil1, fontstil2, uyarı_mesajı)
    create_html_file(dosya_ismi, html_content)
    print(f"Web sitesi {dosya_ismi} ismiyle başarıyla oluşturuldu")

if __name__ == "__main__":
    main()
