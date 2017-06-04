import numpy as np


def register_translation(src_image, target_image):
    """
    Efficient subpixel image translation registration by cross-correlation.[2007]
    :param src_image:
    :param target_image:
    :return:
    """
    src_image = np.array(src_image, dtype=np.complex128, copy=False)
    target_image = np.array(target_image, dtype=np.complex128, copy=False)
    # 这里实际上计算的是
    src_freq = np.fft.fftn(src_image)
    target_freq = np.fft.fftn(target_image)

    shape = src_freq.shape
    image_product = src_freq * target_freq.conj()
    cross_correlation = np.fft.ifftn(image_product)

    # Locate maximum
    # 定位最大值（得到最大值所在的坐标）
    maxima = np.unravel_index(np.argmax(np.abs(cross_correlation)),
                              cross_correlation.shape)
    shifts = np.array(maxima, dtype=np.float64)

    # 是的偏移量小于图片长或宽的一半
    midpoints = np.array([np.fix(axis_size / 2) for axis_size in shape])
    shifts[shifts > midpoints] -= np.array(shape)[shifts > midpoints]
    return shifts, cross_correlation
