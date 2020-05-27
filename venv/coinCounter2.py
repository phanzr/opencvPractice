# import libraries
import matplotlib.pyplot as plt
import numpy as np
import cv2

# cargado de imagen
img = cv2.imread("coin2.jpeg")

# conversion a grises
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# limpieza de ruido
blurred = cv2.GaussianBlur(grey, (17, 17), 0)

# cv2.imshow("grey scale", grey)
# cv2.imshow("blurred", blurred)
# cv2.waitKey(0)

# Deteccion de bordes con metodo canny
outline = cv2.Canny(blurred, 30, 150)

# show canny edge detector
# cv2.imshow("The edges", outline)
# cv2.waitKey(0)


# Deteccion de contornos
(cnts, _) = cv2.findContours(outline, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)

# dibujado de contornos
cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Result", img)
cv2.waitKey(0)

# Cantidad de monedas encontradas
print("Monedas detectadas: %i" % len(cnts))

