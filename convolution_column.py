import numpy as np
import cv2
from pylab import *

def convolution(Img):
    row_p=20
    col_p=1
    count = 0
    Img=double(Img)

    #Img  = np.array(cv2.imread('1.jpeg',0),dtype= int64)#直接读为灰度图像

    rows,cols=Img.shape ## 行 列
    Img22 = np.zeros((rows, cols), dtype=np.double)
    #print(rows,cols)
    #plt.imshow(Img, cmap='gray')
    #plt.show()
    for row_index in range(rows):
        for col_index in range(cols):

            if row_index - row_p < 0 and col_index - col_p < 0:

               temp_matrix = Img[0:row_index+row_p+abs(row_index - row_p),  0:col_index+col_p+abs(col_index - col_p)]

            if row_index - row_p < 0 and col_index - col_p > 0:

               temp_matrix = Img[0:row_index+row_p++abs(row_index - row_p),  col_index-col_p:col_index+col_p]

            if row_index - row_p > 0 and col_index - col_p < 0:
                temp_matrix = Img[row_index - row_p:row_index + row_p,   0:col_index + col_p+abs(col_index - col_p)]

            if row_index - row_p > 0 and col_index - col_p > 0:
                temp_matrix = Img[row_index - row_p:row_index + row_p,    col_index - col_p:col_index + col_p]
            count = count + 1

            if Img[row_index, col_index] < mean(temp_matrix):
            #    #print(Img[row_index, col_index]-mean(temp_matrix))
               #Img22[row_index, col_index] = (Img[row_index, col_index] - mean(temp_matrix))/(Img[row_index, col_index] + mean(temp_matrix))

                 # Cxy = sqrt(abs((Img[row_index, col_index] - mean(temp_matrix)) / (Img[row_index, col_index] + mean(temp_matrix))))
                 # Img22[row_index, col_index]= (1-Cxy)/(1+Cxy)*Img[row_index, col_index]
               Img22[row_index, col_index] = (Img[row_index, col_index] - mean(temp_matrix)) /mean(temp_matrix)
               #Img22[row_index, col_index] =Img[row_index, col_index]/np.max(temp_matrix)-1

            #arr = Img22.flatten()
               #Img22[row_index, col_index] = (Img[row_index, col_index] - mean(temp_matrix)) / (var(temp_matrix))
               #Img22[row_index, col_index]=1*Img[row_index, col_index]
            #     #print(Img[row_index, col_index])
            else:
               Img22[row_index, col_index] = 0


    return Img22