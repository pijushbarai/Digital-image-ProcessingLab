# to print in rgb channel cmap = brg
import cv2
import numpy as np
import matplotlib.pyplot as plt

images = []
titles = []
cmaps = []

def appending(img,title,map):
    images.append(img)
    titles.append(title)
    cmaps.append(map)

def Display():
    n = len(images)
    
    x = int((np.sqrt(n)))
    y = int(np.ceil(n/x))
    if(x == 0):
        x = 1
    for i in range(n):
        
        plt.subplot(x,y,i+1)
        plt.title(titles[i]) 
        plt.subplot(x,y,i+1)
        plt.title(titles[i])
        if(cmaps[i] == 'hist'):
            plt.hist(images[i].ravel(),256,[0,255])
            continue
        plt.imshow(images[i],cmap=cmaps[i])
def main():
    img_path = r'E:\Digital-image-ProcessingLab\assignment10\images\low.jpg'
    
    img = cv2.imread(img_path,0)
    equalized_img = cv2.equalizeHist(img)
    plt.subplot(1,1,1)
    appending(img,'Grayscale image','gray')
    appending(img,'Grayscale Hist','hist')
    appending(equalized_img,'Equalized Image','gray')
    appending(equalized_img,'Equalized Image Hist','hist')
    Display()
    plt.savefig("output.png")
    plt.show()
main()