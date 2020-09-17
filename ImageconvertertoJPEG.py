from PIL import Image


def convert_to_JPEG(image_path):
    im = Image.open(image_path)
    im.convert("RGB")
    return im