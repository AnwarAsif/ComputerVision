import cv2 
import numpy as np 

#Load image
img = cv2.imread('lena.png')

#Color convert 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gaussian blur 
blur_img = cv2.GaussianBlur(gray_img, (5,5), 0)

# Canny edge detector 
imgCanny = cv2.Canny(img, 100,200)

# Dilation Image 
kernel = np.ones((5,5),np.uint8)
dilation_image = cv2.dilate(imgCanny, kernel, iterations = 1)

# Eroded image
erode_image = cv2.erode(dilation_image, kernel, iterations =1)


cv2.imshow('gray image',gray_img)
cv2.imshow('Blur image',blur_img)
cv2.imshow('Canny image',imgCanny)
cv2.imshow('Dilate image', dilation_image)
cv2.imshow('Eroded image', erode_image)
cv2.waitKey(0)