from operator import ne
from cv2 import Laplacian, imread
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
    grayscale_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
    LaplacianFilter = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    horizontalSobelFilter = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    verticalSobelFilter = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    LaplacianFilterProcessed = cv2.filter2D(grayscale_image, -1, LaplacianFilter)
    horizontalSobelFilterProcessed = cv2.filter2D(grayscale_image,-1,horizontalSobelFilter)
    verticalSobelFilterProcessed = cv2.filter2D(grayscale_image,-1,verticalSobelFilter)

    show_image(3,3,1,grayscale_image,'Gray scale')
    show_image(3,3,2,LaplacianFilterProcessed,'Laplacian filter')
    show_image(3,3,3,horizontalSobelFilterProcessed,'Horizontal Sobel')
    show_image(3,3,8,verticalSobelFilterProcessed,'Vertical Sobel')

    plt.savefig('laplacianAndsobelfilter.png')
    plt.show()

main()