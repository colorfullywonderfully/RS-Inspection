from pylab import *

def imhist(img):
    rows, cols = img.shape
    h = np.zeros((256, 1), dtype=np.double)
    for k in range(255):
        h[k] = 0
        for i in range(rows):
            for j in range(cols):
                if img[i,j] == k-1:
                    h[k] = h[k]+1
    return h


def My_MaxEntropy(img):
    rows, cols = img.shape
    gray_p = np.zeros((256, 1), dtype=np.double)
    V_max = np.double(np.max(img))
    V_min = np.double(np.min(img))

    T0 = (V_max + V_min) / 2.0
    h = imhist(img)
    #print(T0 )
    for i in range(255): ###################i from  0
        gray_p[i] = h[i] / np.double(rows * cols)
    H0= 0

    for i in range(1,256):
        if gray_p[i] > 0:
            H0 = H0 - gray_p[i]*math.log(gray_p[i])
    #print(T0)
    cout = 100
    while cout >0:
        Tmax = 0
        T1 =T0
        A1 = 0  # 分割区域G1的点数
        A2 = 0  # 分割区域G2的点数
        B1 = 0  # 分割区域G1的灰度总和
        B2 = 0  # 分割区域G2灰度总和
        gray_Pd=0
        for i in range (rows):
            for j in range(cols):
                if img[i,j]<= T1:
                    A1 = A1 + 1
                    B1 = B1 + img[i, j]
                else:
                    A2 = A2 + 1
                    B2 = B2 + img[i, j]
        M1 = B1 / A1 #分割区域G1的平均灰度
        M2 = B2 / A2 # 分割区域G2的平均灰度
        T2 = (M1 + M2) / 2 # 更新阈值
        TT = np.uint8(floor(T2))
        for i in range(1,TT):  ###########
            gray_Pd = gray_Pd + gray_p[i]

        gray_Pb = 1 - gray_Pd
        Hd = 0
        Hb = 0
        for i in range (255):
            if i <= TT:
                if gray_p[i] > 0:
                    Hd = Hd - gray_p[i] / gray_Pd * math.log(gray_p[i] / gray_Pd)

            else:
                if gray_p[i] > 0:
                    Hb = Hb - gray_p[i] / gray_Pb * math.log(gray_p[i] / gray_Pb)
        H1 = Hd + Hb
        if abs(H0 - H1) < 0.0001:
            Tmax = T2
            break
        else:
            T0 = T2
            H0 = H1
        cout = cout - 1;
    ThreshValue = floor(Tmax)
    return ThreshValue
