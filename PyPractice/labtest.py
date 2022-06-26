import cv2
from matplotlib import pyplot as plt
import numpy as np


if __name__ == '__main__':
    img_path = r'E:\Digital-image-ProcessingLab\assinment6\images\bird2.jpg'
    rgb_image = plt.imread(img_path)
    red_chanel = rgb_image[:,:,0]
    green_chanel = rgb_image[:,:,1]
    blue_chanel = rgb_image[:,:,2]
    row,col,_ = rgb_image.shape
    gray = np.copy(rgb_image)
    for i in range(row):
        for j in range(col):
            gray[i][j] = 0.299*red_chanel[i][j] + 0.587*green_chanel[i][j] + 0.114*blue_chanel[i][j]

    plt.subplot(2,2,1)
    plt.imshow(gray)
    plt.show()