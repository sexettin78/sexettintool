import re
from email import message_from_string
from email.utils import parsedate_to_datetime

def extract_received_headers(raw):
    return re.findall(r"^Received: (.+)", raw, re.MULTILINE)

def extract_ip_addresses(received_headers):
    ip_regex = re.compile(r'\[?(\d{1,3}(?:\.\d{1,3}){3})\]?')
    ips = []
    for header in received_headers:
        found = ip_regex.findall(header)
        if found:
            ips.extend(found)
    return list(set(ips))

def detect_mail_service(from_address):
    if not from_address:
        return "Bilinmiyor"

    lower = from_address.lower()
    if "gmail.com" in lower:
        return "Gmail"
    elif "outlook.com" in lower or "hotmail.com" in lower or "live.com" in lower:
        return "Outlook / Microsoft"
    elif "yahoo.com" in lower:
        return "Yahoo"
    elif "icloud.com" in lower or "me.com" in lower:
        return "Apple Mail / iCloud"
    elif "zoho.com" in lower:
        return "Zoho Mail"
    elif "protonmail.com" in lower:
        return "ProtonMail"
    elif "yandex.com" in lower:
        return "Yandex"
    else:
        return "Özel / Kurumsal Mail Servisi"

def analyze_email_header(raw_header):
    msg = message_from_string(raw_header)

    print("\n=== E-Posta Başlık Analizi ===\n")

    print(f"Konu: {msg.get('Subject')}")
    print(f"Kimden: {msg.get('From')}")
    print(f"Kime: {msg.get('To')}")
    print(f"Mesaj ID: {msg.get('Message-ID')}")

    try:
        date_obj = parsedate_to_datetime(msg.get('Date'))
        print(f"Gönderim Tarihi: {date_obj} ({date_obj.tzinfo})")
    except:
        print(f"Gönderim Tarihi: {msg.get('Date')}")

    print(f"MIME Türü: {msg.get_content_type()}")
    print(f"MIME Sürümü: {msg.get('MIME-Version')}")
    print(f"Boundary: {msg.get_boundary()}")

    user_agent = msg.get('User-Agent') or msg.get('X-Mailer')
    if user_agent:
        print(f"Kullanıcı Aracı: {user_agent}")

    encoding = msg.get("Content-Transfer-Encoding")
    if encoding:
        print(f"İçerik Kodlaması: {encoding}")
        if encoding.lower() in ["base64", "quoted-printable"]:
            print("Kodlanmış içerik tespit edildi.")

    service = detect_mail_service(msg.get('From'))
    print(f"Kullanılan Mail Servisi: {service}")

    references = msg.get("References")
    in_reply_to = msg.get("In-Reply-To")
    if references or in_reply_to:
        print("\nE-Posta Zinciri:")
        if references:
            print(f"  Referanslar: {references}")
        if in_reply_to:
            print(f"  Cevaplanan: {in_reply_to}")

    received_headers = extract_received_headers(raw_header)
    if received_headers:
        print("\nGeçiş Kayıtları (Received Headers):")
        for i, header in enumerate(received_headers, 1):
            print(f"  {i}. {header.strip()}")

        ips = extract_ip_addresses(received_headers)
        if ips:
            print("\nIP Adresleri:")
            for ip in ips:
                print(f"  - {ip}")

    print("\nAnaliz tamamlandı.\n")

if __name__ == "__main__":
    path = input("Analiz edilecek başlık dosyasının yolu: ").strip()

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            analyze_email_header(content)
    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except Exception as e:
        print(f"Hata: {e}")
