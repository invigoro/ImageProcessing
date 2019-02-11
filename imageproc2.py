import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
cv.namedWindow("Video")

blank1 = np.zeros((512,512,3), np.float32)
blank2 = 255 * np.ones((512, 512, 3), np.float32)

img1 = blank1
absDiff = blank1

while True:
    status, img = cap.read()
    cv.absdiff(img, img1, absDiff)

    cv.imshow("Video", img)
    cv.imshow("Blank White", blank1)
    cv.imshow("Blank Black", blank2)
    cv.imshow("Prev Frame", img1)
    cv.imshow("Abs Diff", absDiff)

    img1 = img

    k = cv.waitKey(1)
    if k == 27:
        break

    

cv.destroyAllWindows()