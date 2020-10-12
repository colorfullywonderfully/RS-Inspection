import cv2
import hough
import rotate
import regionconnect
from pylab import *
from skimage import io, transform
import matplotlib.pyplot as plt
from skimage import data,color,morphology,feature
import Map
import My_MaxEntropy
import convolution_column
import numpy as np
import rail_location
import time
####################################################################1. Read + canny

image  = cv2.imread('input_data/0179.jpg',0) #直接读为灰度图像
edges = cv2.Canny(image, 50, 150, apertureSize = 3)
result = image.copy()

####################################################################2. Hough algorithm + Rotation
k=hough.hough(edges,result)
#img2 = transform.rotate(result,k-90)#归一化 （均值为0 方差为1）

img_rotate = rotate.rotate(image,k-90)

plt.subplot(111)
plt.imshow(img_rotate ,cmap ='gray')
plt.axis('off')
plt.show()
#######################3. HPCG algorithm

W = rail_location.convolution(img_rotate)
img_crop = img_rotate[:,W:(W+50)] 
h, w = img_crop.shape
#######################4. LWLC algorithm

img_crop = img_crop[250:(h-250), 4:(w-3)]
img_nomali=convolution_column.convolution(img_crop)
plt.subplot(111)
plt.imshow(img_crop ,cmap ='gray')
plt.axis('off')
plt.show()
img_map=Map.map(img_nomali)
#######################5. ME algorithm：ignoring < 25mm2

start = time.time()
thre = My_MaxEntropy.My_MaxEntropy(img_map)
end = time.time()
print ("T1=",end - start)
ret,th2=cv2.threshold(img_map,thre,255,cv2.THRESH_BINARY)
#######################6. Imgae Morphology

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1, 8))
# opened = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)
# chull = morphology.convex_hull_object(255-opened)
BIN = ((th2/255)<0.5)*1
sub=morphology.remove_small_objects(BIN, min_size=15, connectivity=2, in_place=True)
#######################7. label

fig,(ax0,ax1)= plt.subplots(1,2,figsize=(8, 6))
ax0.imshow(img_crop,cmap='gray')
ax1.imshow(img_crop,cmap='gray')
ax1 = regionconnect.rect_connect(sub,ax1)
fig.tight_layout()
plt.show()

