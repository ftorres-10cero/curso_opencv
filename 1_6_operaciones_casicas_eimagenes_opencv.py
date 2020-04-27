# Seccion 1, Lección 5
# Operaciones Básicas en Imágenes en OpcenCV con Python

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("logo.jpg")

#cv2.imshow('image',img)
#cv2.waitKey(0)

#print(img)

# Obteniendo los colores del pixel BGR
px = img[200,200]
print(px)

# Obtenemos el color azul
blue = img[200,200,0]
print(blue)

# Incluimos un punto rojo Opción menos eficiente
img[200,200] = [0,0,255]

# Accedemos a la coordenada del valor rojo
red = img.item(10,10,2)
print(red)


# Modificamos el nivel del rojo
img.itemset((10,10,2),0)
red = img.item(10,10,2)
print(red)

# Accedemos a la información de la imagen  (ANCHO, ALTO y NUMERO DE CANALES)

print(img.shape)

# Accedemos al tamaño de la imagen  (ANCHO X ALTO X CANALES)
print(img.size)

# Accedemos al tipo de datos de la imagen
print(img.dtype)

# separacion de canales Opción: más costosa
b1,g1,r1 = cv2.split(img)

# O mediante canales independientes: menos costosa
b2 = img[:,:,0]
g2 = img[:,:,1]
g2 = img[:,:,2]


cv2.imshow('image',b1)
cv2.waitKey(0)

cv2.imshow('image',g1)
cv2.waitKey(0)

cv2.imshow('image',r1)
cv2.waitKey(0)


img[:,:,2] = 255

r3 = img[:,:,2]

img1 = cv2.merge((b1,g1,r3))

cv2.imshow('image',img1)
cv2.waitKey(0)


#uso de bordes con distintos tipos
BLUE = [0,0,255]  # Matploblib es RGB en lugar de BGR
replicate = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_CONSTANT,value=BLUE)

# Mostramos todos los resultados
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()