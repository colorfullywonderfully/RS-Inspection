
import numpy as np
import cv2
from pylab import *

def convolution(Img):

    p = 50
    # 计数
    count = 0

    #Img  = np.array(cv2.imread('1.jpeg',0),dtype= int64)#直接读为灰度图像
    #plt.imshow(Img,'gray')
    #plt.show()
    #print(Img)
    rows,cols=Img.shape ## 行 列
    #print(rows,cols)
    window = []

    for col_index in range(cols):
        if (col_index + p) > cols:
                break
        
        temp_matrix = Img[:, (col_index) : (col_index + p)]
        count = count + 1
        M = mean(temp_matrix)
        window.append(M)
    _argmax = np.argmax(window)

    return _argmax

