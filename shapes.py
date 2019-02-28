import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_circle (event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y),60, (200,0,0), -1)

cv2.namedWindow (winname='draw')
cv2.setMouseCallback('draw', draw_circle)


img = np.zeros((512,512,3),np.int8)

while(True):
    cv2.imshow('draw', img)
    if cv2.waitKey(1) & (0xff == 27):
        break

cv2.destroyAllWindows()

