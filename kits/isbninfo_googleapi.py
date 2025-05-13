import requests

def get_book_info(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)

    if response.status_code != 200:
        print("API isteği başarısız oldu.")
        return

    data = response.json()

    if data["totalItems"] == 0:
        print("Kitap bulunamadı.")
        return

    item = data["items"][0]
    info = item["volumeInfo"]
    sale = item.get("saleInfo", {})
    access = item.get("accessInfo", {})

    print("\nKİTAP BİLGİLERİ")
    print("-" * 50)
    print(f"Başlık: {info.get('title', 'Bilinmiyor')}")
    print(f"Yazar(lar): {', '.join(info.get('authors', ['Bilinmiyor']))}")
    print(f"Yayıncı: {info.get('publisher', 'Bilinmiyor')}")
    print(f"Yayın Tarihi: {info.get('publishedDate', 'Bilinmiyor')}")
    print(f"Sayfa Sayısı: {info.get('pageCount', 'Bilinmiyor')}")
    print(f"Kategoriler: {', '.join(info.get('categories', ['Yok']))}")
    print(f"Dil: {info.get('language', 'Bilinmiyor')}")
    print(f"Açıklama: {info.get('description', 'Yok')[:300]}...")

    print("\nSATIŞ BİLGİLERİ")
    print("-" * 50)
    if sale.get("saleability") == "FOR_SALE":
        price = sale.get("retailPrice", {})
        print(f"Fiyat: {price.get('amount', '?')} {price.get('currencyCode', '')}")
        print(f"Satın Al: {sale.get('buyLink')}")
    else:
        print("Satışta değil.")

    print("\nEK BAĞLANTILAR")
    print("-" * 50)
    print(f"Önizleme: {info.get('previewLink')}")
    print(f"Web Reader: {access.get('webReaderLink', 'Yok')}")
    print(f"Google Books Sayfası: {info.get('canonicalVolumeLink')}")


isbn = input("ISBN numarasını giriniz: ").strip()
get_book_info(isbn)
