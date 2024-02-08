import cv2
import numpy as np
img=np.ones((512,512,3),np.uint8)
img=img*255
"""pts=np.array([[25,50],[25,100],[100,25]],np.int32)
pts=pts.reshape((-1,2,1))
isClosed=True 
color=(255,0,0)
thickness=2
image=cv2.polylines(img,[pts],isClosed,color,thickness)
cv2.imshow("triangle",image)"""

"""font=cv2.FONT_HERSHEY_SIMPLEX
org=(50,50)
fontScale=1
color=(100,100,0)
thickness=2
img=cv2.putText(img,'KEC',org,font,fontScale,color,thickness,cv2.LINE_AA)
cv2.imshow("KEC",img)


img1=cv2.rectangle(img,(20,5),(40,20),(0,255,0),2)
cv2.imshow("reactangle",img1)

img12=cv2.rectangle(img,(20,5),(40,20),(255,255,255),2)
cv2.imshow("square",img12)"""

#<---Olympic logo--->
img1=cv2.circle(img,(120,50),40,(255,0,0),2)
cv2.imshow("circle",img1)
img2=cv2.circle(img,(170,50),40,(0,0,0),2)
cv2.imshow("circle",img2)
img3=cv2.circle(img,(220,50),40,(0,0,255),2)
cv2.imshow("circle",img3)
img4=cv2.circle(img,(140,110),40,(0,255,255),2)
cv2.imshow("circle",img4)
img5=cv2.circle(img,(190,110),40,(0,255,0),2)
cv2.imshow("circle",img5)


