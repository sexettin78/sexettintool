import sys
import PyPDF2
import os

def extract_metadata(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        metadata = reader.metadata
        print("\nMetadata:")
        if metadata:
            for key, value in metadata.items():
                print(f"{key}: {value}")
        else:
            print("Metadata bulunamadı.")

def extract_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print("\nÇıkarılan yazılar:")
        for i, page in enumerate(reader.pages):
            print(f"\n--- Sayfa {i+1} ---")
            text = page.extract_text()
            print(text if text else "Yazı algılanamadı.")
print("""1 - Pdf Dosyası Veri Analizi
2 - Pdf Dosyasından Metadata Verilerini Sil
""")
secim = int(input("Seçiminizi giriniz:"))
pdf_path = input("Pdf dosyasının yolunu giriniz:")
if(secim==1):
	if not os.path.exists(pdf_path):
    		print("Hata: Dosya bulunamadı.")
	else:
    		extract_metadata(pdf_path)
    		extract_text(pdf_path)
elif(secim==2):
    if not os.path.exists(pdf_path):
        print("Hata: Dosya bulunamadı.")
    else:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.add_metadata({})
            output_path = pdf_path.replace(".pdf", "_temiz.pdf")
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

            print(f"Metadata temizlendi. Yeni dosya: {output_path}")
else:
	print("Hatalı giriş")