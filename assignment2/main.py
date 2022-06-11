import math
from cv2 import imread, log
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image

def main():
    img_path = r'E:\Digital-image-ProcessingLab\assignment2\images\download.jpg'
    img = plt.imread(img_path)
    grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    x,y = grayscale.shape
    print(x,y)
    t1 = 20
    t2 = 150
    c = 25
    p = 3

    condition1 = grayscale
    epsilon = 0.0000001
    for i in range(x):
        for j in range(y):
            if(grayscale[i][j] >= t1 and grayscale[i][j] <= t2):
                condition1[i][j] = 100
            else:
                condition1[i][j] = 10

    grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    condition2 = grayscale
    for i in range(x):
        for j in range(y):
            if(grayscale[i][j] >= t1 and grayscale[i][j] <=t2):
                condition2[i][j] = 100
            else:
                condition2[i][j] = grayscale[i][j]

    grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    condition3 = grayscale
    for i in range(x):
        for j in range(y):
            temp = c * math.log(1+grayscale[i][j],10)
            if(temp <= 255 and temp >=0):
                condition3[i][j] = temp
            elif(temp < 0):
                condition3[i][j] = 0
            elif(temp > 255):
                condition3[i][j] = 255

    grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    condition4 = grayscale
    for i in range(x):
        for j in range(y):
            condition4[i][j] = c * pow((grayscale[i][j]+epsilon),p)
            
    plt.subplot(2,2,1)
    plt.title('Condition1 image')
    plt.imshow(condition1,cmap='gray')

    plt.subplot(2,2,2)
    plt.title('condition2 image')
    plt.imshow(condition2,cmap='gray')

    plt.subplot(2,2,3)
    plt.title('codition3 image')
    plt.imshow(condition3,cmap='gray')

    plt.subplot(2,2,4)
    plt.title('condition4 image')
    plt.imshow(condition4,cmap='gray')
   

  
    plt.show()
main()