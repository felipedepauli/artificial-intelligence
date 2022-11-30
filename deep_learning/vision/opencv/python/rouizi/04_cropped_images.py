# Para cropar basta usar o método de slice

import cv2
import os

path  = "theory/engineering/vision/opencv/python/rouizi/"
msg   = "Press 'q' to quit"
image = cv2.imread(os.path.join(path, "images/roi.jpg"))

cv2.imshow(msg, image)
cv2.waitKey(0)

# Vamos cropar esta parada
image_cropped = image[0:200, 0:200]
cv2.imshow(msg, image_cropped)
cv2.waitKey(0)