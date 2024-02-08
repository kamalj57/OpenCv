import cv2 as cv
import os
import numpy as np
print(cv.__version__)
people=['dhoni','sachien','kohli']
print(people)
DIR=r'C:\Users\user\AppData\Local\Programs\Python\Python311\images'
face_classifier=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
features=[]
labels=[]
def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.1,3)
            for (x,y,w,h) in faces:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()
print("Training Done")
print("Feature lenght=",len(features))
print("Label Length=",len(labels))
features=np.array(features,dtype='object')
labels=np.array(labels)
face_recoginizer=cv.face.LBPHFaceRecognizer_create()
face_recoginizer.train(features,labels)
face_recoginizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
print("successful")



                
