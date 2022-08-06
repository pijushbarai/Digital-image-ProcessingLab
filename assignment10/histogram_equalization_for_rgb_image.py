from asyncio.windows_events import NULL
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
    for i in range(n):
        plt.subplot(x,y,i+1)
        plt.title(titles[i]) 
        plt.subplot(x,y,i+1)
        plt.title(titles[i])
        if(cmaps[i] == 'hist'):
            plt.hist(images[i].ravel(),256,[0,255])
            continue
        elif (cmaps[i] == 'null'):
            plt.imshow(images[i])
            continue
        plt.imshow(images[i],cmap=cmaps[i])

def main():
    # img_path = r'E:\Digital-image-ProcessingLab\assignment10\images\forest.jpg'
    img_path = r'E:\Digital-image-ProcessingLab\assignment9\images\pranta.jpg'

    img = plt.imread(img_path)

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

    # convert the YUV image back to RGB format
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    appending(img,'Original Image','null')
    # appending(img,'Original Hist','hist')
    appending(img_output,'Histogram equalized image','null')
    
    # appending(img_output,'output Hist','hist')
    Display()
    plt.show()

main()

