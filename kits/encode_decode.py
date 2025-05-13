import base64
import binascii
import urllib.parse
import html

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58_encode(data: bytes) -> str:
    num = int.from_bytes(data, 'big')
    encode = ''
    while num > 0:
        num, rem = divmod(num, 58)
        encode = BASE58_ALPHABET[rem] + encode
    for byte in data:
        if byte == 0:
            encode = BASE58_ALPHABET[0] + encode
        else:
            break
    return encode

def base58_decode(data: str) -> bytes:
    num = 0
    for char in data:
        num *= 58
        num += BASE58_ALPHABET.index(char)
    return num.to_bytes((num.bit_length() + 7) // 8, 'big')

def encode_all(text: str):
    encoded_bytes = text.encode()

    print(f"\n[ENCODE] {text}")
    print(f"URL      : {urllib.parse.quote(text)}")
    print(f"HTML     : {html.escape(text)}")
    print(f"Base64   : {base64.b64encode(encoded_bytes).decode()}")
    print(f"Base58   : {base58_encode(encoded_bytes)}")
    print(f"ASCII    : {' '.join(str(ord(c)) for c in text)}")
    print(f"HEX      : {binascii.hexlify(encoded_bytes).decode()}")
    print(f"OCTAL    : {' '.join(oct(ord(c))[2:] for c in text)}")
    print(f"BINARY   : {' '.join(bin(ord(c))[2:].zfill(8) for c in text)}")

def decode_all(text: str):
    print(f"\n[DECODE] {text}")
    try:
        print(f"URL      : {urllib.parse.unquote(text)}")
    except: print("URL decode: HATA")

    try:
        print(f"HTML     : {html.unescape(text)}")
    except: print("HTML decode: HATA")

    try:
        print(f"Base64   : {base64.b64decode(text).decode()}")
    except: print("Base64 decode: HATA")

    try:
        print(f"Base58   : {base58_decode(text).decode()}")
    except: print("Base58 decode: HATA")

    try:
        print(f"HEX      : {binascii.unhexlify(text).decode()}")
    except: print("HEX decode: HATA")

    try:
        ascii_decoded = ''.join([chr(int(c)) for c in text.split()])
        print(f"ASCII    : {ascii_decoded}")
    except: print("ASCII decode: HATA")

    try:
        octal_decoded = ''.join([chr(int(c, 8)) for c in text.split()])
        print(f"OCTAL    : {octal_decoded}")
    except: print("OCTAL decode: HATA")

    try:
        binary_decoded = ''.join([chr(int(c, 2)) for c in text.split()])
        print(f"BINARY   : {binary_decoded}")
    except: print("BINARY decode: HATA")


print("""1 - Encode İşlemleri
2 - Decode İşlemleri""")
e_d_secim = int(input("Seçiminizi giriniz: "))
e_d_veri = input("Veri giriniz: ")
if e_d_secim == 1:
	encode_all(e_d_veri)
elif e_d_secim == 2:
    decode_all(e_d_veri)
else:
    print("Hatalı veri girişi")
