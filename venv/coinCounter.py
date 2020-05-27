# import libraries
import matplotlib.pyplot as plt
import numpy as np
import cv2

# cargado de imagen
img = cv2.imread("coin2.jpeg")

img2 = image.open("coin2.jpeg")

# obtenemos la anchura y altura
width, height = img2.size

im2 = img2.resize((width/2, height/2), Image.NEAREST)
im3 = img2.resize((width/2, height/2), Image.BILINEAR)
im4 = img2.resize((width/2, height/2), Image.BICUBIC)
im5 = img2.resize((width/2, height/2), Image.ANTIALIAS)
cv2.imshow("grey scale", im2)


# # conversion a grises
# grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # limpieza de ruido
# blurred = cv2.GaussianBlur(grey, (17, 17), 0)
#
# # cv2.imshow("grey scale", grey)
# # cv2.imshow("blurred", blurred)
# # cv2.waitKey(0)
#
# # Deteccion de bordes con metodo canny
# outline = cv2.Canny(blurred, 30, 150)
#
# # show canny edge detector
# # cv2.imshow("The edges", outline)
# # cv2.waitKey(0)
#
#
# # Deteccion de contornos
# (cnts, _) = cv2.findContours(outline, cv2.RETR_EXTERNAL,
#             cv2.CHAIN_APPROX_SIMPLE)
#
# # dibujado de contornos
# cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
#
# fuente = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
# cv2.putText(img,text="Monedas detectadas: %i" % len(cnts), org=(20,100), fontFace=fuente, fontScale=3, color=(0,255,0), thickness=4, lineType=cv2.LINE_8)
#
# cv2.imshow("Result", img)
# cv2.waitKey(0)
#
# # Cantidad de monedas encontradas
# # print("Monedas detectadas: %i" % len(cnts))

