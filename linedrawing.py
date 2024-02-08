#Drawing Function
import opencv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.imshow('The line drawing',img)
img1=cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow("The line ",img1)
cv2.waitkey(0)
cv2.destroyAllWindows()
