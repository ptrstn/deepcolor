import deepcolor
from PIL import Image


def test_colorize_image():
    test_image = Image.open("data/de.png")
    colored_image = deepcolor.colorize_image(test_image, debug=True)
    assert colored_image is not None
