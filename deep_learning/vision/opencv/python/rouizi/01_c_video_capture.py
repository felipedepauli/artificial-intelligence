import cv2
import os

path = "theory/engineering/vision/opencv/python/rouizi/"

video = cv2.VideoCapture(os.path.join(path, "videos/pexels-cottonbro-5532768.mp4"))
webcam = cv2.VideoCapture(0)

# Não existe uma opção de tocar vídeo. O que existe
# é uma opção para mostrar os frames. Como os frames
# serão mostrados muito rapidamente, parecerá um vídeo

while True:
    success, frame = webcam.read()
    cv2.circle(frame, (330, 350), 10, (0, 255, 0), 1)
    cv2.imshow("frame", frame)
    if cv2.waitKey(20) == ord('q'):
        break

video.release()
webcam.release()
cv2.destroyAllWindows()

# Você pode perceber que dá ruim pelo fato da resolução.
# É possível modificar a resolução do vídeo

frame_width     = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height    = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps             = int(video.get(cv2.CAP_PROP_FPS))

print("Width  =", frame_width)
print("Height =", frame_height)
print("FPS    =", fps)