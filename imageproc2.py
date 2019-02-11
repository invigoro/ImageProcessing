import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
status, img = cap.read()

cv.namedWindow("Video")

blank1 = np.float32(img)
blank2 = np.float32(img)

img = np.float32(img)
absDiff = np.float32(img)

while True:
    status, img = cap.read()
    blur = cv.GaussianBlur(img,(5,5),0)
    cv.accumulateWeighted(blur, blank1, .320)
    res1 = cv.convertScaleAbs(blank1)
    absDiff = cv.absdiff(img, res1)
    grayimg = cv.cvtColor(absDiff, cv.COLOR_BGR2GRAY)
    _, grayimg = cv.threshold(grayimg, 25, 255, cv.THRESH_BINARY)
    grayimg = cv.GaussianBlur(grayimg,(5,5),0)
    #grayimg = cv.cvtColor(absDiff, cv.COLOR_BGR2GRAY)
    _, grayimg = cv.threshold(grayimg, 220, 255, cv.THRESH_BINARY)
    img1, contours, hierarchy = cv.findContours(grayimg, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    cv.drawContours(img, contours, -1, (0,255,0), 3)
    cv.imshow("Video", img)
    #cv.imshow("Blur", blur)
    #cv.imshow("Running Avg", res1)
    cv.imshow("Abs Diff", grayimg)
    #cv.imshow("Blank White", blank2)
    #cv.imshow("Prev Frame", img1)

    k = cv.waitKey(1)
    if k == 27:
        break


cv.destroyAllWindows()