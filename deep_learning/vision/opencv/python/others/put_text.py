import cv2
import os

path = "opencv/rouizi/"

image = cv2.imread(os.path.join(path, "images/sample.jpg"))

# O putText() é utilizado para escrever texto em um frame.
message     = "This is a notebook"
font        = cv2.FONT_HERSHEY_TRIPLEX
org         = (150,250)
fontScale   = 2
color       = (105, 200, 100)
tickness    = 5

image       = cv2.putText(image, message, org, font, fontScale, color, tickness, cv2.LINE_AA)

cv2.imshow("Minha Imagem", image)

cv2.waitKey(0)