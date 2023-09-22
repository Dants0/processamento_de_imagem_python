import numpy as np
import imutils
import cv2

img = cv2.imread('star.jpg')
cv2.imshow("Original", img)
proporcao = 100.0 / img.shape[1]
tamanho_novo = (100, int(img.shape[0] * proporcao))
img_redimensionada = cv2.resize(img, tamanho_novo,
interpolation = cv2.INTER_AREA)
cv2.imshow("Imagem redimensionada", img_redimensionada)
cv2.waitKey(0)
