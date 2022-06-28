from operator import ne
import random
from cv2 import imread, medianBlur
import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
import math



def show_image(row,col,pos,img,title):
    plt.subplot(row,col,pos)
    plt.title(title)
    plt.imshow(img,cmap='gray')

def main():
    path = r'E:\Digital-image-ProcessingLab\assinment6\images\bird2.jpg'
    rgb_image = imread(path)
    grayscale_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    grayscale_image = cv2.resize(grayscale_image, (580,480))
    
    averageKernel = np.array([[1,1,1,],[1,1,1],[1,1,1]])/9
    gaussianBlurKarnel = np.array([[1,2,1],[2,4,2],[1,2,1]])/16
    averageKernelProcessedgrayscale= cv2.filter2D(grayscale_image,-1,averageKernel)

    row,col = grayscale_image.shape
    noiseNumber = int((row*col)/16)
    # print(noiseNumber,row,col)
    noisyImage = np.copy(grayscale_image)
    for i in range(noiseNumber):
        value = random.randint(0,1)
        x = random.randint(0,row-1)
        y = random.randint(0,col-1)
        noisyImage[x][y] = value*255

    averageKernelProcessedNoisyImage = cv2.filter2D(noisyImage,-1,averageKernel)
    gaussianBlurKarnelProcessedNoisyImage = cv2.filter2D(noisyImage,-1,gaussianBlurKarnel)
    # https://medium.com/@florestony5454/median-filtering-with-python-and-opencv-2bce390be0d1
    medianBluredImage = cv2.medianBlur(noisyImage,5)
    show_image(2,3,1,grayscale_image,'Grayscale Image')
    show_image(2,3,2,averageKernelProcessedgrayscale,'Grayscale Image filtered(AVG)')
    show_image(2,3,3,noisyImage,'Noisy Image(Salt and Pepper)')
    show_image(2,3,4,averageKernelProcessedNoisyImage,'Noisy image filtered(AVG)')
    show_image(2,3,5,gaussianBlurKarnelProcessedNoisyImage,'Noisy Image filtered(Gaussian)')
    show_image(2,3,6,medianBluredImage,'Noisy Image Filtered(MEDIAN)')
    
    plt.savefig('saltAndPepperNoise.png')
    plt.show()


    


main()