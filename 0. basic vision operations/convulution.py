import cv2
import numpy as np
import matplotlib.pyplot as plt 

def conv(img, kernel): 
    img_h, img_w = img.shape 
    kernel_h, kernel_w = kernel.shape

    crop_img = img[2:2+ kernel_h, 2:2+kernel_w]
    plt.imshow(crop_img,cmap='gray')
    # plt.show()

    # find the kernel centre 
    centre_h = np.int8((kernel_h/2))
    centre_w = np.int8((kernel_w/2))
    print(centre_h)
 
    conv_img = np.copy(img)
    for i in range(img_h - centre_h): 
        for j in range(img_w - centre_w): 
            conv[i][j]
    return conv_img 
if __name__ == "__main__":

    img = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    img.append([1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1])
    img.append([1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,1])
    img.append([1,1,1,1,0,0,0,3,3,3,3,3,0,3,1,1,1,1])
    img.append([1,1,1,0,3,0,3,3,3,3,3,3,0,3,3,3,1,1])
    img.append([1,1,1,0,3,0,0,3,3,3,3,3,3,0,3,3,3,1])
    img.append([1,1,1,0,0,3,3,3,3,3,3,3,0,0,0,0,1,1])
    img.append([1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,1,1,1])
    img.append([1,1,1,1,0,0,2,0,0,0,0,2,0,1,1,1,1,1])
    img.append([1,1,1,0,0,0,2,0,0,0,0,2,0,0,0,1,1,1])
    img.append([1,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,1])
    img.append([1,3,3,3,0,2,3,2,2,2,2,3,2,0,3,3,3,1])
    img.append([1,3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,3,1])
    img.append([1,3,3,3,2,2,2,2,1,1,2,2,2,2,3,3,3,1])
    img.append([1,1,1,1,2,2,2,1,1,1,1,2,2,2,1,1,1,1])
    img.append([1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1])
    img.append([1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1])
    img.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

    img = np.array(img)
    img = np.float32(img)
    kernel = np.array([1/9 for i in range(9)]).reshape((3,3))
    # print(kernel)
    conv_img = conv(img, kernel)
    plt.imshow(conv_img,cmap='gray')
    # plt.savefig('mario.png')
    plt.show()