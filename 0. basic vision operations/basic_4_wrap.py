import cv2
import numpy as np 

img = cv2.imread('cards.jpg')

w, h = 250, 350
points_1 = np.float32([[164,17],[282,93],[40,162],[163,249]])
points_2 = np.float32([[0,0],[w,0],[0, h],[w,h]]) 

# make perspectives target image
perspective_image = cv2.getPerspectiveTransform(points_1, points_2)
warpped_image = cv2.warpPerspective(img, perspective_image, (w,h))

cv2.imshow('original', img)
cv2.imshow('Warpped image', warpped_image)
cv2.waitKey(0)