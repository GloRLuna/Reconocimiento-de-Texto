import cv2
import pytesseract
from translate import Translator
import time
import sys

# Inicializar la cámara
cap = cv2.VideoCapture(0)



while True:

    print("Iniciando en:")
    for i in range(5, 0, -1):
        sys.stdout.write(str(i) + "\r")
        sys.stdout.flush()
        time.sleep(1)

    # Leer una imagen de la cámara
    ret, img = cap.read()
   
    # Utilizar Tesseract para reconocer el texto en la imagen
    text = pytesseract.image_to_string(img)
    print("Texto detectado:", text)
   
    # Utilizar Google Translate para traducir el texto
    translator = Translator(to_lang="es")
    translation = translator.translate(text)
    print("Traducción:", translation)
   
    # Guardar la traducción en un archivo de texto
    with open("translation.txt", "w") as f:
        f.write(translation)
   
    # Mostrar la imagen original con el texto reconocido superpuesto
    cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Imagen", img)
   
    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()