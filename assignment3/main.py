import math
from cv2 import GaussianBlur, imread, log
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image


def main():
    img_path = r'E:\Digital-image-ProcessingLab\assignment3\images\flower.jpeg'
    img = plt.imread(img_path)
    plt.subplot(3,3,1)
    plt.title('main image')
    plt.imshow(img)
    

    #kernels
    kernels = np.ones([3,3])
    print(kernels)
    identityKernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
    ridgeDitectionKernel = np.array([[-1,-1,-1],[-1,16,-1],[-1,-1,-1]])
    ridgeDitectionKernel2 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    sharpenKarnel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    boxBlurKarnel = np.array([[1,1,1],[1,1,1],[1,1,1]])/9
    gaussianBlurKarnel = np.array([[1,2,1],[2,4,2],[1,2,1]])/16

    grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    plt.subplot(3,3,2)
    plt.title('grayscale image')
    plt.imshow(grayscale,cmap='gray')

    identityKernelProcessed = cv2.filter2D(grayscale, -1, identityKernel)
    ridgeDitectionKernelProcessed = cv2.filter2D(grayscale, -1, ridgeDitectionKernel)
    ridgeDitectionKernel2Processed = cv2.filter2D(grayscale, -1, ridgeDitectionKernel2)
    sharpenKarnelProcessed = cv2.filter2D(grayscale, -1, sharpenKarnel)
    boxBlurKarnelProcessed = cv2.filter2D(grayscale, -1, boxBlurKarnel)
    gaussianBlurKarnelProcessed = cv2.filter2D(grayscale,-1,gaussianBlurKarnel)


    plt.subplot(3,3,3)
    plt.title('identity karnel')
    plt.imshow(identityKernelProcessed,cmap='gray')

    plt.subplot(3,3,4)
    plt.title('ridge Ditection karnel')
    plt.imshow(ridgeDitectionKernelProcessed,cmap='gray')

    plt.subplot(3,3,5)
    plt.title('Ridge Ditection karnel 2')
    plt.imshow(ridgeDitectionKernel2Processed,cmap='gray')

    plt.subplot(3,3,6)
    plt.title('Sharpen Karnel')
    plt.imshow(sharpenKarnelProcessed,cmap='gray')

    plt.subplot(3,3,7)
    plt.title('Box Blour Karnel')
    plt.imshow(boxBlurKarnelProcessed,cmap='gray')
    
    plt.subplot(3,3,8)
    plt.title('Gaussian Karnel')
    plt.imshow(gaussianBlurKarnelProcessed,cmap='gray')

    plt.show()

main()