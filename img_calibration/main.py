"""
图片校准
"""

import matplotlib.pyplot as plt
from skimage import data
from register_translation import register_translation
import matplotlib.font_manager as fm

# 注意设置中文字体
myfont = fm.FontProperties(fname='/home/pj/datum/fonts/msyh.ttf')


def crop(im, size):
    """
    剪切图片
    :param im:
    :param size:
    :return:
    """
    return im[size[0]:size[2], size[1]: size[3]]


fig = plt.figure(figsize=(8, 4))
ax1 = plt.subplot(1, 4, 1)
ax2 = plt.subplot(1, 4, 2)
ax3 = plt.subplot(1, 4, 3)
ax4 = plt.subplot(1, 4, 4)

image = data.camera()
size1 = (0, 0, 450, 450)
size2 = (50, 10, 500, 460)
im1 = crop(image, size1)
im2 = crop(image, size2)

ax1.imshow(image, cmap='gray')
ax1.set_title('原始图片', fontproperties=myfont)
ax2.imshow(im1, cmap='gray')
ax2.set_title('图片A:' + str(size1), fontproperties=myfont)
ax3.imshow(im2, cmap='gray')
ax3.set_title('图片B:' + str(size2), fontproperties=myfont)
# shifts = register_translation_without_fft(im1, im2)
shifts, cross_correlation = register_translation(im1, im2)
ax4.imshow(cross_correlation.real, cmap='gray')
ax4.set_title('互相关矩阵' + "最高点为：" + str(shifts), fontproperties=myfont)
plt.show()
