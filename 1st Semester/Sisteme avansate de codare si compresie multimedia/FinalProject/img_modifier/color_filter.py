import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt


import pywt
import pywt.data


class ColorFilters:
    filters = {"ascent": "Ascent", "aero": "Aero", 'camera': 'Camera', 'nino': "Nino"}
    ASCENT, AERO, CAMERA, NINO = filters.keys()


def ascent():
    return do_wavelets(pywt.data.ascent())


def aero():
    return do_wavelets(pywt.data.aero())


def nino():
    return do_wavelets(pywt.data.nino())


def camera():
    return do_wavelets(pywt.data.camera())


def do_wavelets(original):
    # Wavelet transform of image, and plot approximation and details
    titles = ['Approximation', ' Horizontal detail', 'Vertical detail', 'Diagonal detail']
    coeffs2 = pywt.dwt2(original, 'bior1.3')
    LL, (LH, HL, HH) = coeffs2
    fig = plt.figure(figsize=(12, 3))
    for i, a in enumerate([LL, LH, HL, HH]):
        ax = fig.add_subplot(1, 4, i + 1)
        ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
        ax.set_title(titles[i], fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

    fig.canvas.draw()
    image_from_plot = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    image_from_plot = image_from_plot.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    img = Image.fromarray(image_from_plot)
    img = ImageOps.invert(img)
    return img


def color_filter(filter_name):
    if filter_name == ColorFilters.ASCENT:
        img = ascent()
    elif filter_name == ColorFilters.AERO:
        img = aero()
    elif filter_name == ColorFilters.CAMERA:
        img = camera()
    elif filter_name == ColorFilters.NINO:
        img = nino()
    else:
        raise ValueError(f"can't find filter {filter_name}")

    return img
