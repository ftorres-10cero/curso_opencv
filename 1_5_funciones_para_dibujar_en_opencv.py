# Seccion 1, Lección 5
# Funciones para dibujar en OpenCV

import numpy as np
import cv2

# Crea una imagen en negro
img = np.zeros((512,512,3), np.uint8)

# Dibuja una línea horizontal verde con un grosor de 2 px cruzando la mitad de la ventana
img = cv2.line(img,(0,255),(511,255),(0,255,0),2)

# Dibuja un rectangulo relleno centrado en la parte inferior
img = cv2.rectangle(img,(210,360),(300,500),(200,100,100),-1)

# Dibuja una elipse
img = cv2.ellipse(img,(255,105),(100,100),0,0,240,(255,150,150),-1)

#Dibujando un polígono
pts = np.array([[180,120],[330,120],[255,140]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

#Incluyendo texto
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'DRAWING',(40,90), font, 3,(255,255,255),2,cv2.LINE_AA)

# Mostrar la imagen
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()