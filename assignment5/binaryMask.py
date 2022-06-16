from operator import ne
from cv2 import imread
import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
import math

def show_image(row,col,pos,img,title):
    plt.subplot(row,col,pos)
    plt.title(title)
    plt.imshow(img,cmap='gray')

def main():
    path = r'E:\Digital-image-ProcessingLab\assignment5\image\bird.jpg'
    rgb_image = imread(path)
    grayscale_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    binary_mask = np.zeros(grayscale_image.shape, dtype=np.uint8)
    binary_mask = cv2.circle(binary_mask, (600, 400), 300, (255,255,255), -1)
    result = cv2.bitwise_and(grayscale_image, binary_mask)

    show_image(2,3,1,grayscale_image,'Grayscale Image')
    show_image(2,3,2,binary_mask,'Binary Mask')
    show_image(2,3,3,result,'After Masking')

    plt.savefig('binaryMask.png')
    plt.show()

    


main()