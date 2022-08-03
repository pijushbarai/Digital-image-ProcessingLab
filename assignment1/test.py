import imp
import matplotlib.pyplot as plt
import numpy as np
import cv2
def main():
    img_path = r'E:\Digital-image-ProcessingLab\assignment1\images\nature.jpg'
    img = cv2.imread(img_path,0)
    # ret,binary_image = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    w,h = img.shape
    binary = np.zeros((w,h))
    # new_image = np.zeros((8,w,h))
    # bits = [1,2,4,8,16,32,64,128]
    # for i in range(w):
    #     for j in range(h):
    #         for k in range(8):
    #             new_image[k][i][j] = img[i][j] & bits[k]
    for i in range(w):
        for j in range(h):
          if(img[i][j] >= 127):
            binary[i][j] = 1  

    plt.subplot(1,1,1)
    plt.imshow(binary,cmap='gray')
    plt.show()

main()