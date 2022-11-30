import cv2
import os
import numpy as np
from imutils.perspective import four_point_transform

path = "engineering/ia/vision/opencv/python/rouizi/Projetos/02_leitor_de_gabarito"

height      = 800
width       = 600
# --------------------------
green       = (0, 255, 0)
red         = (0, 0, 255)
blue        = (255, 0, 0)
white       = (255,255,255)
# --------------------------
questions   = 5
answers     = 5
correct_ans = [0, 4, 1, 7, 4]
# --------------------------
image       = cv2.imread(os.path.join(path, "images/1.jpg"))
image       = cv2.resize(image, (width, height))
image_copy0 = image.copy()
image_copy1 = image.copy()
# --------------------------
# Ainda não sei o porquê, mas sempre transformamos para cinza
# e depois aplicamos o Blur (desfoque) Gaussiano
gray        = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred     = cv2.GaussianBlur(gray, (5,5), 0)
edged0      = cv2.Canny(gray, 10, 70)
edged1      = cv2.Canny(blurred, 10, 70)

cv2.imshow("Bem Louco1", image)
cv2.imshow("Bem Louco2", gray)
cv2.imshow("Bem Louco3", blurred)
cv2.imshow("Bem Louco4.1 - gray", edged0)
cv2.imshow("Bem Louco4.2 - blurred", edged1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --------------------------
contours, _ = cv2.findContours(edged1, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, green, 3)
cv2.imshow("Yeap!", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --------------------------
# A gente precisa remover tudo que não seja o documento desejado.
# Utilizando o código a seguir, podemos remover o background da imagem,
# que é tudo que não seja a folha do gabarito
def get_rect_cnts(contours):
    rect_cnts = []
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        if len(approx) == 4:
            rect_cnts.append(approx)
    rect_cnts = sorted(rect_cnts, key=cv2.contourArea, reverse=True)
    return rect_cnts
# --------------------------
rect_cnts = get_rect_cnts(contours)
document = four_point_transform(image_copy0, rect_cnts[0].reshape(4,2))

cv2.drawContours(image_copy0, rect_cnts, 1, green, 3)
cv2.imshow("Yeap 2!!", image)
cv2.imshow("Document", document)
cv2.waitKey(0)
cv2.destroyAllWindows()
# --------------------------
# Agora que já removemos o background, temos um documento certinho na imagem.
# Precisamos, agora, destacar as duas regiões de interesse.
gray_doc    = cv2.cvtColor(document, cv2.COLOR_BGR2GRAY)
blurred_doc = cv2.GaussianBlur(gray_doc, (5,5), 0)
edged_doc   = cv2.Canny(blurred_doc, 10, 70)

contours, _ = cv2.findContours(edged_doc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rect_cnts   = get_rect_cnts(contours)
biggest_cnt = rect_cnts[0]
grade_cnt   = rect_cnts[1]

cv2.drawContours(document, rect_cnts[:2], -1, green, 3)
cv2.imshow("Two biggest contours", document)
cv2.waitKey(0)
cv2.destroyAllWindows()


# -------------------------
doc_copy    = document.copy()
doc_copy1    = document.copy()


x,y         = biggest_cnt[0][0][0] + 4, biggest_cnt[0][0][1] + 4
x_W, y_H    = biggest_cnt[2][0][0] - 4, biggest_cnt[2][0][1] - 4

mask        = np.zeros((document.shape[0], document.shape[1]), dtype="uint8")
cv2.rectangle(mask, (x,y), (x_W, y_H), white, -1)
masked      = cv2.bitwise_and(doc_copy, doc_copy, mask=mask)

cv2.imshow("Two biggest contours", document)
cv2.imshow("Masked", masked)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

masked      = masked[y:y_H, x:x_W]
gray        = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
_, thresh   = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("masked", masked)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

def split_image(image):
    r = len(image) // questions * questions
    c = len(image[0]) // answers * answers
    image = image[:r, :c]
    rows = np.vsplit(image, questions)
    boxes = []
    for row in rows:
        cols = np.hsplit(row, answers)
        for box in cols:
            boxes.append(box)

    return boxes

boxes = split_image(thresh)

cv2.imshow("box number 3", boxes[2])
cv2.waitKey(0)
cv2.destroyAllWindows()

score = 0

for i in range(0, questions):
    user_answer = None
    for j in range(0, answers):
        pixels = cv2.countNonZero(boxes[i*5 + j])
        if user_answer is None or pixels > user_answer[1]:
            user_answer = (j, pixels)
    
    cnt, _ = cv2.findContours(boxes[i*5 + user_answer[0]], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnt:
        c[:, :, 0] += x + ((x_W - x) // 5) * user_answer[0]
        c[:, :, 1] += y + ((y_H - y) // 5) * i

    if correct_ans[i] == user_answer[0]:
        cv2.drawContours(doc_copy1, cnt, -1, green, 3)
        score += 1
    else:
        cv2.drawContours(doc_copy1, cnt, -1, red, 3)

score = (score / 5) * 100
x_grade = grade_cnt[0][0][0]
y_grade = grade_cnt[0][0][1]

cv2.putText(doc_copy1, "{}%".format(int(score)),
            (x_grade - 10, y_grade - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, red, 3)

cv2.imshow("image", image)
cv2.imshow("final score", doc_copy1)
cv2.waitKey(0)
cv2.destroyAllWindows()