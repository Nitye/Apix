import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
rec = cv2.VideoWriter('Apix Video.avi', fourcc, 24.0, (640, 480))

while True:
    ret, frame = cap.read()
    cv2.imshow("God's beautiful creation", frame)
    key = cv2.waitKey(1) & 0xff
    rec.write(frame)
    if key == ord('q'):
        break

cap.release()
rec.release()
cap.destroyALLWindows()
