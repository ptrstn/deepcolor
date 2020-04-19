import os
import pathlib

import deepcolor
from PIL import Image

here = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))


def test_colorize_image():
    image_path = pathlib.Path(here.parent, "data", "de.png")
    test_image = Image.open(image_path)
    colored_image = deepcolor.colorize_image(test_image, debug=True)
    assert colored_image is not None
