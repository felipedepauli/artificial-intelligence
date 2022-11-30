import cv2

# Não existe mais! Procurar algo que esteja no lugar.
cv2.legacy_TrackerKCF_create()

video = cv2.VideoCapture('./race.mp4')

ok, frame = video.read()

bbox = cv2.selectROI(frame)