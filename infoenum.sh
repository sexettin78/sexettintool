#!/bin/bash

echo "Sistem Bilgileri"
echo "---------------------"
uname -a
cat /etc/*release
arch
hostname
hostnamectl

echo -e "\nKullanıcı Bilgileri"
echo "---------------------"
whoami
id
groups
lastlog | grep -v "**Never logged in**"

echo -e "\nAg Bilgileri"
echo "---------------------"
ip a
ip r
ss -tulnp
cat /etc/resolv.conf

echo -e "\nSSH Anahtarları"
echo "---------------------"
find /home /root -name "id_rsa" 2>/dev/null

echo -e "\nCron Joblar"
echo "---------------------"
cat /etc/crontab
ls -la /etc/cron.*

echo -e "\nOrtam Değişkenleri"
echo "---------------------"
env

echo -e "\nİşlem Bilgileri"
echo "---------------------"
ps aux | head -n 15

echo -e "\nGeçmiş ve Bash Kayıtları"
echo "---------------------"
cat ~/.bash_history 2>/dev/null
cat /root/.bash_history 2>/dev/null

echo -e "\nKurulu Paketler (Cikis islemi icin q tusuna basiniz)"
echo "---------------------"
if command -v dpkg > /dev/null; then
    dpkg -l
elif command -v rpm > /dev/null; then
    rpm -qa
fi

echo -e "\nSudo Yetkileri"
echo "---------------------"
sudo -l 2>/dev/null

echo -e "\nİlginc Dosyalar"
echo "---------------------"
echo "NOT: BU KISIM BIRAZ UZUN SUREBILIR, BU YUZDEN BURASI SONA KOYULDU."
echo "EGER YUKSEK YETKILI DOSYALARI OGRENMEK ISTEMIYORSANIZ PROGRAMI SONLANDIRABİLİRSİNİZ."
find / -name "*.bak" -o -name "*.old" -o -name "*.swp" 2>/dev/null
find / -perm -4000 -type f 2>/dev/null   # SUID dosyaları
find / -perm -2000 -type f 2>/dev/null   # SGID dosyaları


echo -e "Kesif tamamlandı."
