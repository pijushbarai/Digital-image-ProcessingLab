import matplotlib.pyplot as plt
import cv2
import numpy as np



def main():
    img_path = r'E:\Digital-image-ProcessingLab\asspractice\images\horse.jpg'
    rgb_image = plt.imread(img_path)
    grayscale_image = cv2.cvtColor(rgb_image,cv2.COLOR_BGR2GRAY)
    w,h = grayscale_image.shape
    new_image = np.zeros((8,w,h))
    bits = [1,2,4,8,16,32,64,128]

    for i in range(w):
        for j in range(h):
            for k in range(8):
                new_image[k,i,j] = grayscale_image[i,j] & bits[k]
    
    plt.subplot(1,1,1)
    plt.imshow(new_image[6],cmap='gray')
    plt.show()

main()