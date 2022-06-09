from cv2 import imread
import numpy as np
import matplotlib.pyplot as plt
import cv2

def main():
    img_path = r'E:\Digital-image-ProcessingLab\assignment1\images\pigeon.jpg'
    img = plt.imread(img_path)
    grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    
    print(img,img.max(),img.min(),img.shape)
    plt.imshow(grayscale,cmap='gray')
    plt.show()
main()