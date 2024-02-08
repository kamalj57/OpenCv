#                          ColorFilter
import cv2 as cv
import numpy as np
img=cv.imread("rose.jpg")
hav=cv.cvtColor(img,cv.COLOR_BGR2HSV)
lr=np.array([99,100,10])
ur=np.array([195,205,175])
mask=cv.inRange(hav,lr,ur)
cv.imshow("original image",img)
cv.imshow("HSV",mask)
cv.waitkey(0)

