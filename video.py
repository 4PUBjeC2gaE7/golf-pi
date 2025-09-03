#!/usr/bin/env python
import numpy as np
import cv2 

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("samples/IMG_1115.MOV")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    dst = cv2.medianBlur(frame, 9)
    edges = cv2.Canny(dst, 50, 150)
    cv2.imshow('frame', edges)
    if cv2.waitKey(20) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
