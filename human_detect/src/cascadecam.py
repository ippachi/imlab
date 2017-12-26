import cv2
import numpy as np

Cascade = cv2.CascadeClassifier('../data/model/lbp_17/cascade.xml')

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	frame = frame[:,::-1]

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	point = Cascade.detectMultiScale(gray, scaleFactor=1.06, minNeighbors=45, minSize=(200, 200), maxSize=(320, 320))

	if len(point) > 0:
		for rect in point:
			cv2.rectangle(gray, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=2)

	cv2.imshow('camera capture', gray)

	cv2.waitKey(1)

	k = cv2.waitKey(1)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()

