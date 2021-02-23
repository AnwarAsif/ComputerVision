import cv2

# import image
img = cv2.imread('lena.png')

#cv2.imshow('image',img)
#cv2.waitKey(0)

# import video 
cap = cv2.VideoCapture('Football.mp4')

# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#     if cv2.waitKey(1) & 0xFF== ord('q'):
#         break

# import webcam

cap = cv2.VideoCapture(0)
print(cap.isOpened())
print('test')

# cap.set(3,640)
# cap.set(4,480)

# while True:
#     success, img = cap.read()
#     cv2.imshow("web cam", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break