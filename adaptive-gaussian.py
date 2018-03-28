import cv2 as cv
import numpy as np
img = cv.imread('./images/pool-table-above-17031042.jpg', 0)
cv.imshow('orig', img)
cv.waitKey(0)

img = cv.medianBlur(img, 7)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY, 11, 2)
cv.imshow('adaptive thresh gaussian', th3)
cv.waitKey(0)