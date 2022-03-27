import cv2
import numpy as np
import pyautogui
import os

os.chdir("C://Apix Media")
screen_size = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter("Apix video.avi", fourcc, 24.0,  (screen_size))
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("Your screen", frame)
    if cv2.waitKey(1) == ord("q"):
        break
        cv2.destroyALLWindows()