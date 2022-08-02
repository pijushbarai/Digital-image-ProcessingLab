import cv2
from matplotlib import pyplot as plt
import numpy as np


def main():
    image_path = r'images\sk1.jpg'
    img = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    ret,thresh_img = cv2.threshold(grayscale_image,127,255,cv2.THRESH_BINARY) 
    thresh_img ^= 255
    kernel = np.ones((3, 3), np.uint8)
    img_erosion = cv2.erode(thresh_img, kernel, iterations=1)
    img_dilation = cv2.dilate(thresh_img, kernel, iterations=1)
    img_opening = cv2.dilate(img_erosion,kernel)
    img_closing = cv2.erode(img_dilation,kernel)
    plt.subplot(3,2,1)
    plt.title('input')
    plt.imshow(thresh_img,cmap='gray')
    plt.subplot(3,2,2)
    plt.title('erotion')
    plt.imshow(img_erosion,cmap='gray')
    plt.subplot(3,2,3)
    plt.title('dialation')
    plt.imshow(img_dilation,cmap='gray')
    plt.subplot(3,2,4)
    plt.title('opening')
    plt.imshow(img_opening,cmap='gray')
    plt.subplot(3,2,5)
    plt.title('closint')
    plt.imshow(img_closing,cmap='gray')

    plt.savefig('out_sk1.png')

    plt.show()
main()