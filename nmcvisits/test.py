import os

from PIL import Image

def resizeImage(path, newPath):
    im = Image.open(path)
    thumb_width = 200

    def crop_center(pil_img, crop_width, crop_height):
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                            (img_height - crop_height) // 2,
                            (img_width + crop_width) // 2,
                            (img_height + crop_height) // 2))

    def crop_max_square(pil_img):
        return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

    im_thumb = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
    return im_thumb