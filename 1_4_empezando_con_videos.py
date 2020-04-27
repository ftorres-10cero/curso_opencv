# Seccion 1, Lección 4
# Empezando con vídeos

import numpy as np
import cv2

input_file = "input.avi"
output_file = "output.avi"

frame_width = 640
frame_height = 480

frame_per_sec = 25.0


# Guardar un vídeo tras transformar

cap = cv2.VideoCapture(input_file)

# Define el codec y crea el objeto VideoWriter (http://www.fourcc.org/codecs.php)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#fourcc = cv2.VideoWriter_fourcc(*'MPG4')
out = cv2.VideoWriter(output_file, fourcc, frame_per_sec, (frame_width,frame_height))

while (cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:

    # Nuestras operaciones sobre los cuadros se hacen aqui
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Invertimos el frame
    frame_flip = cv2.flip(frame, 0)  # invierte el cuadro

    # Cambiamos tamaño al frame
    frame = cv2.resize(frame, (frame_width, frame_height))

    # escribe el cuadro invertido
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break

# Libera todo si la tarea ha terminado
cap.release()
out.release()
cv2.destroyAllWindows()