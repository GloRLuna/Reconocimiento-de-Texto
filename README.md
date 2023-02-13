# Proyecto de Inteligencia Artificial

Haciendo uso de OCR (Reconocimiento Óptico de Caracteres) y con la biblioteca translate,
en conjunto con Tesseract se diseño un código para reconocer el texto y traducirlo.

Se encuentran los códigos de prueba de OCR.py, que reconoce el texto y superpone en tiempo
real los carácteres detectados

El código Prueba.py reconoce el texto en ingles y lo traduce a español en tiempo real. La
imagen del video tarda varios segundos en aparecer (usando Raspberry Pi 4B - 2GB) y muestra
el resultado de la traducción anterior.

La presición del reconocimiento de texto en tiempo real no es fiable, los resultados obtenidos
varian dependiendo de la  calidad de la cámara utilizada, la luz del entorno, el tipo y tamaño
de la letra del texto. En caso de querer reconocer texto escrito a mano se recomienda que esté
escrito con pluma o plumón.

El código traduccion.py reconoce el idioma ya sea en español o inglés y lo traduce según corresponda
al otro idioma. Primero reconoce el texto, después detecta el idioma, procede a traducirlo y luego
y por último guarda la traducción en un archivo de texto. No funciona en tiempo real. Para que se 
guarde correctamente la traducción se recomienda terminar el proceso después de terminar cada 
traducción.
