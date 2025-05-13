import os
import time
import stat
import pwd
import mimetypes
import hashlib
import datetime
import math

def get_hashes(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
    print("\033[92m============HASH VERİLERİ============")
    print("MD5:", hashlib.md5(data).hexdigest())
    print("SHA1:", hashlib.sha1(data).hexdigest())
    print("SHA256:", hashlib.sha256(data).hexdigest())

def get_timestamps(path):
    stat_info = os.stat(path)
    try:
        creation_time = datetime.datetime.fromtimestamp(stat_info.st_birthtime).strftime('%Y-%m-%d %H:%M:%S')
    except AttributeError:
        creation_time = "\033[93mBilinmiyor (Bu platformda oluşturma zamanı desteklenmiyor)"
    print("\033[93m============ZAMAN VERİLERİ============")
    print("Oluşturma:", creation_time)
    print("Düzenleme:", time.ctime(stat_info.st_mtime))
    print("Erişim:", time.ctime(stat_info.st_atime))


def get_magic_type(path):
    with open(path, "rb") as f:
        header = f.read(16).hex().lower()
        if header.startswith("25504446"): return "PDF"
        elif header.startswith("504b0304"): return "ZIP veya DOCX/XLSX/PPTX"
        elif header.startswith("ffd8ffe0") or header.startswith("ffd8ffe1") or header.startswith("ffd8ffe8"): return "JPEG"
        elif header.startswith("89504e47"): return "PNG"
        elif header.startswith("47494638"): return "GIF"
        elif header.startswith("377abcaf"): return "7-Zip"
        elif header.startswith("52617221"): return "RAR"
        elif header.startswith("4d5a"): return "EXE veya DLL"
        elif header.startswith("494433"): return "MP3"
        elif header.startswith("0000001866747970"): return "MP4"
        elif header.startswith("49492a00") or header.startswith("4d4d002a"): return "TIFF"
        elif header.startswith("52494646"): return "AVI"
        elif header.startswith("000001ba"): return "MPEG"
        elif header.startswith("4f676753"): return "OGG" 
        elif header.startswith("57415645"): return "WAV"
        elif header.startswith("23212f2f"): return "Shebang (script dosyası - ilk satıra bakın)"
        elif header.startswith("424d"): return "BMP"
        elif header.startswith("00000100"): return "ICO"
        elif header.startswith("494e4458"): return "INDX (Microsoft Outlook Index)"  
        elif header.startswith("d0cf11e0a1b11ae1"): return "MSI (Microsoft Installer)"
        elif header.startswith("ac97df0777ae"): return "DBF (dBase database file)"
        elif header.startswith("4344303031"): return "ISO (ISO-9660 CD/DVD image)"
        elif header.startswith("7b5c72746631"): return "RTF (Rich Text Format)"
        elif header.startswith("53514c697465"): return "SQLite database"
        elif header.startswith("efbbbf"): return "UTF-8 encoded text (BOM ile)" 
        elif header.startswith("feff"): return "UTF-16 encoded text (BOM ile)"  
        elif header.startswith("fffe"): return "UTF-16 encoded text (BOM ile)"  
        elif header.startswith("1f8b"): return "GZIP"
        elif header.startswith("1f9d"): return "Z (compress)"
        elif header.startswith("425a68"): return "Bzip2"
        elif header.startswith("fd377a585a00"): return "XZ"
        elif header.startswith("7801"): return "Zlib"
        elif header.startswith("789c"): return "Zlib (deflate)"
        elif header.startswith("78da"): return "Zlib (deflate)"
        elif header.startswith("7f454c46"): return "ELF (Executable and Linkable Format)"
        return "\033[91mBu dosya türü, sexettintool veri türü uzantılarında bulunamadı."



def get_permissions(path):
    st = os.stat(path)
    try:
        owner = pwd.getpwuid(st.st_uid).pw_name
    except KeyError:
        owner = st.st_uid
    print("\033[94m============İzin Verileri============")
    print("Sahip:", owner)
    print("İzinler:", stat.filemode(st.st_mode))
    print("inode:", st.st_ino)
    print("Hard link sayısı:", st.st_nlink)



def get_size(filepath):
    size_bytes = os.path.getsize(filepath)
    if size_bytes == 0:
        return "0 bytes"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    print("\033[95m============Boyut Verileri============")
    print("Dosya Boyutu:","%s %s" % (s, size_name[i]))



def analyze_file(filepath):
    print("\033[96m============Dosya Yolu============")
    print("Dosya Yolu:", filepath)
    print()
    get_hashes(filepath)
    print()
    get_timestamps(filepath)
    print()
    print("\033[91m============Dosya Türü============") 
    print("Magic Type:", get_magic_type(filepath)) 
    print("Mime Type:", mimetypes.guess_type(filepath)[0])
    print()
    get_permissions(filepath)
    print()
    get_size(filepath)
    print("\033[0m") 


dosyayolu = input("Analiz edilecek dosya: ")
analyze_file(dosyayolu)



     
        

