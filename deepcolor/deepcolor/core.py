from PIL import Image
from deepcolor import richzhang


def colorize_image(image: Image, debug=False) -> Image:
    if debug:
        print("Colorizing image...")
    return richzhang.colorize_image(image)
