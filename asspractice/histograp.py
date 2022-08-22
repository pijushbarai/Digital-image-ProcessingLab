import matplotlib.pyplot as plt
import cv2
import numpy as np




def main():
    img_path = r'E:\Digital-image-ProcessingLab\asspractice\images\horse.jpg'
    rgb_image = plt.imread(img_path)
    grayscale_image = cv2.cvtColor(rgb_image,cv2.COLOR_RGB2GRAY)
    grayscale_image = grayscale_image.reshape(-1)
    print(grayscale_image.shape)
    # x = np.arange(0,255)
    # y = np.zeros((256))
    # for i in range(len(grayscale_image)):
    #     y[grayscale_image[i]] +=1

    x = np.arange(0,256)
    y = np.zeros((256))
    for i in range(len(grayscale_image)):
        y[grayscale_image[i]] += 1

    plt.subplot(2,2,1)
    # plt.imshow(grayscale_image)
    plt.bar(x,y,width=1)
    plt.show()

main()