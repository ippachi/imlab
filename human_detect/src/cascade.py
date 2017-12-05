import numpy as np
import cv2
import skvideo.io as sk

cap = sk.FFmpegReader('../input/video/02.avi')

Cascade = cv2.CascadeClassifier('../data/model/cascade.xml')

for frame in cap.nextFrame():

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    point = Cascade.detectMultiScale(gray, 1.06, 4, 0, (140, 140), (160, 160))

    i = 0
    if len(point) > 0:
      for rect in point:
        i += 1
        if i % 5 == 0:
          cv2.rectangle(gray, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=2)

    cv2.imshow('frame',gray)

    cv2.waitKey(1)

    point = None

cap.release()
cv2.destroyAllWindows()
