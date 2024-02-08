#                          GUI


''' # read a colour image from the working directory
img = cv2.imread('download.jfif')
#img = cv2.resize(img,(320,240))

 # display the original image
cv2.imshow('Original Image', img)
key = cv2.waitKey(0)
print(key)
 # KEYBOARD INTERACTIONS
if key == ord('q'):
                cv2.destroyAllWindows()
cv2.imwrite("new image",img)'''
#------------------------------------------------------
#                    Trackbar
'''
import cv2 as cv
import numpy as np

def nothing(self):
    pass

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
while (True):

    cv.imshow('image', img)


    k = cv.waitKey(1)
    if k == 27:
        break


    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')


    img[:] = [b, g, r]


cv.destroyAllWindows()
'''
#-----------------------------------------------------------------
#
'''
import cv2 as cv
import numpy as np

def nothing(self):
    pass

cv.namedWindow('image')
cv.createTrackbar('t','image',0,255,nothing)
while (True):
    img=np.zeros((512,512,3),np.uint8)
    img_center_y=img.shape[0]//2
    img_center_x=img.shape[1]//2
    s=int(cv.getTrackbarPos('t','images'))
    cv.circle(img,(img_center_y,img_center_x), s, (0,0,255), -1)
    cv.rectangle(img,(0,0),(s,s),(255,0,0),-1)
    cv.imshow('img',img)

    k = cv.waitKey(1)
    if k == 27:
        break


cv.destroyAllWindows()'''
#--------------------------------------------------------------------------
#                           Switch

import cv2  
import numpy as np

#trackbar callback fucntion does nothing but required for trackbar
def nothing(x):
    pass

def change_color(x):
    if(cv2.getTrackbarPos('rad','controls')>127):
        global color
        color=(255,0,0)
    else:
         color=(0,0,255)
#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls')
#create trackbar in 'controls' window with name 'r''
cv2.createTrackbar('rad','controls',0,255,change_color)
cv2.createTrackbar('s','controls',0,1,nothing)
#initial color
color=(0,0,255)
while(1):
    img = np.zeros((512,512,3), np.uint8)
#returns current position/value of trackbar
    radius= int(cv2.getTrackbarPos('rad','controls'))
#returns current slider value of trackbar 's'
    switch=cv2.getTrackbarPos('s','controls')

#checks if shape varible is off (0) or on (1)
#draw square if switch is on
    if(switch==1):
        image = cv2.rectangle(img, (0,0), (radius,radius), color, -1)    
        pass
#draw circle if switch is off
    else:
#draw a red circle
        cv2.circle(img,(200,200), radius, color, -1)
#show the image window
        cv2.imshow('img',img)

#waitfor the user to press escape and break the while loop
        k = cv2.waitKey(1)# & 0xFF
        if k == 27:
            break

#destroys all window
cv2.destroyAllWindows()

#------------------------------------------------------------------------
import cv2
import numpy as np
 # read a colourful image
img_1 = cv2.imread('ged.jpg')
img_1 = cv2.resize(img_1, (620,410))
# display the image
cv2.imshow('Colour', img_1)

 # read another image to display clicked colour
img_2 = cv2.imread('mke.jpg')
cv2.imshow('image2', img_2)
#img_2 = np.zeros((912, 912, 3), np.uint8)
#img_2 = cv2.resize(img_2, (620,410))
#cv2.imshow('Colour', img_2)
print(img_2.shape)
def Mouse_Event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # read colours at left clicked point
        b = img_1[x,y,0]
        g = img_1[x,y,1]
        r = img_1[x,y,2]
        # change the colour of a portion of image
        coloured = img_2.copy()
        coloured[0:255, 0:300, 0:150] = [b,g,r]
   #     coloured[:, :, :] = [b,g,r]
        str1=" Mouse Event Demo  -Color values : "+ str(b)+" "+str(g)+ " " +str(r)
        coloured = cv2.putText(coloured, str1, (40,190), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 2)
        cv2.imshow('Clicked Colour', coloured)
        print(b,g,r)

 # set Mouse Callback method
cv2.setMouseCallback('Colour', Mouse_Event)
cv2.waitKey(0)
cv2.destroyAllWindows()


