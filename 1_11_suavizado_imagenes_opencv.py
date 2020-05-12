# Seccion 1, Lección 11
# Suavizando Imágenes con OpenCV

# Aplicar filtros personalizados a imágenes (convolución 2D)..
# cv2.filter2D()



import cv2
import numpy as np
from matplotlib import pyplot as plt

# Convolución 2D (Filtrado de imágenes)

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('nadal.jpg')

#Crea el kernel
kernel = np.ones((5,5),np.float32)/25

#Filtra la imagen utilizando el kernel anterior
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Promediada')
plt.xticks([]), plt.yticks([])

plt.show()

# Promedio

img = cv2.imread('nadal.jpg')

blur = cv2.blur(img,(3,3))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Difuminada promedio')
plt.xticks([]), plt.yticks([])
plt.show()


# Filtro Gaussiano


img = cv2.imread('nadal.jpg')

blur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Difuminada Gaussiano')
plt.xticks([]), plt.yticks([])
plt.show()


# Filtro de Mediana

img = cv2.imread('nadal.jpg')

median = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Difuminada Mediana')
plt.xticks([]), plt.yticks([])
plt.show()
