import cv2 
import numpy as np 

img = cv2.imread('lena.png')
img_hor = np.hstack([img, img, img])
img_hor = cv2.resize(img_hor,(900,300))

cv2.imshow('img',img_hor)
cv2.waitKey(0)