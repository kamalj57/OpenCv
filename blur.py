import cv2 as cv
import numpy as np
img=cv.imread("download.jfif")
cv.imshow("og",img)
#                 GaussianBlur
#Syntax -> GaussianBlur(src,dst,ksize,sigmaX)
"""guass=cv.GaussianBlur(img,(5,5),100)
cv.imshow("guasin",guass)"""

#                   MedianBlur
#->Salt and pepper noise(Impulse noise)
#Syntax -> medianBlur(src,dst,ksize)
"""median=cv.medianBlur(img,15)
cv.imshow("median",median)"""

#                   Bilateral Blur
"""intensity of each pixel replace with weighted avg of intensity values from nearby pixels
sharp edges can be preserved while degrading the weak ones"""
#Syntax -> bilateralFilter(src,dst,d,sigmaColor,sigmaSpace,borderType)
"""bilateral= cv.bilateralFilter(img,9,150,150)
cv.imshow("bilateral",bilateral)"""
#-------------------------------------------------------------------------------------"""
#create border
#Syntax -> cv2.copyMakeBorder(src,top,bottom,left,right,borderType,value)
#bord=cv.copyMakeBorder(img,7,8,15,12,cv.BORDER_CONSTANT,None,value=155)
"""bord=cv.copyMakeBorder(img,207,108,205,112,cv.BORDER_REFLECT,None)
cv.imshow("border",bord)"""
#-------------------------------------------------------------------------------------"""
#                    Grayscaling of Images
""" 1.cv2.cvtColor() function
    2.cv2.imread()with flag=0
    3.pixel manipulation(Average method) """
#img=cv.imread("sharp.jfif",0) -> gray scale img(,0)is important
#img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY) -> using cvtColor
#cv.imshow("gi",img1)
#-------------------------------------------------------------------------------------

#print height,width,bgr values of an image
h,w,d=img.shape
"""print("Height :",h,"Width :",w)
h1=int(input())
w1=int(input())
b,g,r=img[h-h1,w-w1]
print("Blue:",b,"Green:",g,"Red:",r)"""
#-------------------------------------------------------------------------------------

#                     Edge detection in image
#syntax -> cv2.Canny(img,T_lower,T_upper,aperture_size,L2Gradient)
#edge=cv.Canny(img,70,70)
#cv.imshow("edge",edge)
#-------------------------------------------------------------------------------------

#                       Scaling an image
#Synatx -> cv2.resize(src,dsize[,dst[,fx[,fy[,interpolation]]]])
#cv2.INTER_AREA ->shrinking ,cv2.INTER_CUBIC -> zooming
"""scale=cv.resize(img,(int(w/2),int(h/2)),interpolation=cv.INTER_AREA)
scale1=cv.resize(img,(int(w*2),int(h*2)),interpolation=cv.INTER_CUBIC)
cv.imshow("shrinking",scale)
cv.imshow("zooming",scale1)"""
#-------------------------------------------------------------------------------------

#                      Placing text in an image
""""font=cv.FONT_HERSHEY_SIMPLEX
org=(50,50)
fontScale=1
color=(255,0,0)
thickness=2
img=cv.putText(img,'KAMAL',org,font,fontScale,color,thickness,cv.LINE_AA)
cv.imshow("Font ",img)"""
#-------------------------------------------------------------------------------------

#                       Translating Image
# Syntax -> cv2.warpAffine(src,M,dsize,dst,flags,borderMode,borderValue)
#quarter_height,quarter_width=h/6,w/6
"""T=np.float32([[1,0,10],[0,1,30]])
translate=cv.warpAffine(img,T,(w,h))
cv.imshow("Translater",translate)"""
#-------------------------------------------------------------------------------------

#                        circle
#cv2.circle(
circle=cv.circle(img,(100,60),30,(120,120,120),-2)
cv.imshow("icrcle",circle)

