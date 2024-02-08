import cv2 as cv
""""
img=cv.imread('goku.jpg')
img1=cv.rectangle(img,(300,150),(500,300),(255,134,0),5)
cv.imshow('op',img1)
"""
""""
face=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv.imread('2people.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=face.detectMultiScale(gray,1.2,2)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow('img',img)
"""
face=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
faces=cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
img=cv.imread('3pl.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face1=face.detectMultiScale(gray,1.2,2)
face2=faces.detectMultiScale(gray,1.1,1)
for (x,y,w,h) in face1:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
for (x,y,w,h) in face2:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
cv.imshow('img',img)
