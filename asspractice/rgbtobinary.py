import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = r'E:\Digital-image-ProcessingLab\asspractice\images\horse.jpg'
    rgb_image = plt.imread(img_path)

    r = rgb_image[:,:,0]
    g = rgb_image[:,:,1]
    b = rgb_image[:,:,2]

    # grayscale_image = r*0.2989 + g*0.5870 + b*0.1140
    grayscale_image = cv2.cvtColor(rgb_image,cv2.COLOR_RGB2GRAY)

    w,h = grayscale_image.shape
    binary_image = np.zeros((w,h))
    for i in range(w):
        for j in range(h):
            if(grayscale_image[i,j] >= 127):
                binary_image[i,j] = 255

    plt.subplot(2,2,1)
    plt.imshow(grayscale_image,cmap='gray')
    plt.subplot(2,2,2)
    plt.imshow(binary_image,cmap='binary')



    plt.show()

    


main()