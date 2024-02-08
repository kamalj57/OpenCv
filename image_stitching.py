#                          Image stitching
'''
    -> basically photograph stretched horizontally without distortion
    -> img must have some common key-points btwn imgs
    -> use stitch() function
    -> Homography - transformation that maps the points in one point to the corresponding point in another img
    -> calculation of homography using RANSAC algorithm
    
'''
import cv2 as cv
img=['download1.jfif','download3.jfif']
imgs=[]
for i in range(len(img)):
    imgs.append(cv.imread(img[i]))
    imgs[i]=cv.resize(imgs[i],(0,0),fx=0.8,fy=0.8)
cv.imshow('1',imgs[0])
cv.imshow('2',imgs[1])
stitchy=cv.Stitcher.create()
(dummy,op)=stitchy.stitch(imgs)
if dummy!=cv.STITCHER_OK:
    print("Stitching is not succesfully ")
else:
    print("Your image is ready")
cv.imshow('result',op)
