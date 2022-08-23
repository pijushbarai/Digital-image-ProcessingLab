import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path = r'E:\Digital-image-ProcessingLab\asspractice\images\horse.jpg'
    rgb_image = plt.imread(img_path)
    grayscale_image = cv2.cvtColor(rgb_image,cv2.COLOR_BGR2GRAY)

    kernel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    
    w,h = grayscale_image.shape
    print(grayscale_image.shape)
    paddedImage = np.zeros((w+2,h+2))
    print(paddedImage.shape)
    w,h = paddedImage.shape
    paddedImage[1:w-1,1:h-1] = grayscale_image
    newimage = np.zeros((w-2,h-2))
    print(newimage.shape)
    w,h = newimage.shape
    for i in range(w):
        for j in range (h):

            kernel2 = paddedImage[i:i+3,j:j+3]
            newimage[i][j] = np.sum(np.multiply(kernel,kernel2))
    
    plt.subplot(1,1,1)
    plt.imshow(newimage,cmap='gray')
    plt.show()

main()