newimage = np.zeros((w-2,h-2))
    m,n = kernel.shape
    for i in range(w):
        for j in range (h):
            kernel2 = grayscale_image[i:i+m,j:j+n]
            newimage[i][j] = np.sum(np.multiply(kernel,kernel2))