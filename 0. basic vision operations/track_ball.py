import cv2
import numpy as np 

cap = cv2.VideoCapture('Football.mp4')

def getContours(img):
    
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for con in contours: 
        area = cv2.contourArea(con)
        if area > 500:
            cv2.drawContours(resized, con, -1, (255,255,0),2)
            peri = cv2.arcLength(con, True)
            aprox = cv2.approxPolyDP(con, 0.02*peri, True)
            x,y,w, h = cv2.boundingRect(aprox)
            cv2.rectangle(resized, (x,y),(x+w,y+h), (0,0,255),2)
            cv2.putText(resized, 'Ball',(x, y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, .5, (255,0,100),2)


while True: 
    success, img = cap.read()
    cv2.imshow("video", img)
    scale_percent = 40 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    hsv_img = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

    h_min = 0
    h_max = 179
    s_min = 0
    s_max = 157
    v_min = 174
    v_max = 255

    low = np.array([h_min, s_min, v_min])
    up = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(resized, low, up)
    img_blur = cv2.GaussianBlur(mask, (7,7), 1)
    img_canny = cv2.Canny(img_blur,50,50)
    getContours(img_canny)


    cv2.imshow('video', resized)
    cv2.waitKey(1)
