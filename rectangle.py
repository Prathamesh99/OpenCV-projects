import cv2
import numpy as np
import matplotlib.pyplot as plt

drawing = False
ix, iy = -1, -1

def draw_rect(event, x, y, param, flags):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        cv2.rectangle(img, (ix,iy), (x,y), (255,255,0),-1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix,iy),(x,y), (255,255,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.rectangle(img, (ix,iy),(x,y),(255,255,0),-1)

cv2.namedWindow(winname='free_draw')
cv2.setMouseCallback('free_draw',draw_rect)

img = np.zeros((512,512,3), np.int8)
while(True):
    cv2.imshow('free_draw',img)
    if cv2.waitKey(2) & 0xff == 27:
        break

cv2.destroyAllWindows()



