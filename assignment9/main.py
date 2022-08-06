import numpy as np
import cv2
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
        plt.imshow(images[i],cmap=cmaps[i])

def zero_padding (binary_image,struct_element):
    w,h = binary_image.shape
    m,n = struct_element.shape
    padding_image = np.zeros(shape=(w + int(m/2)*2,h + int(n/2)*2))
    w,h = padding_image.shape
    padding_image[int(m/2):w-int(m/2),int(n/2):h-int(n/2)] = binary_image
    return padding_image

def one_padding(binary_image,struct_element):
    w,h = binary_image.shape
    m,n = struct_element.shape
    padding_image = np.ones(shape=(w + int(m/2)*2,h + int(n/2)*2))
    w,h = padding_image.shape
    padding_image[int(m/2):w-int(m/2),int(n/2):h-int(n/2)] = binary_image
    return padding_image
    
def custom_dilate(binary_image,struct_element):
    padded_image = zero_padding(binary_image,struct_element)
    new_image = np.copy(binary_image)
    m,n = struct_element.shape
    w,h = new_image.shape
    for i in range(w):
        for j in range(h):
            kernel = padded_image[i:i+m,j:j+n]
            new_image[i][j] = np.sum(np.multiply(struct_element,kernel))
            if new_image[i,j] > 0:
                new_image[i,j] = 255
    
    return new_image


def custom_erode(binary_image,struct_element):
    new_image = np.copy(binary_image)
    padded_image = one_padding(binary_image,struct_element)
    m,n = struct_element.shape
    w,h = new_image.shape
    sum = 0
    sum = int(np.sum(struct_element[0:m,0:n]))
    for i in range(w):
        for j in range(h):
            kernel = padded_image[i:i+m,j:j+n]
            new = np.sum(np.multiply(kernel,struct_element))
            if(sum*255 == new):
                new_image[i,j] = 255
            else:
                new_image[i,j] = 0
    
    return new_image
def main():
    img_path = r'E:\Digital-image-ProcessingLab\assignment9\images\tree.jpg'

    img = cv2.imread(img_path,0)
    struct_element = np.ones((5,3))
    
    ret,binary_image = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    binary_image ^= 255

    # morphological operation by built in methods
    erosion_image = cv2.erode(binary_image,struct_element,iterations=1)
    dilation_image = cv2.dilate(binary_image,struct_element,iterations=1)
    opening_image = cv2.dilate(erosion_image,struct_element,iterations=1)
    closing_image = cv2.erode(dilation_image,struct_element,iterations=1)
    
    # morphological operation by custom boult methods
    custom_dilate_image = custom_dilate(binary_image,struct_element)
    custom_erod_image = custom_erode(binary_image,struct_element)
    custom_opening_image = custom_dilate(custom_erod_image,struct_element)
    custom_closing_image = custom_erode(custom_dilate_image,struct_element)

    
    # appending items in list to display
    appending(binary_image,'Binary Image','binary')
    appending(dilation_image,'Built in Dilate Image','binary')
    appending(custom_dilate_image,'Custom Dilate','binary')   
    appending(erosion_image,'Built in Erode','binary')
    appending(custom_erod_image,'Custom erosion','binary')
    appending(opening_image,'Built in Opening','binary')
    appending(custom_opening_image,'Custom Opening Image','binary')
    appending(closing_image,'Built in Closing','binary')
    appending(custom_closing_image,'Custom closing image','binary')

    Display()
    plt.show()
main()