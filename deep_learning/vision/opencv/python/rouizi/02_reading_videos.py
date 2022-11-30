import cv2
import os

path = "opencv/rouizi/"
video = cv2.VideoCapture(os.path.join(path, "videos/pexels-cottonbro-5532768.mp4"))

# O vídeo precisa ter uma configuração que faço com quele tenha a resolução correta, assim como a extensão correta.
# The video have to have a configuration that make it lead to a correct resolution and extension.
frame_width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps          = int(video.get(cv2.CAP_PROP_FPS))

print("Width  =", frame_width)
print("Height =", frame_height)
print("FPS    =", fps)

# XVID = avi
# MPEG = mp4
# WEBM = webm
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# E agora criamos um descritor de um arquivo de vídeo com todas as configurações que fizemos
# And now we create a video descriptor with all the configurations that we made
output = cv2.VideoWriter("meu_novo_video.avi", fourcc, fps, (frame_width, frame_height))

def open_video():
    while True:
        success, frame = video.read()
        cv2.imshow("frame", frame)
        output.write(frame)
        if not success:
            break
        # if cv2.waitKey(20) == ord('q'):
        #     break
    video.release()
    cv2.destroyAllWindows()

open_video()