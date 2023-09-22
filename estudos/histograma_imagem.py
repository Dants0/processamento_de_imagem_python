from matplotlib import pyplot as plt
import cv2

# img = cv2.imread('star.jpg')
img = cv2.imread('yoda.png')

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem", img)
cv2.waitKey(0)

#função calcular histograma da imagem

h = cv2.calcHist([img], [0], None, [256], [0,256])

plt.figure()
plt.title("Histograma")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(h)
plt.xlim([0, 256])
plt.show()

# plt.hist(img.ravel(),256,[0,256])
# plt.show() 


cv2.waitKey(0)
