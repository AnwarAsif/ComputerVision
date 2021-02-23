import cv2 

cap = cv2.VideoCapture('Football.mp4')

for i in range(1): 
    _, frame = cap.read()
    cv2.imwrite('ball.png',frame)
