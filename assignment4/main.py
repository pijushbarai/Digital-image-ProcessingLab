import math
from cv2 import imread, log
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image

def main():
    img_path = r'E:\Digital-image-ProcessingLab\assignment4\images\cat.jpeg'
    img = plt.imread(img_path)
    grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    
    grayscale = grayscale.reshape(-1)
    print(grayscale.shape)


    x = np.arange(0,256)
    y = np.zeros((256),dtype=int)
    for i in range(len(grayscale)):
        y[grayscale[i]] += 1
    
    plt.subplot(2,2,1)
    plt.title('Own build hisr function')
    plt.bar(x,y,width=1)

    plt.subplot(2,2,2)
    plt.title('Hist function')
    plt.hist(grayscale.ravel(),256,[0,256])

    grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    w,h = grayscale.shape
    paddingImage = np.zeros(shape=(w+2,h+2))
    w,h = paddingImage.shape
    paddingImage[1:w-1,1:h-1] = grayscale
    
    ridgeDitectionKernel2 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    ridgeDitectionKernel2Processed = cv2.filter2D(grayscale, -1, ridgeDitectionKernel2)
    _,k = ridgeDitectionKernel2.shape

    new_width = w-k +1
    new_height = h-k +1
    modified_image = np.zeros(shape=(new_width,new_height))
    print(modified_image.shape)
    for i in range(new_width):
        for j in range(new_height):
            kernel = paddingImage[i:i+k,j:j+k]
            modified_image[i,j] = np.sum(np.multiply(ridgeDitectionKernel2,kernel))
            if(modified_image[i,j] < 0):
                modified_image[i,j] = 0
            elif(modified_image[i,j] > 255):
                modified_image[i,j] = 255

    

    plt.subplot(2,2,3)
    plt.title('Own Build filter')
    plt.imshow(modified_image,cmap='gray')

    plt.subplot(2,2,4)
    plt.title('Buildin filtered')
    plt.imshow(ridgeDitectionKernel2Processed,cmap='gray')


    plt.show()



main()