import cv2
import os

path  = "theory/engineering/vision/opencv/python/rouizi/"
msg   = "Press 'q' to quit"
image = cv2.imread(os.path.join(path, "images/roi.jpg"))

cv2.imshow(msg, image)
cv2.waitKey(0)

img_width  = image.shape[0]
img_height = image.shape[1]

print(img_height)
print(img_width)

factor = 2.5

image = cv2.resize(image, (int(img_height*factor), int(img_width*factor)))
print('É nozes')

cv2.imshow(msg, image)
cv2.waitKey(0)