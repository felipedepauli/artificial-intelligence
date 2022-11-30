import cv2
import os
import numpy as np
from pyzbar import pyzbar

path = "./engineering/deep_learning/vision/opencv/python/rouizi/"
# image = cv2.imread(os.path.join(path, "images/qrcode.png"))
windowTitle = "Olá!"
image = cv2.imread('/d/aincrivelfabrica\git/theory\engineering/deep_learning/vision\opencv/python/rouizi/images/qrcode.png')
cv2.imshow(windowTitle, image)
cv2.waitKey(0)

# Tá muito grande. Vamos diminuí-la!

image = cv2.resize(image, (640, 850))

cv2.imshow(windowTitle, image)
cv2.waitKey(0)

# Ficou melhor!

red             = (0, 0, 255)
green           = (0, 255, 0)
barcode_color   = (255, 0, 0)
qrcode_color    = (255,255,0)

barcodes = pyzbar.decode(image)

for barcode in barcodes:
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape((-1, 1, 2))   # Quando a gente usa -1, estamos dizendo que não sabemos qual é a dimensão. Infira!
    print(pts)
    if barcode.type == "QRCODE":
        cv2.polylines(image, [pts], True, qrcode_color, 3)
    if barcode.type == "CODE128":
        cv2.polylines(image, [pts], True, barcode_color, 3)
    text = "{}".format(barcode.data.decode("utf-8"))
    cv2.putText(image, text, (barcode.rect[0], barcode.rect[1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, 2)

cv2.imshow(windowTitle, image)
cv2.waitKey(0)




