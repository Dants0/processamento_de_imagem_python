import cv2

imagem = cv2.imread("start.jpg")

print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2]) 

#mostra a imagem
# cv2.imshow("Yoda", imagem)

#esperando qualquer tecla ser digitada
# cv2.waitKey(0)

# cv2.imwrite("Yoda2.png", imagem)

#ver oredem bgr e não rgb
(b,g,r) = imagem[0,0]

print("O pixel (0, 0) tem as seguintes cores:")
print(f'Vermelho: {r}, Verde: {g}, Azul: {b}')


# def varrerPixelAPixel(imagem):
#     for i in range(0, imagem.shape[0]):
#         for j in range(0, imagem.shape[1]):
#             # imagem[i,j] = (0,255,0) #substituir toda imagem por azul
#             # imagem[i, j] = (i%256,j%256,i%256) #A alteração nas componentes das cores da imagem conforme as coordenadas de linha e coluna geram a imagem acima.
#             imagem[i, j] = (0, (i*j)%256, 0)
#     cv2.imshow("Imagem modificada", imagem)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    

# varrerPixelAPixel(imagem)

# def modificarImagemACada5PixelsXeY(image):
#     for i in range(0, image.shape[0], 10):
#         for j in range(0, image.shape[1], 20):
#             image[i:i+5, j:j+5] = (0, 255, 255)
#     cv2.imshow("Imagem modificada", image)
#     cv2.waitKey(0)
    
    
# modificarImagemACada5PixelsXeY(imagem)

def criarVariosFormatosNaImagem(image):
    #Cria um retangulo azul por toda a largura da imagem
    image[30:50, :] = (255, 0, 0)
    cv2.imshow("Imagem alterada", image)
    cv2.imwrite("alterada.jpg", image)
    cv2.waitKey(0)

criarVariosFormatosNaImagem(imagem)

#Cria um quadrado vermelho
    # image[100:150, 50:100] = (0, 0, 255)
#Cria um retangulo amarelo por toda a altura da imagem
    # image[:, 200:220] = (0, 255, 255)
#Cria um retangulo verde da linha 150 a 300 nas colunas 250 a
350
    # image[150:300, 250:350] = (0, 255, 0)
#Cria um quadrado ciano da linha 150 a 300 nas colunas 250 a
350
    # image[300:400, 50:150] = (255, 255, 0)
#Cria um quadrado branco
    # image[250:350, 300:400] = (255, 255, 255)
    #Cria um quadrado preto
    # image[70:100, 300: 450] = (0, 0, 0)
