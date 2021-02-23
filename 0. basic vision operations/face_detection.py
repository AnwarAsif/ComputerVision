import cv2

face_cascade = cv2.CascadeClassifier('frontalFace10/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('frontalEyes35x16.xml')

#img = cv2.imread('lena.png')
img = cv2.imread('faces.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
eyes = eyes_cascade.detectMultiScale(img_gray, 1.1,4)

for (x,y,w,h) in faces: 
    cv2.rectangle(img, (x,y), (x+w, y+h), (100,100,100),4)
    cv2.putText(img, 'Face',(x,y-10), cv2.FORMATTER_FMT_MATLAB, 2, (255,0,0), 2, cv2.LINE_AA)

for (x,y,w,h) in eyes:
    cv2.rectangle(img, (x,y), (x+w,y+h), (200,200,20),4)
    cv2.putText(img, 'eyes', (x,y-5), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 1, cv2.LINE_AA)

cv2.imshow('Image', img)
cv2.waitKey(0)
