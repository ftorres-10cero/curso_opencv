# Seccion 1, Lección 7
# Operaciones Aritméticas en Imágenes OpcenCV con Python

import cv2
# cargamos 2 imagenes
img1 = cv2.imread('dst.png')
img2 = cv2.imread('aprenderpython.png')

# cv2.imshow('res',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# cv2.imshow('res',img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Yo quiero poner el logo en el corner izquierdo y por eso creo un ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# cv2.imshow('res',roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Ahora creo una máscara de logotipo y hago su máscara inversa también
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# cv2.imshow('res',img2gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

ret, mask = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# cv2.imshow('res',mask_inv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Recortamos el inverso de la mascara del logotiopola al logotipo
img2_bg = cv2.bitwise_and(img2,img2,mask = mask_inv)

# cv2.imshow('res',img2_bg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Recortamos la máscara en el fondo
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)


# cv2.imshow('res',img1_bg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Sumamos ambas imágenes

img1_img2 = cv2.add(img1_bg,img2_bg)

# cv2.imshow('res',img1_img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Tome solamente la región del logotipo de la imagen del logotipo
# img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# cv2.imshow('res',img2_fg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Ponga el logotipo en ROI y modifique la imagen principal
#dst = cv2.add(img1_bg,img1_bg)





# Sutituimos el recuadro que contiene el logo en la imagen principal
img1[0:rows, 0:cols ] = img1_img2


cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()





# Recortamos la máscara inversa en el fondo
img1_bg_logo = cv2.bitwise_and(roi,roi,mask = mask_inv)

img1_img2 = cv2.addWeighted(roi,1,img2_bg,0.2,0)


# Sutituimos el recuadro que contiene el logo en la imagen principal
img1[0:rows, 0:cols ] = img1_img2


cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()