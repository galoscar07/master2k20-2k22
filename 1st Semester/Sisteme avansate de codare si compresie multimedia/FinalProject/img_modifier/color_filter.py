import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt


import pywt
import pywt.data


class ColorFilters:
    ascent, aero, ecg, camera, nino
    filters = {"ascent": "Ascent", "vertical": "Vertical", 'diagonal': 'Diagonal'}
    HORIZONTAL, VERTICAL, DIAGONAL = filters.keys()


def color_filter(img, filter_name):
    img_copy = img.copy()

    # Load image
    original = pywt.data.camera()
    # original = img_copy
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

    # Image from plot
    ax.axis('off')
    fig.tight_layout(pad=0)

    # To remove the huge white borders
    ax.margins(0)

    fig.canvas.draw()
    image_from_plot = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    image_from_plot = image_from_plot.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    img = Image.fromarray(image_from_plot)
    img = ImageOps.invert(img)
    return img

    if filter_name == ColorFilters.HORIZONTAL:
        img = Image.fromarray(LH, 'RGB')
    elif filter_name == ColorFilters.VERTICAL:
        img = Image.fromarray(HL, 'RGB')
    elif filter_name == ColorFilters.DIAGONAL:
        img = Image.fromarray(HH, 'RGB')
    else:
        raise ValueError(f"can't find filter {filter_name}")

    return img
