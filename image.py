import cv2
import numpy as np
import time
img=cv2.imread('download.jfif')
#cv2.imshow('image1',img)
#h,w,d=img.shape
#print(h,w,d)
#(B,G,R)=img[100,250]
#print("Image1",R,G,B)
#B,G,R=cv2.split(img)
#cv2.imshow("red",R)
#cv2.imshow("blue",B)
#cv2.imshow("green",G)
#print(R,G,B)
#cv2.imwrite('C:/Users/user/Pictures/new.jpg',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#b=img.copy()
#b[:,:,1]=0
#b[:,:,2]=0
#g[:,:,0]=0
#g[:,:,2]=0
#r=img.copy()
#r[:,:,0]=0
#r[:,:,1]=0
#cv2.imshow("B-RGB",b)
#cv2.imshow("R-RGB",r)
#cv2.imshow("G-RGB",g)
#img1=np.ones((300,300),dtype='uint8')
#cv2.imshow("Black",img1)
#print(img1)
#cv2.imshow("White",img1*255)
#img1=cv2.imread('download.jfif')
#img11=cv2.resize(img1,(270,405))
#cv2.imshow('image2',img11)
#img2=cv2.add(img,img11)
#img2=cv2.subtract(img,img11)
#img2=cv2.multiply(img,img11)
#img2=cv2.divide(img,img11)
#img22=cv2.addWeighted(img,0.35,img2,1,2)
#cv2.imshow('combine',img2)
#<--Transition-->
#for i in np.linspace(0,1,100):
    #alpha=i
    #beta=1-alpha
    #op=cv2.addWeighted(img,alpha,img11,beta,0)
    #cv2.imshow('Tranisitin',op)
    #time.sleep(0.02)
    #if cv2.waitKey(1) == 27:
      #  break
#<--Mask-->
print(img.shape())
mask=np.ones((300,168),dtype='uint8')
mask=mask*255
res=cv2.bitwise_and(img,mask)
cv2.imshow('white',res)
mask1=np.zeros((300,168),dtype='uint8')
res1=cv2.bitwise_and(img,mask1)
cv2.imshow('black',res1)
#(B,G,R)=img11[100,250]
#print("Image2",R,G,B)
#(B,G,R)=img2[100,250]
#print("Combined",R,G,B)
