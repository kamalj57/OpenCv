import cv2
import numpy as np

# define an image (black) on which the circle to be drawn
img = np.zeros((512,512,3), np.uint8)

# define mouse callback function to draw circle
def draw_circle(event, x, y, flags, param):
      if event == cv2.EVENT_LBUTTONDOWN:
         cv2.circle(img, (x, y), 100, (0, 255, 255), 2)

# Create a window
cv2.namedWindow("Circle Window")

# bind the callback function to the window
cv2.setMouseCallback("Circle Window", draw_circle)

# display the image
while True:
   cv2.imshow("Circle Window", img)
   if cv2.waitKey(20) & 0xFF == 27:
      break
cv2.destroyAllWindows()
