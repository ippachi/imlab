import numpy as np
import cv2
import skvideo.io as sk

img_src = cv2.imread("../input/image/sample.png", 1)

img_result = img_src

Cascade = cv2.CascadeClassifier('../data/model/lbp_17/cascade.xml')

gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
point = Cascade.detectMultiScale(gray, scaleFactor=1.06, minNeighbors=0, minSize=(90, 90), maxSize=(100, 100))

if len(point) > 0:
    for rect in point:
        cv2.rectangle(img_result, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=2)

cv2.imshow('show image', img_result)

key = cv2.waitKey(0)&0xff

if key == ord('q'):
    cv2.destroyAllWindows()
    exit()
