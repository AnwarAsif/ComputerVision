import cv2 
import numpy as np 


def getContours(img):
    
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for con in contours: 
        area = cv2.contourArea(con)
        if area > 500:
            cv2.drawContours(cont_img, con, -1, (255,255,0),5)
            peri = cv2.arcLength(con, True)
            aprox = cv2.approxPolyDP(con, 0.02*peri, True)
            #print(len(aprox))
            obj_cor = len(aprox)
            print(obj_cor)
            x,y,w, h = cv2.boundingRect(aprox)
            if obj_cor == 3: 
                cv2.rectangle(cont_img, (x,y),(x+w,y+h), (0,0,255),2)
                cv2.putText(cont_img, 'Triangle',(x+100,y+100), cv2.FORMATTER_FMT_MATLAB, 3, (255,0,0), 3, cv2.LINE_AA)
            else: 
                cv2.putText(cont_img, 'Not a Triangle', (x+100,y+100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0,255,0), 4, cv2.LINE_AA)

img = cv2.imread('shapes2.jpg')
#img = cv2.imread('shapes3.png')
cont_img = img.copy()
img_blur = cv2.GaussianBlur(img, (7,7), .7)
img_canny = cv2.Canny(img_blur,40,50)
getContours(img_canny)

bk = np.stack((img_canny,)*3, axis=-1)
stk= np.hstack([img, img_blur, bk, cont_img])
stk = cv2.resize(stk, (800,250))



cv2.imshow('images', stk)
cv2.waitKey(0)