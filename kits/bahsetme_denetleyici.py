import asyncio
from telethon import TelegramClient, events
from datetime import datetime

print("Verilerinizi bahsetmeler.txt dosyasında bulabilirsiniz.")
api_id = input("Api id değerinizi giriniz: ")
api_hash = input("Api hash değerinizi giriniz: ")
client = TelegramClient("stn_tool", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def mention_listener(event):
    me = await client.get_me()
    if event.message.mentioned or f"@{me.username}" in event.raw_text:
        sender = await event.get_sender()
        ad = getattr(sender, "username", None) or f"{sender.first_name} {sender.last_name or ''}"
        simdi = datetime.now()
        saat = simdi.strftime("%H:%M:%S")
        tarih = simdi.strftime("%d.%m.%Y - %A")
        with open("bahsetmeler.txt", "a", encoding="utf-8") as f:
            f.write(f"{event.raw_text}  -->  {ad} - {saat} | {tarih}\n")

async def main():
    print("Mention dinleyici başlatıldı...")
    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())
