import numpy as np
import cv2
import skvideo.io as sk

cap = sk.FFmpegReader('../input/video/02.avi')

Cascade = cv2.CascadeClassifier('../data/model/lbp_17/cascade.xml')

i = 0
for frame in cap.nextFrame():

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    point = Cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=100, minSize=(120, 120), maxSize=(140, 140))

    if len(point) > 0 and i % 2 == 0:
        for rect in point:
            cv2.rectangle(gray, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=2)
    i += 1

    cv2.imshow('frame',gray)

    cv2.waitKey(1)

    point = None

cap.release()
cv2.destroyAllWindows()
