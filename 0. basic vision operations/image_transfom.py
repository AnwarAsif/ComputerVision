import numpy as np 
import matplotlib.pyplot as plt 
import cv2 

img = cv2.imread('letterR.jpg',0)
print(img.shape)

# Rotation
trans_img = np.zeros_like(img)

for i, row in enumerate(img): 
    for j, col in enumerate(row):
        trans_img[j,i] = img[i, j]


images = np.hstack([img, trans_img])

plt.imshow(images, cmap='gray')
plt.show()