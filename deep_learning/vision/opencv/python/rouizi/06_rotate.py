import cv2
import os

path     = "engineering/vision/opencv/python/rouizi"
filename = "images/sample.jpg"
msg      = "Nova Janela"

image = cv2.imread(os.path.join(path, filename))
cv2.imshow(msg, image)
cv2.waitKey(0)

height, width = image.shape[0:2]

print(height, "x", width)

center_x = width / 2
center_y = height / 2

print(center_x, "x", center_y)

# Sempre iremos utilizar warpAffine. Só precisamos passar a matriz de transformação.
# Essa matriz tem o centro de rotação, o ângulo de rotação e o quanto será escalada a imagem.
M = cv2.getRotationMatrix2D((center_x, center_y), 90, .5)

image = cv2.warpAffine(image, M, (width, height))

cv2.imshow(msg, image)
cv2.waitKey(0)