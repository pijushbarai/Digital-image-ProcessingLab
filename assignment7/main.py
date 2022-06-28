from turtle import color
import cv2
import matplotlib.pyplot as plt
import numpy as np

def showImage(row,col,pos,img,title):
    plt.subplot(row,col,pos)
    plt.imshow(img,cmap='gray')
    plt.title(title)

def showHist(row,col,pos,img,title):
    plt.subplot(row,col,pos)
    plt.plot(img,color= 'r')
    plt.title(title)

def main():
    image_path = r'E:\Digital-image-ProcessingLab\assignment7\images\photo.jpg'
    rgbImage = plt.imread(image_path)
    grayscale = cv2.cvtColor(rgbImage,cv2.COLOR_RGB2GRAY)
    newImage1 = np.copy(grayscale)
    newImage2 = np.copy(grayscale)
    newImage3 = np.copy(grayscale)
    r,c = grayscale.shape
    for i in range(r):
        for j in range(c):
            if(grayscale[i][j] < 100):
                newImage1[i][j] = newImage1[i][j] + 100
                if(newImage3[i][j] + 100 > 155):
                    newImage3[i][j] = 155
                else:
                    newImage3[i][j] = newImage3[i][j] + 100
            if(grayscale[i][j] > 155):
                newImage2[i][j] = newImage2[i][j]-100
                if((newImage3[i][j]-100) < 100):
                    newImage3[i][j] = 100
                else:
                    newImage3[i][j] = (newImage3[i][j]-100)
            
    grayscaleHist = cv2.calcHist([grayscale],[0],None,[256],[0,256])
    newImage1Hist = cv2.calcHist([newImage1],[0],None,[256],[0,256])
    newImage2Hist = cv2.calcHist([newImage2],[0],None,[256],[0,256])
    newImage3Hist = cv2.calcHist([newImage3],[0],None,[256],[0,256])
    showImage(4,2,1,grayscale,'Grayscale Image')
    showHist(4,2,2,grayscaleHist,'Grayscale Hist')
    showImage(4,2,3,newImage1,'')
    showHist(4,2,4,newImage1Hist,'Moved Right')
    showImage(4,2,5,newImage2,'')
    showHist(4,2,6,newImage2Hist,'Moved left')
    showImage(4,2,7,newImage3,'')
    showHist(4,2,8,newImage3Hist,'Narrow Band')
    
    plt.savefig('paddyfieldHistogram.png')
    plt.show()
main()