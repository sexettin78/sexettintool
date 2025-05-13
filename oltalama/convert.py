import base64
import os

def base64_to_image(base64_string, output_dir="oltalama/images"):
    """Base64 kodlu string'i resim dosyasına dönüştürür."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    try:
        image_data = base64.b64decode(base64_string.split(',')[1]) 
        filename = os.path.join(output_dir, f"image_{len(os.listdir(output_dir))}.png") 
        with open(filename, 'wb') as f:
            f.write(image_data)
        print(f"Resim {filename} olarak kaydedildi.")
        return filename
    except Exception as e:
        print(f"Hata: {e}")
        return None

def process_base64_file(filename="oltalama/base64_images.txt"):
  """Belirtilen dosyadaki base64 verilerini resimlere dönüştürür."""
  try:
      with open(filename, 'r') as f:
          for line in f:
              base64_to_image(line.strip()) 
  except FileNotFoundError:
      print(f"Hata: {filename} dosyası bulunamadı.")

process_base64_file()