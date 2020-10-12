from skimage import data,segmentation,measure,morphology,color
import matplotlib.patches as mpatches

def rect_connect(img_fill,ax):
    label_image =measure.label(img_fill)  #连通区域标记

    for region in measure.regionprops(label_image):  # 循环得到每一个连通区域属性集

        # 忽略小区域
        if region.area < 10:
            continue

        # 绘制外包矩形
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)
    return ax

