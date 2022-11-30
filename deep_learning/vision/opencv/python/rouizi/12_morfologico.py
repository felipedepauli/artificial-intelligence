import cv2
import os

path = "engineering/vision/opencv/python/rouizi"

image = cv2.imread(os.path.join(path, "./images/roi.jpg"))

cv2.imshow("Original", image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel      = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)) 

erode1 = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel, iterations=1)
erode2 = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel, iterations=2)

cv2.imshow("Gray", gray_image)
cv2.imshow("Erode 1", erode1)
cv2.imshow("Erode 2", erode2)
cv2.waitKey(0)


