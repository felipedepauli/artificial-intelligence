import cv2
import os

path = "engineering/vision/opencv/python/rouizi/"

# A ação mais básica do OpenCV é a leitura de imagens.
# Para isso, basta usar a função cv2.imread().

image = cv2.imread(os.path.join(path, "images/sample.jpg"))

# Se você imprimir esse arquivo, verá que se trata de uma matriz numpy.
print(image)
print('-----------------------')
print(type(image))
input()

# Vamos dar uma olhada em um dos pixels. O resultado é
# uma matriz de 3 dimensões com o sistema de cores BGR.
print(image[100, 100])
input()

# Se você quiser apenas um canal, por exemplo, apenas blue,
# você pode colocar o índice desejado, sendo 0, 1 e 2 para B G e R.
# Cor Vermelha
print("Red:\t", image[100,100,2])

# Vamos acessar a cor verde
print("Green\t", image.item(100,100,1))

# Vamos dar uma olhada em alguns atributos da imagem.
print("Size:\t", image.size, "bytes")
print("Type:\t", image.dtype)

# cv2.imshow("Minha Imagem", image)
# cv2.imwrite(os.path.join(path, "images/minha_nova_imagem.jpg"), image)

# cv2.waitKey(0)