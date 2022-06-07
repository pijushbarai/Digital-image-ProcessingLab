import matplotlib.pyplot as plt
import cv2

def main():
    img_path = r'E:\Digital-image-ProcessingLab\assignment1\images\nature.jpg'
    print(img_path)
    rgb = plt.imread(img_path)
    print(rgb.shape, rgb.max(), rgb.min())

    red = rgb[:, :, 0]
    green = rgb[:, :, 1]
    blue = rgb[:, :, 2]
    print(red.shape, red.max(), red.min())

    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    print(grayscale.shape, grayscale.max(), grayscale.min())

    _, binary = cv2.threshold(grayscale, 50, 255, cv2.THRESH_BINARY)

    plt.figure(figsize=(40, 40))
    plt.subplot(6,2,1)
    plt.title('Rgb image')
    plt.imshow(rgb)
    
    plt.subplot(6,2,2)
    plt.title('Rgb Histogram')
    plt.hist(rgb.ravel(),256,[0,256])

    plt.subplot(6,2,3)
    plt.title('Red chanel')
    plt.imshow(red,cmap='Reds')
    
    plt.subplot(6,2,4)
    plt.title('Red Histogram')
    plt.hist(red.ravel(),256,[0,256])

    plt.subplot(6,2,5)
    plt.title('Green chanel')
    plt.imshow(green,cmap='Greens')
    
    plt.subplot(6,2,6)
    plt.title('Green Histogram')
    plt.hist(green.ravel(),256,[0,256])

    plt.subplot(6,2,7)
    plt.title('Blue chalel')
    plt.imshow(red,cmap='Blues')
    
    plt.subplot(6,2,8)
    plt.title('Blue Histogram')
    plt.hist(blue.ravel(),256,[0,256])


    plt.subplot(6,2,9)
    plt.title('Grayscale images')
    plt.imshow(grayscale,cmap='gray')
    
    plt.subplot(6,2,10)
    plt.title('Gray Histogram')
    plt.hist(grayscale.ravel(),256,[0,256])


    plt.subplot(6,2,11)
    plt.title('Binary image')
    plt.imshow(binary,cmap='binary')
    
    plt.subplot(6,2,12)
    plt.title('Binary Histogram')
    plt.hist(blue.ravel(),256,[0,256])

    plt.show()
	
main()
