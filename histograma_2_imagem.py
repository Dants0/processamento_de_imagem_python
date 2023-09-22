from matplotlib import pyplot as plt
import numpy as np
import cv2

# img = cv2.imread('star.jpg')
img = cv2.imread('yoda.png')
cv2.imshow("Imagem Colorida", img)

# Separa os canais
canais = cv2.split(img)
cores = ("b", "g", "r")

plt.figure()
plt.title("Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")

for (canal, cor) in zip(canais, cores):
    # Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, color=cor)
    plt.xlim([0, 256])

# Movendo plt.show() e cv2.waitKey(0) para fora do loop
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
