from telethon.sync import TelegramClient
from telethon.tl.types import User
import csv

print("Not: Program yalnızca direkt mesajlardaki (özel) sohbetleri analiz eder. Grup, kanal veya botlar dahil edilmez. Eğer son sohbetlerinizde hiç bireysel kullanıcı yoksa, hiçbir ID listelenmeyebilir. Bu nedenle sistem en fazla 50 sohbeti tarar ve içlerinden yalnızca gerçek kullanıcıları alır.\n")
api_id = input("Api id değerinizi giriniz: ")
api_hash = input("Api hash değerinizi giriniz: ")

kisisayisi = int(input("Son konuşulan kaç kişinin id numarası toplansın:"))
print("Örneğin son 5 sohbetinizde 3 kanal ve 2 insan var. Burada 5 kişinin verisini çekmek isterseniz yalnızca 2 insanın verisini çeker. Buna dikkat ederek sayı belirtiniz.")
client = TelegramClient('stn_tool', api_id, api_hash)

async def main():
    await client.start()

    dialogs = await client.get_dialogs(limit=30)
    ids = set()

    for dialog in dialogs:
        entity = dialog.entity
        if isinstance(entity, User) and not entity.bot and not entity.is_self:
            user_id = entity.id
            username = entity.username or "YOK"
            ids.add((user_id, username))

        if len(ids) >= kisisayisi:
            break

    with open("dm_kullanicilar.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Kullanıcı Adı", "ID"])
        for id, uname in ids:
            writer.writerow([uname, id])

    print(f"{len(ids)} kullanıcı kaydedildi → dm_kullanicilar.csv")

with client:
    client.loop.run_until_complete(main())
