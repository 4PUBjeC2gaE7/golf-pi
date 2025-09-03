#!/usr/bin/env python
import numpy as np
import cv2 

MIX_FACTOR_A = 0.2
MIX_FACTOR_B = 1 - MIX_FACTOR_A
BLUR_AMOUNT = 9

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, im_base = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    im_blur = cv2.medianBlur(im_base, BLUR_AMOUNT)
    im_edges = cv2.Canny(im_blur, 50, 150)
    im_edges_color = cv2.cvtColor(im_edges, cv2.COLOR_GRAY2RGB)
    im_running = cv2.addWeighted(im_running, MIX_FACTOR_A,
                                 im_edges_color, MIX_FACTOR_B,
                                 0) if 'im_running' in locals() else im_edges_color
    im_output = cv2.subtract(im_base, im_running)

    cv2.imshow('frame', im_output)
    if cv2.waitKey(20) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()