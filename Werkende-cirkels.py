import cv2
import numpy as np
import imutils
import mahotas as mh

img = cv2.imread('./images/7circles.png', 0)
cv2.imshow('start', img)
cv2.waitKey(0)

cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

diameterBall = 80 # 15
radiusBall = int(round(diameterBall/2))
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 2*radiusBall*0.9,
                           minRadius=0, #int(round(radiusBall*0.8)),
                           maxRadius=0, #int(round(radiusBall*1.2)),
                           param1=50,
                           param2=30)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('detected circles', cimg)
    cv2.waitKey(0)

cv2.destroyAllWindows()
