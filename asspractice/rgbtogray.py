import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    img_path = r'E:\Digital-image-ProcessingLab\asspractice\images\horse.jpg'
    rgb_image = plt.imread(img_path)
    r = rgb_image[:,:,0]
    g = rgb_image[:,:,1]
    b = rgb_image[:,:,2]
    gray = r*0.2989 + g*0.5870 + b*0.1140
    print(gray.shape)

    plt.subplot(2,1,1)
    plt.imshow(gray,cmap='gray')
    plt.show()
main()