from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, PeerUser, PeerChat, PeerChannel
import asyncio

api_id = input("Api id değerinizi giriniz: ")
api_hash = input("Api hash değerinizi giriniz: ")
phone_number = input("Telefon numaranızı ülke kodu ile beraber +90xxx şeklinde giriniz: ")
hedef_kadi = input("Mesajları çekilecek kişinin kullanıcı adı (başında @ olmadan): ")
mesaj_dosya = input("Mesajların kayıt edileceği dosyayı giriniz:")

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    me = await client.get_me()

    result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=200,
        hash=0
    ))
    
    target_username = hedef_kadi
    target_user = await client.get_entity(target_username)

    all_messages = []

    for dialog in result.dialogs:
        peer = dialog.peer
        if isinstance(peer, PeerUser) or isinstance(peer, PeerChat) or isinstance(peer, PeerChannel):
            try:
                async for message in client.iter_messages(peer, from_user=target_user):
                    all_messages.append(message.text)
            except:
                pass  
    
    with open(mesaj_dosya, 'a', encoding='utf-8') as f:
        for message in all_messages:
            f.write(f"{message}\n")

with client:
    client.loop.run_until_complete(main())
print("İşlem tamamlandı")
