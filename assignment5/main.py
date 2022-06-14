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
    w,h = grayscale_image.shape
    new_image = np.zeros((8,w,h))
    restore_image = np.zeros((w,h))
    bits = [1,2,4,8,16,32,64,128]
    for i in range(w):
        for j in range(h):
            for k in range(8):
                new_image[k][i][j] = grayscale_image[i][j] & bits[k]
    show_image(3,4,1,grayscale_image,'Gray Image')
    show_image(3,4,2,new_image[0],'0 bit-slicing')
    show_image(3,4,3,new_image[1],'1 bit-slicing')
    show_image(3,4,4,new_image[2],'2 bit-slicing')
    show_image(3,4,5,new_image[3],'3 bit-slicing')
    show_image(3,4,6,new_image[4],'4 bit-slicing')
    show_image(3,4,7,new_image[5],'5 bit-slicing')
    show_image(3,4,8,new_image[6],'6 bit-slicing')
    show_image(3,4,9,new_image[7],'7 bit-slicing')
    for i in range(w):
        for j in range(h):
            for k in range(8):
                restore_image[i][j] += new_image[k][i][j]
    show_image(3,4,10,restore_image,'Restored Image')
    plt.savefig('bitslicing.png')
    plt.show()
main()
