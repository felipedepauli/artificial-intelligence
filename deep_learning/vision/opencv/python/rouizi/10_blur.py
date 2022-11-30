from random import gauss
import cv2
import os

path = "./engineering/deep_learning/vision/opencv/python/rouizi/"
msg  = "New Window"

image = cv2.imread(os.path.join(path, "./images/roi.jpg"))

cv2.imshow(msg, image)


blur_3x3 = cv2.blur(image, (3, 3))
blur_9x9 = cv2.blur(image, (9, 9))

cv2.imshow("Blur 3x3", blur_3x3)
cv2.imshow("Blur 9x9", blur_9x9)
cv2.waitKey(0)

gaussian_blur_3x3 = cv2.GaussianBlur(image, (3,3), 0)
gaussian_blur_9x9 = cv2.GaussianBlur(image, (9,9), 0)

cv2.imshow("Gaussian Blur 3x3", gaussian_blur_3x3)
cv2.imshow("Gaussian Blur 9x9", gaussian_blur_9x9)
cv2.waitKey(0)

median_blur_3x3 = cv2.medianBlur(image, 3)
median_blur_9x9 = cv2.medianBlur(image, 9)

cv2.imshow("Median Blur 3x3", median_blur_3x3)
cv2.imshow("Median Blur 9x9", median_blur_9x9)
cv2.waitKey(0)

bilateral_blur_3x3 = cv2.bilateralFilter(image, 11, 21, 11)
bilateral_blur_9x9 = cv2.bilateralFilter(image, 15, 51, 59)

cv2.imshow("Bilateral Blur 3x3", bilateral_blur_3x3)
cv2.imshow("Bilateral Blur 9x9", bilateral_blur_9x9)
cv2.waitKey(0)

cv2.destroyAllWindows()