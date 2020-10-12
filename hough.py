import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def hough(img_edge,img):

    lines = cv2.HoughLines(img_edge,1,np.pi/180,118)  #这里对最后一个参数使用了经验型的值

    #print("result",lines)
    for line in lines[0]:
        rho = line[0] #第一个元素是距离rho
        theta= line[1] #第二个元素是角度theta
        #print (rho)
        #print (theta)
        if  (theta < (np.pi/4. )) or (theta > (3.*np.pi/4.0)): #垂直直线
                    #该直线与第一行的交点
            pt1 = (int(rho/np.cos(theta)),0)
            #该直线与最后一行的焦点
            pt2 = (int((rho-img.shape[0]*np.sin(theta))/np.cos(theta)),img.shape[0])
            #绘制一条白线
            #cv2.line( img, pt1, pt2, (255))
        else: #水平直线
            # 该直线与第一列的交点
            pt1 = (0,int(rho/np.sin(theta)))
            #该直线与最后一列的交点
            pt2 = (img.shape[1], int((rho-img.shape[1]*np.cos(theta))/np.sin(theta)))
            #绘制一条直线
            #cv2.line(img, pt1, pt2, (255,255,255), 8)
    k=(np.arctan((np.double((rho-img.shape[1]*np.cos(theta))/np.sin(theta))-np.double(rho/np.sin(theta)))/(img.shape[1])))*57.297#180/3.1415
    # print(k)
    # print(pt1)
    # print(pt2)
    # print((int((rho-img.shape[1]*np.cos(theta))/np.sin(theta))-int(rho/np.sin(theta)))/(img.shape[1]))

    return k