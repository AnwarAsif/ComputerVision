import cv2 
import numpy as np

def empty(a):
    pass

cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', (640,400))
cv2.createTrackbar('Hue min','TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue max','TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat min','TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat max','TrackBar', 157, 255, empty)
cv2.createTrackbar('Val min','TrackBar', 174, 255, empty)
cv2.createTrackbar('Val max','TrackBar', 255, 255, empty)

while True:
    img = cv2.imread('ball.png')
    img = cv2.resize(img, (640, 412))
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('Hue min','TrackBar')
    h_max = cv2.getTrackbarPos('Hue max','TrackBar')
    s_min = cv2.getTrackbarPos('Sat min','TrackBar')
    s_max = cv2.getTrackbarPos('Sat max','TrackBar')
    v_min = cv2.getTrackbarPos('Val min','TrackBar')
    v_max = cv2.getTrackbarPos('Val max','TrackBar')

    low = np.array([h_min, s_min, v_min])
    up = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img, low, up)
    img_result = cv2.bitwise_and(img, img, mask=mask)

    img_bk = np.stack((mask,)*3, axis=-1)
    img_col = np.hstack([img, hsv_img,img_bk,img_result])
    img_col = cv2.resize(img_col, (1200,300))

    cv2.imshow('All', img_col)

    cv2.waitKey(1)