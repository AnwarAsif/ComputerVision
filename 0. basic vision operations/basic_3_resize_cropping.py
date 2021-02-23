import cv2
import numpy as np 

# image resize 
img = cv2.imread('test.jpg')
resize_img = cv2.resize(img, (200, 179))

# image crop
crop_img = img[800:1200, 2000:2500]


cv2.imshow('Resized image', resize_img)
cv2.imshow('Cropped image', crop_img)
cv2.waitKey(0)