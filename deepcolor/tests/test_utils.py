import pathlib

import pytest
from deepcolor.settings import PACKAGE_ROOT
from deepcolor.utils import load_image, convert_to_grayscale, download_to_path
from skimage import color


def test_convert_to_grayscale(einstein_image_path):
    image = load_image(einstein_image_path)
    assert image.mode == "RGB"

    image_lab = color.rgb2lab(image)

    assert image_lab[0][0][0] != 0
    assert image_lab[0][0][1] != 0
    assert image_lab[0][0][2] != 0

    image_gray = convert_to_grayscale(image)
    image_gray_lab = color.rgb2lab(image_gray)

    assert image_gray_lab[0][0][0] == image_lab[0][0][0], "L channel should stay the same"
    assert image_gray_lab[0][0][1] == 0, "a Channel should be zero"
    assert image_gray_lab[0][0][2] == 0, "b Channel should be zero"

    with pytest.raises(ValueError):
        convert_to_grayscale(image.convert(mode="CMYK"))


def test_download_to_path():
    url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png"
    path = pathlib.Path(PACKAGE_ROOT, "data", "google.png")
    assert not path.exists()

    download_to_path(url=url, path=path)

    assert path.exists()
    path.unlink()
    assert not path.exists()
