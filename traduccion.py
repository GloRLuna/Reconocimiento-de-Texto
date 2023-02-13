import cv2
import pytesseract
from pytesseract import Output
from translate import Translator
import langdetect
import sys
import time

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:

    # Leer una imagen de la cámara
    ret, img = cap.read()

    cv2.imshow("Preview", img)

    start = input("Presiona G para comenzar a traducir, cualquier otra tecla para salir: ")
    if start.upper() != "G":
        break
   
    # Utilizar Tesseract para reconocer el texto en la imagen
    text = pytesseract.image_to_string(img, lang="spa+en")
    print("Texto detectado:\n", text)
   
    # Utilizar Translate para detectar el idioma del texto
    detected_lang = langdetect.detect(text)
    print("Idioma Detectado:", detected_lang)

    # Utilizar Translate para traducir el texto
    translator_en = Translator(to_lang="en")
    translator_es = Translator(to_lang="spa")
    if detected_lang == "es":
        translation = translator_en.translate(text)
    elif detected_lang == "en":
        translation = translator_es.translate(text)
    else:
        translation = "No se pudo determinar el idioma del texto"
    print("Traducción:\n", translation)
    
    file_name = input("Ingrese el nombre bajo el que quiere guardar la traducción: ")

    # Guardar la traducción en un archivo de texto
    with open(file_name + ".txt", "w") as f:
        f.write(translation)
    
    cv2.destroyAllWindows()


# Liberar la cámara y cerrar las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()
