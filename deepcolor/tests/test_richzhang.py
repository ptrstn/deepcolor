import pytest
from deepcolor.checks import CAFFE_IS_INSTALLED
from deepcolor.utils import load_image


@pytest.mark.skipif(not CAFFE_IS_INSTALLED, reason="Caffe is not installed")
def test_colorize_l_image(farmer_image_path):
    image = load_image(farmer_image_path)

    from deepcolor import richzhang

    colored_image = richzhang.colorize_image(image, gpu=False)

    assert image != colored_image
    assert image.size == colored_image.size


@pytest.mark.skipif(not CAFFE_IS_INSTALLED, reason="Caffe is not installed")
def test_colorize_rgb_image(lincoln_image_path):
    image = load_image(lincoln_image_path)

    from deepcolor import richzhang

    colored_image = richzhang.colorize_image(image, gpu=False)

    assert image != colored_image
    assert image.size == colored_image.size
