# Seccion 1, Lección 3
# Empezando con imágenes

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Cargamos la imagen del disco duro
imagen = cv2.imread("logo.jpg")

# Load an color image in grayscale
flag_color = 1    # Imagen en color
flag_bw = 0    # Imagen en escala de grises
flag_original = -1   # Imagen original

img_color = cv2.imread("logo.jpg",flag_color)
img_bw = cv2.imread("logo.jpg",flag_bw)

# Creamos dos ventanas con dos modalidades distintas
cv2.imshow("image_coloe", img_color)
cv2.imshow("image_bw", img_bw)

# Esperamos evento de teclado
cv2.waitKey(0)

# Destruir todas las ventanas
cv2.destroyAllWindows()


# Creamos la ventana y despues incluimos la imagen
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.waitKey(0)
cv2.imshow('image',img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Guardamos la imagen en escala de grises en formato PNG
cv2.imwrite('deepgris.png',img_bw)


# Incluimos Condiciones para guardar una imagen

img = cv2.imread('logo.jpg',0)
cv2.imshow('image',img)

k = cv2.waitKey(0) & 0xFF
# Si pulsamos la tecla ESC salimos
if k == 27:
  cv2.destroyAllWindows()

# Si pulsamos la tecla s guardamos y salimos
elif k == ord('s'):
  cv2.imwrite('deepgray.jpg',img)
  cv2.destroyAllWindows()


# Uso de MatplotLib (https://matplotlib.org/)

img = cv2.imread('logo.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()