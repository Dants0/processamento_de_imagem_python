import numpy as np
import cv2
imagem = cv2.imread('start.jpg')
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'OpenCV',(15,65), fonte,
2,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("Ponte", imagem)
cv2.waitKey(0)

#crop image 

cropped_image = imagem[110:500, 100:200]

cv2.imshow('Imagem cortada', cropped_image)
cv2.imwrite("imagemRecortada.jpg", cropped_image)