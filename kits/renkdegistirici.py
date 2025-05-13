import cv2
import numpy as np

def hex_to_bgra(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 8:  
        return [int(hex_color[i:i+2], 16) for i in (4, 2, 0, 6)]  # BGRA formatına çevir
    return [int(hex_color[i:i+2], 16) for i in (4, 2, 0)] + [255]  # Varsayılan alfa 255 (tam opak)

def replace_color(image_path, color_to_replace_hex, new_color_hex, tolerance=30):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        print("Görüntü yüklenemedi!")
        return None
    
    if image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    
  
    color_to_replace = np.array(hex_to_bgra(color_to_replace_hex), dtype=np.uint8)
    new_color = np.array(hex_to_bgra(new_color_hex), dtype=np.uint8)
    
    lower_bound = np.array([max(0, c - tolerance) for c in color_to_replace[:3]] + [0], dtype=np.uint8)
    upper_bound = np.array([min(255, c + tolerance) for c in color_to_replace[:3]] + [255], dtype=np.uint8)
    

    mask = cv2.inRange(image[:, :, :3], lower_bound[:3], upper_bound[:3])

    new_image = image.copy()
    new_image[mask > 0] = new_color
    
    return new_image

input_image = input("Görüntü yolu: ")
print("Transparan için #00000000 yazınız.")
target_color_hex = input("Değiştirilecek renk (HEX): ")   
replacement_color_hex = input("Yerine konulacak renk (HEX): ")  
outputfile = input("Oluşturulacak dosya adı (örn: output.png): ")

output = replace_color(input_image, target_color_hex, replacement_color_hex)
if output is not None:
    cv2.imwrite(outputfile, output)
    cv2.imshow("Result", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
