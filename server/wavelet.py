import numpy as np
import pywt
import cv2

import numpy as np
import pywt
import cv2


def w2d(img, mode='haar', level=1):
    imarray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    imarray = np.float32(imarray)
    imarray /= 255

    coeff = pywt.wavedec2(imarray, mode, level=level)

    coeff_H = list(coeff)
    coeff_H[0] *= 0

    imarray_H = pywt.waverec2(coeff_H, mode)
    imarray_H *= 255
    imarray_H = np.uint8(imarray_H)

    return imarray_H
