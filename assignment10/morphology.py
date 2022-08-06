import cv2
import matplotlib.pyplot as plt
import numpy as np

src_img = np.array([
    [1,1,0,1,0,0,0,0],
    [1,1,1,0,0,0,0,0],
    [0,1,0,1,0,0,0,1],
    [0,0,1,0,0,0,1,0],
    [0,0,0,1,1,1,0,0],
    [0,1,0,0,0,0,1,0],
    [0,0,1,1,1,1,0,0]
],np.uint8)

kernel = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
],dtype=np.uint8)

erosion = cv2.erode(src_img,kernel,iterations=1,borderType=cv2.BORDER_REFLECT)
img_set = [src_img,kernel,erosion]

plt.figure(figsize=(10,10))
for i in range(len(img_set)):
    plt.subplot(2,2,i+1)
    plt.imshow(img_set[i],cmap='gray')
 
plt.show()
