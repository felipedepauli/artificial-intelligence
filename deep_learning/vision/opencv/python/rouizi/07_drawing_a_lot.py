import os
import cv2

path = "engineering/vision/opencv/python/rouizi"
file = "images/insane.jpg"

class myImage:

    green = (0,255,0)
    blue  = (255,0,0)
    red   = (0,0,255)
    black = (0, 0, 0)
    white = (255,255,255)

    def __init__(self, path, file, msg=""):
        self.msg    = msg
        self.path   = path
        self.image  = cv2.imread(os.path.join(path, file))

    def amIExist(self):
        return os.path.exists(self.path)

    def drawLine(self, start_point, end_point, color=green, thickness=2):
        cv2.line(self.image, start_point, end_point, color, thickness)

    def drawRectangle(self,left_corner, right_corner, color=green, thickness=2):
        cv2.rectangle(self.image, left_corner, right_corner, color, thickness)

    def drawCircle(self, center, radius, color=blue, thickness=-1):
        cv2.circle(self.image, center, radius, color, thickness)

    def drawEllipse(self, center, axes, angle, startAngle, endAngle, color=red, thickness=2):
        cv2.ellipse(self.image, center, axes, angle, startAngle, endAngle, color, thickness)
    
    def label(self, text, position, fontScale=1, color=white, thickness=1):
        cv2.putText(self.image, text, position, cv2.FONT_HERSHEY_COMPLEX, fontScale, color, thickness)

    def imshow(self, msg=""):
        if msg == "":
            msg = self.msg
        cv2.imshow(msg, self.image)
        cv2.waitKey(0)
        
image = myImage(path, file, "My fucking window")
print(image.amIExist())
image.drawLine((100,100), (400,100), (255, 255, 0), 4)
image.drawRectangle((180, 180), (300, 270))
image.drawCircle((240, 225), 100, thickness=2)
image.drawEllipse((240,225), (150,50), 0, 0, 360)
image.label("Vai vendo!", (100, 50))
image.imshow()