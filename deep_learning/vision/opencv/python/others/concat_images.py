import numpy as np
import os
import cv2

root = "engineering/vision/opencv/python/others"

# Loading two images to concatenate
image1 = cv2.imread(os.path.join(root, "./images/dice.jpg"))
image2 = cv2.imread(os.path.join(root, "./images/sample.jpg"))

# Let's show them ;D
cv2.imshow('this is my pic', image1)
cv2.waitKey(0)
cv2.imshow('this is my pic', image2)
cv2.waitKey(0)

# -------------------------------------------------------
# SAME DIMENSIONS IMAGES CONCATENATION
# Each image is set of numbers in an arrow.
# If you concatenate two images with the same dimensions, you have two images side by side.
same_dimensions = np.concatenate((image1, image1), axis=1)
cv2.imshow('Hey, brow!', same_dimensions)
cv2.waitKey(0)

# -------------------------------------------------------
# VERTICALLY CONCATENATION
# We are going to define a function for vertically
# concatenating images of different widths

def vconcat_resize(img_list, interpolation 
                   = cv2.INTER_CUBIC):
      # take minimum width
    w_min = min(img.shape[1] 
                for img in img_list)
      
    # resizing images
    im_list_resize = [cv2.resize(img,
                      (w_min, int(img.shape[0] * w_min / img.shape[1])),
                                 interpolation = interpolation)
                      for img in img_list]
    # return final image
    return cv2.vconcat(im_list_resize)
  
# Now we call the function passing the two images as arguments
img_v_resize = vconcat_resize([image1, image2])
  
# show the output image
cv2.imshow('vconcat_resize.jpg', img_v_resize)
cv2.waitKey(0)

# -------------------------------------------------------
# HORIZONTALLY CONCATENATION
# We are going to define a function for horizontally
# concatenating images of different widths

def hconcat_resize(img_list, 
                   interpolation 
                   = cv2.INTER_CUBIC):
      # take minimum hights
    h_min = min(img.shape[0] 
                for img in img_list)
      
    # image resizing 
    im_list_resize = [cv2.resize(img,
                       (int(img.shape[1] * h_min / img.shape[0]),
                        h_min), interpolation
                                 = interpolation) 
                      for img in img_list]
      
    # return final image
    return cv2.hconcat(im_list_resize)
  
# function calling
img_h_resize = hconcat_resize([image1, image2, image1])

  
# show the output image
cv2.imshow('vconcat_resize.jpg', img_h_resize)
cv2.waitKey(0)



cv2.destroyAllWindows()