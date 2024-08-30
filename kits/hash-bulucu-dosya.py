import hashlib

def calculate_file_hash(file_path, algorithm='sha256'):
    hash_function = None
    if algorithm == 'md5':
        hash_function = hashlib.md5()
    elif algorithm == 'sha1':
        hash_function = hashlib.sha1()
    elif algorithm == 'sha256':
        hash_function = hashlib.sha256()
    else:
        raise ValueError("Geçersiz algoritma. Sadece 'md5', 'sha1', veya 'sha256' kullanabilirsiniz.")
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hash_function.update(chunk)
    
    return hash_function.hexdigest()
file_path = input("Hash almak istediğiniz dosyanın yolunu giriniz: ")
print("Virustotal genellikle sha256 algoritmasını kullanır")
algorithm = input("Kullanmak istediğiniz hash algoritmasını yazınız ('md5', 'sha1', 'sha256'): ").lower()
try:
    file_hash = calculate_file_hash(file_path, algorithm)
    print(f"Dosya hash ({algorithm}): {file_hash}")
except Exception as e:
    print(f"Hata: {e}")
