import cv2
import os

path = "engineering/vision/opencv/python/rouizi"
msg  = "New Window"

image = cv2.imread(os.path.join(path, "./images/roi.jpg"))

cv2.imshow(msg, image)
cv2.waitKey(0)

gray_image_1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image_2 = cv2.GaussianBlur(gray_image_1, (9,9), 0)

cv2.imshow("Gray", gray_image_1)
cv2.imshow("Gray and Gaussian", gray_image_2)
cv2.waitKey(0)

ret, thresh_bin_1 = cv2.threshold(gray_image_1, 90, 255, cv2.THRESH_BINARY)
ret, thresh_bin_2 = cv2.threshold(gray_image_2, 90, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold only Gray", thresh_bin_1)
cv2.imshow("Threshold with Gaussian", thresh_bin_2)


ret, thresh_otsu    = cv2.threshold(gray_image_2, 60, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
adapt_thresh        = cv2.adaptiveThreshold(gray_image_2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)

cv2.imshow("Otsu", thresh_otsu)
cv2.imshow("Adaptative", thresh_otsu)

cv2.waitKey(0)
