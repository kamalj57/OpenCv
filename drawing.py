import cv2
import numpy as np
#img=np.zeros((512,512,3),np.uint8)

#<---Image Shape-->
"""cv2.imshow('The line drawing',img)
img1=cv2.line(img,(0,0),(511,511),(255,0,0),5) -->blue Line
img1=cv2.line(img,(0,0),(511,511),(255,255,255),5)  -->white Line
img1=cv2.line(img,(0,0),(511,511),(567,859,0),5) -->skyblue Line
img1=cv2.arrowedLine(img,(0,0),(511,511),(255,0,0),5) -->arrowedline
img1=cv2.rectangle(img,(0,0),(511,511),(255,0,0),5)--> rectangle
img1=cv2.ellipse(img,(120,100),(100,50),0,0,360,(0,255,0),5) -->ellipse"""

#<---cv2.putText()method -->Display font in an image--->
"""
font=cv2.FONT_HERSHEY_SIMPLEX
org=(50,50)
fontScale=1
color=(100,100,0)
thickness=2
img=cv2.putText(img,'KAMALESH J',org,font,fontScale,color,thickness,cv2.LINE_AA)
#cv2.imshow("The line ",img1)
cv2.imshow("Font ",img)
"""

#<---cv2.polylines()method-->
"""
pts=np.array([[25,70],[25,160],[110,200],[200,160],[200,70],[110,20]],np.int32)
pts=pts.reshape((-1,1,2))
isClosed=True --> connect the strt & end points
color=(255,0,0)
thickness=2
image=cv2.polylines(img,[pts],isClosed,color,thickness)
while(1):
    cv2.imshow('polygon',image)
    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()"""

#<----Thresholding--->
"""
img=cv2.imread('ged.jpg',0)
cv2.imshow('image',img)
ret,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("thresh_binary",thresh)
cv2.imshow("thresh_bin_inv",thresh2)
cv2.imshow("thresh_trunc",thresh3)
cv2.imshow("thresh_tozero",thresh4)
cv2.imshow("thresh_tozero_inc",thresh5) """

#<---Array Slicing and cropping--->
"""
img=cv2.imread('ged.jpg')
roi=img[200:250,300:350]
cv2.imshow("roi",roi)"""

#masking
"""img=cv2.imread('download.jfif')
cv2.imshow("OI",img)
black=np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow("Black",black)
circle=cv2.circle(black,(img.shape[1->height]//2-20,img.shape[0->width]//2-20),50,255,-1)
cv2.imshow("Mask",circle)
mask=cv2.bitwise_and(img,img,mask=circle)
cv2.imshow("MI",mask)"""

#<--Erosion and Dilation-->
#morphological image processing
#removing noise - unwanted pixels
#identify intensity bumps or holes in picture
#Dilation -> expand the image -->cv2.erode(src,kernel,dest[,anchor[,iterations[,borderType[,borderValue]]]])
#Erosion -> shrinking the image
"""img=cv2.imread('jk.png',0)
cv2.imshow('copyninja',img)
kernel=np.ones((5,5),np.uint8)
imgd=cv2.dilate(img,kernel,iterations=14)
cv2.imshow("Dilation",imgd)
imge=cv2.erode(img,kernel,iterations=14)
cv2.imshow("Erosion",imge) """

#both erosion and dilation -> cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
"""img=cv2.imread('noisy.jfif',0)
cv2.imshow('oi',img)
kernel=np.ones((5,5),np.uint8) [np.zeros->filter doesn't apply,original image willcome]
morph=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow("morph",morph)"""

"""img=cv2.imread('noisy.jfif',0)
cv2.imshow('oi',img)
kernel1=(5,5)
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,kernel1)
morph=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow("morph",morph) """

#both dialtion and erosion -> cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
#diff btwn erosion & dilation -> cv2.morphologyEx(img,cv2.MORPH_GADIENT,kernel)
#diff btwn opening & original image -> cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
#diff btwn closing & original image -> cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel

img=cv2.imread('car.jfif')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rectkernel=cv2.getStructuringElement(cv2.MORPH_RECT,(13,15))
black=cv2.morphologyEx(gray,cv2.MORPH_BLACKHAT,rectkernel)
top=cv2.morphologyEx(gray,cv2.MORPH_TOPHAT,rectkernel)
cv2.imshow('oi',img)
cv2.imshow("black",black)
cv2.imshow("top",top)
