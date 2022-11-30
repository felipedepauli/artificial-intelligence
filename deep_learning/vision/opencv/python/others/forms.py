import os
import cv2
import numpy as np

path = "engineering/vision/opencv/python/others/"
image = cv2.imread(os.path.join(path, 'images/minha_nova_imagem.jpg'))

# ----------------------------------------
# 1. RECTANGLES
# Let's start with the rectangles.
# You firstly have to create the configuration to pass as argments to the rectagle cv2 method.

# Configuration
window_name         = 'Image with a rectangle'
start_point         = (5,5)
end_point           = (220, 220)
color               = (255, 0, 0)
thickness           = 2

# Presenting
image_rectangle = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow(window_name, image_rectangle)
cv2.waitKey(0)

# ----------------------------------------
# 2. CIRCLES
# Now we are going to create circles. It's the same process.

# Configuration
window_name         = 'Image with a circle'
center_coordinates  = (150, 360)
radius              = 20
color               = (255, 0, 0)
tickness            = 2
# If you want to fill the circle, set it to -1

# Presenting
image_circle = cv2.circle(image, center_coordinates, radius, color, tickness)
cv2.imshow(window_name, image_circle)
cv2.waitKey(0)

# ----------------------------------------
# 3. POLYLINES

# Configuration
window_name         = 'Image with a polyline'
pts                 = np.array([[ 25,  70], [ 25, 160],  # Polygon corner points coordinates
                                [110, 200], [200, 160],
                                [200,  70], [110,  20]],
                                np.int32)
pts                 = pts.reshape((-1, 1, 2))
isClosed            = True
color               = (255, 0, 0)
thickness           = 2

# Presenting
image_polyline = cv2.polylines(image, [pts], isClosed, color, thickness)
cv2.imshow('image', image_polyline)
cv2.waitKey(0)

# ----------------------------------------
cv2.destroyAllWindows()
