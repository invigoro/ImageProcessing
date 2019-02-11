import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
status, img = cap.read()

cv.namedWindow("Video")

blank1 = np.float32(img)
blank2 = np.float32(img)

img1 = blank1
absDiff = np.float32(img)

while True:
    status, img = cap.read()
    blur = cv.GaussianBlur(img,(5,5),0)
    cv.accumulateWeighted(blur, blank1, .320)
    res1 = cv.convertScaleAbs(blank1)
    absDiff = cv.absdiff(img, res1)

    cv.imshow("Video", img)
    #cv.imshow("Blur", blur)
    cv.imshow("Running Avg", res1)
    cv.imshow("Abs Diff", absDiff)
    #cv.imshow("Blank White", blank2)
    #cv.imshow("Prev Frame", img1)

    img1 = img

    k = cv.waitKey(1)
    if k == 27:
        break


cv.destroyAllWindows()