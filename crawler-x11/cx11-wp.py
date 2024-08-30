def filter_messages(file_path, username):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    filtered_messages = []

    for line in lines:
        if "Medya dahil edilmedi" in line:
            continue
        if f"{username}:" in line:
            parts = line.split(" - ", 1)
            if len(parts) > 1:
                msg_parts = parts[1].split(": ", 1)
                if len(msg_parts) > 1:
                    message = msg_parts[1]
                    filtered_messages.append(message.strip())

    return filtered_messages


file_path = input("Mesajların bulunduğu metin dosyasının konumunu ve uzantısını giriniz:")
username = input("Mesajları alınacak kişinin numarasını veya da kullanıcı adını giriniz:")
kayit_path = input("Verilerin kaydedileceği yeni dosyanın adını ve uzantısını giriniz:")
filtered_messages = filter_messages(file_path, username)
kayit_dosya = open(kayit_path,"a+",encoding="utf-8")
for msg in filtered_messages:
    kayit_dosya.write(msg)
    kayit_dosya.write("\n")
print("İşlem tamamlandı")
