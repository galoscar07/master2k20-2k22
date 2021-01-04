from PIL import Image
import img_modifier.color_filter as cf


def get_img(path):
    """Return PIL.Image object"""
    if path == "":
        raise ValueError("path is empty of has bad format")

    try:
        return Image.open(path)
    except Exception:
        raise ValueError(f"can't open the file {path}")


def resize(img, width, height):
    """Resize image"""
    return img.resize((width, height))


def color_filter(img, filter_name):
    """Filter image"""
    return cf.color_filter(img, filter_name)
