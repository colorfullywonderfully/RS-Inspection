import cv2
import math

def rotate(
        img,  # image matrix
        angle  # angle of rotation
):
    height = img.shape[0]
    width = img.shape[1]

    if angle % 180 == 0:
        scale = 1
    elif angle % 90 == 0:
        scale = float(max(height, width)) / min(height, width)
    else:
        scale = math.sqrt(pow(height, 2) + pow(width, 2)) / min(height, width)

        # print 'scale %f\n' %scale

    rotateMat = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    rotateImg = cv2.warpAffine(img, rotateMat, (width, height))
    # cv2.imshow('rotateImg',rotateImg)
    # cv2.waitKey(0)

    return rotateImg  # rotated image