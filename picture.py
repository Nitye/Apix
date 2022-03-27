import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow("Python Photos")

img_counter = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("test", frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
         print("Escape hit, closing the app")
         break

    elif k%256 == 32:
        img_name = "openCv image.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("Picture taken")
        img_counter+=1

cap.release()
cap.destroyAllWindows()