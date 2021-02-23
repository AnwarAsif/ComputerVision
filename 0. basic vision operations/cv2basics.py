from os import pathconf
import cv2
import sys
import matplotlib.pyplot as plt

def load_and_display(path='none'):
    if path == 'none': 
        sys.exit('file path not defined')

    img = cv2.imread(path)

    if img is None:
        sys.exit("Could not read the image.")

    plt.imshow(img)
    plt.show()

    return img

def basic_operation(img):
    pass

if __name__ == "__main__":

    img_path = 'test.jpg'
    img = load_and_display(path=img_path)

    basic_operation(img)

