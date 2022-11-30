from itertools import count
import cv2
import os
import numpy as np

path = "engineering/vision/opencv/python/rouizi"

image = cv2.imread(os.path.join(path, "./images/objects.jpg"))

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_image, (3,3), 0)


canny = cv2.Canny(blurred, 10, 100)

contorno, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image_copy = np.ones(image.shape)

cv2.drawContours(image_copy, contorno, -1, (0, 0, 0), 1)


cv2.imshow("Original", image)
cv2.imshow("Gray", gray_image)
cv2.imshow("Blurred", blurred)
cv2.imshow("Canny", canny)
cv2.imshow("Contours", image_copy)

cv2.waitKey(0)