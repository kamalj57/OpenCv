import cv2 as cv
import numpy as np
people=['dhoni','sachien']
face_classifier=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
face_recoginizer=cv.face.LBPHFaceRecognizer_create()
face_recoginizer.read('face_trained.yml')
img=cv.imread('dhoni3.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("image",img)
face=face_classifier.detectMultiScale(gray,1.1,1)
for (x,y,w,h)in face:
    faces_roi=gray[y:y+h,x:x+h]
    label,confidence=face_recoginizer.predict(faces_roi)
    print(label)
    print(confidence)
    cv.putText(img,people[label],(5,5),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv.imshow('detected person',img)

