import cv2
import numpy as np

# Vamos gerar uma imagem definindo seus pixels
# Queremos uma imagem 400x600
image1 = np.zeros((400, 600), dtype="uint8")
print(image1)

# Agora vamos desenhar nessa tela em branco
cv2.rectangle(image1, (20,20), (300,20), (200,100,100), 1) 
image2 = np.zeros((400, 600), dtype="uint8")
cv2.rectangle(image2, (100,20), (300,200), (200,100,100), -1) 
cv2.imshow("Minha janela insana", image1)
cv2.waitKey(0)
cv2.imshow("Minha janela insana", image2)
cv2.waitKey(0)

new_image = cv2.bitwise_or(image1, image2)
cv2.imshow("Minha Janela Insana", new_image)
cv2.waitKey(0)

# Você pode criar uma máscara utilizando o bitwise_and

