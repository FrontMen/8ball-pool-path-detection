# Mat img = imread("images/pool-table-above-17031042.jpg", 0);
# Mat img2, dst;
# pyrDown(img, img2);
# adaptiveThreshold(255-img2, dst, 255,  ADAPTIVE_THRESH_MEAN_C,
#         THRESH_BINARY, 9, 10); imwrite("adaptiveT.png", dst);
# imshow("dst", dst);

import numpy as np
import cv2

# im = cv2.imread('images/pool-table-above-17031042.jpg', cv2.COLOR_BGR2GRAY)
img = cv2.imread("images/pool-table-above-17031042.jpg", 0)

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
grayout = 255*np.ones((im.shape[0], im.shape[1], 1), np.uint8)
blur = cv2.GaussianBlur(gray, (5, 5), 1)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
wcnt = 0
for item in contours:
    area = cv2.contourArea(item)
    print wcnt, area
    [x, y, w, h] = cv2.boundingRect(item)
    if area > 10 and area < 200:
        roi = gray[y:y+h, x:x+w]

        cntd = 0
        for i in range(x, x+w):
            for j in range(y, y+h):
                if gray[j, i] == 0:
                    cntd = cntd + 1
        density = cntd/(float(h*w))

        if density < 0.5:
            for i in range(x, x+w):
                for j in range(y, y+h):
                    grayout[j, i] = gray[j, i]
        wcnt = wcnt + 1

cv2.imwrite('result.png', grayout)
