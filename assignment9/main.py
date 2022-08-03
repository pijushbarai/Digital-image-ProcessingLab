import numpy as np
import cv2
import matplotlib.pyplot as plt
def Display(images,titles):
    index = 1
    n = len(images)
    x = int(n/2)
    y = int(n/2)+1
    print(n)
    for index in range(n):
        plt.subplot(x,y,index+1)
        plt.title(titles[index])
        plt.imshow(images[index],cmap='gray')
def main():
    img_path = r'E:\Digital-image-ProcessingLab\assignment9\images\tree.jpg'
    img = cv2.imread(img_path,0)
    struct_element = np.ones((3,3))
    images = []
    titles = []
    ret,binary_image = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    images.append(binary_image)
    titles.append('Binary Images')
    erosion_image = cv2.erode(binary_image,struct_element,iterations=1)
    images.append(erosion_image)
    titles.append('Erosion Image')
    dilation_image = cv2.dilate(binary_image,struct_element,iterations=1)
    images.append(dilation_image)
    titles.append('Dilated Images')
    opening_image = cv2.dilate(erosion_image,struct_element,iterations=1)
    images.append(opening_image)
    titles.append('Opening Images')
    closing_image = cv2.erode(dilation_image,struct_element,iterations=1)
    images.append(closing_image)
    titles.append('Closing images')
    Display(images,titles)
    plt.show()
main()