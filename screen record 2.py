import numpy as np
import cv2
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter("Apix video.avi", fourcc, 10.0, (1366, 768))
while True:
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    out.write(frame)
    if cv2.waitKey(1) == 27:
        break
out.release()
cv2.destroyALLWindows()