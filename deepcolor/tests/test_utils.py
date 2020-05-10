import pathlib

import numpy
import pytest
from deepcolor.settings import PACKAGE_ROOT
from deepcolor.utils import (
    load_image,
    convert_to_grayscale,
    download_to_path,
    resize_image,
    image_to_float32_array,
    extract_l_channel,
    intersperse,
    float32_array_to_image,
)
from skimage import color


def test_convert_to_grayscale_rgb(lincoln_image_path):
    image = load_image(lincoln_image_path)
    assert image.mode == "RGB"

    image_lab = color.rgb2lab(image)

    assert image_lab[0][0][0] != 0
    assert image_lab[0][0][1] != 0
    assert image_lab[0][0][2] != 0

    image_gray = convert_to_grayscale(image)
    image_gray_lab = color.rgb2lab(image_gray)

    assert round(image_gray_lab[0][0][0], 2) == round(
        image_lab[0][0][0], 2
    ), "L channel should stay the same"
    assert round(image_gray_lab[0][0][1], 2) == 0, "a Channel should be zero"
    assert round(image_gray_lab[0][0][2], 2) == 0, "b Channel should be zero"

    with pytest.raises(ValueError):
        convert_to_grayscale(image.convert(mode="CMYK"))


def test_convert_to_grayscale_l(farmer_image_path):
    image = load_image(farmer_image_path)
    assert image.mode == "L"

    image_lab = color.rgb2lab(image.convert("RGB"))

    assert image_lab[69][42][0] != 0
    assert round(image_lab[69][42][1], 2) == 0, "a Channel should be zero"
    assert round(image_lab[69][42][2], 2) == 0, "b Channel should be zero"

    image_gray = convert_to_grayscale(image)
    image_gray_lab = color.rgb2lab(image_gray)

    assert round(image_gray_lab[69][42][0], 2) == round(
        image_lab[69][42][0], 2
    ), "L channel should stay the same"
    assert round(image_gray_lab[69][42][1], 2) == 0, "a Channel should stay zero"
    assert round(image_gray_lab[69][42][2], 2) == 0, "b Channel should stay zero"

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


def test_resize_image(lincoln_image_path):
    image = load_image(lincoln_image_path)
    image_array = image_to_float32_array(image)
    assert image.size == (444, 640)
    resized_array = resize_image(image_array, 10, 10)
    resized_image = float32_array_to_image(resized_array)
    assert resized_image.size == (10, 10)


def test_extract_l_channel(lincoln_image_path):
    image = load_image(lincoln_image_path)
    assert numpy.array(image).ndim == 3

    l_channel = extract_l_channel(image)
    assert l_channel.ndim == 2, "Should be 2-dimensional"


def test_intersperse():
    assert intersperse("A", "B", "C", delimiter="X") == ["A", "X", "B", "X", "C"]
    assert intersperse("A", delimiter="X") == ["A"]
    assert intersperse(delimiter="X") == []
    assert intersperse("A", "B", "C", delimiter=None) == ["A", "B", "C"]
