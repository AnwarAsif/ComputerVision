import cv2
import numpy as np 

# make img 
img = np.zeros((512,512, 3),np.uint8)
# make img blue
# img[100:200, 100:200] = [255,0, 0]

# Draw 
cv2.line(img, (0,0), (300,300), (0,0,255), 3)
cv2.line(img, (0,img.shape[0]), (img.shape[1],0), (0,255,255), 3)
cv2.circle(img, (200,200), 30, (255,255,0), 2)
cv2.rectangle(img, (200,200),(450,400), (255,255,255), 5)
cv2.rectangle(img, (200,200),(350,300), (255,255,255), cv2.FILLED)

# Text 
cv2.putText(img, 'Asif Anwar',(400,400),cv2.FONT_HERSHEY_DUPLEX , .4, (255,0,0))

cv2.imshow('mask',img)
cv2.waitKey(0)