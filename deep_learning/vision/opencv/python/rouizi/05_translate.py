import cv2
import os
import numpy as np

path = "engineering/vision/opencv/python/rouizi/"
msg = "Press 'q' to quit"
image = cv2.imread(os.path.join(path, "images/roi.jpg"))

cv2.imshow(msg, image)
cv2.waitKey(0)

height, width = image.shape[:2]
width = int(width * 2)
height = int(height * 2)

print(height, "x", width)

tx = 50
ty = 100

# Primeiro a gente precisa definir os deslocamentos.
# Primeiro o ponto de deslocamento em x
# Segundo  o ponto de deslocamento em y
# Para fazer isso é bem simples: usamos uma matriz identidade com
# o valor de deslocamento em B.
# Ax = B
# Existem duas formas de se fazer isso:
matrix = np.float32([[1, 0, 100], [0, 1, 50]])
A = np.array([[1, 0, tx],
              [0, 1, ty]],
              np.float32)

trans_image = cv2.warpAffine(image, A, (width, height))

cv2.imshow(msg, trans_image)
cv2.waitKey(0)