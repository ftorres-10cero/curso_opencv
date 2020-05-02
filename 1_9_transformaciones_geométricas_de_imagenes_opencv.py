# Seccion 1, Lección 9
# Transformaciones geométricas de imágene

# Aprender a aplicar diferentes transformaciones geométricas a imágenes, tales como: traslación, rotación, transformación afín, etc.
#
# Utilizar las funciones cv2.getPerspectiveTransform.
#
# cv2.warpAffine
# cv2.warpPerspective
# cv2.resize()   //cv2.INTER_AREA  / cv2.INTER_CUBIC / cv2.INTER_LINEAR *


import numpy as np
import cv2

img = cv2.imread('aprenderpython.png')

# REDIMENSIÓN

#Indicando el factor de escala
res1 = cv2.resize(img,None,fx=1.5, fy=1.5, interpolation = cv2.INTER_LINEAR)

# Indicando manualmente el nuevo tamaño deseado de la iamgen
height, width = img.shape[:2]
res2 = cv2.resize(img,(int(1.5*width), int(1.5*height)), interpolation = cv2.INTER_CUBIC)

# cv2.imshow('lineal',res1)
# cv2.imshow('cubica',res2)
#
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()

# TRASLACIÓN

import cv2
import numpy as np

img = cv2.imread('aprenderpython.png',0)
rows,cols = img.shape

M = np.float32([[1,0,210],[0,1,20]])  # Matriz de desplazamiento x = +210px y = + 20px
dst = cv2.warpAffine(img,M,(cols*2,rows*2))

# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ROTACIÓN


img = cv2.imread('cuadricula.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1) # Rotación de 45º

print(M)

dst = cv2.warpAffine(img,M,(cols,rows))

# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# TRANSFORMACIÓN AFÍN

import numpy as np
import matplotlib.pyplot as plt #carga la librería para graficar
import cv2

img = cv2.imread('cuadricula.jpg')
rows,cols,ch = img.shape

pts_origen = np.float32([[100,400],[400,100],[100,100]])
pts_destino = np.float32([[50,300],[400,200],[80,150]])


M = cv2.getAffineTransform(pts_origen,pts_destino)
dst = cv2.warpAffine(img,M,(cols,rows))

# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()


# TRANSFORMACIÓN DE PERSPECTIVA

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('sudoku.png')
rows,cols,ch = img.shape

pts_origen = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts_destino = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts_origen,pts_destino)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()