import cv2
import numpy as np
import os

path = "engineering/vision/opencv/python/rouizi/"
image = cv2.imread(os.path.join(path, "images/roi.jpg"))

cv2.imshow("Minha Imagem", image)
cv2.waitKey(0)

image[200:333, 80:160] = [0, 0, 255]
cv2.imshow("Minha Imagem", image)
cv2.waitKey(0)

# Se você quiser, pode retirar toda uma cor fundamental.
image[:, :, 0] = 0
cv2.imshow("Os verdes sumiram", image)
cv2.waitKey(0)