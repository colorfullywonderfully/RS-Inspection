import numpy as np

def map(img):
    rows, cols = img.shape
    Im = np.zeros((rows, cols), dtype=np.double)
    for i in range(rows):
        for j in range(cols):
               Im[i, j] = 255/(img.max()-img.min())*(img[i,j]-img.min())
    return Im