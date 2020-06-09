import deepcolor
import pytest
from PIL import Image
from deepcolor.checks import CAFFE_IS_INSTALLED


def test_colorize_image_none(farmer_image_path):
    test_image = Image.open(farmer_image_path)
    colored_image = deepcolor.colorize_image(test_image, -1, method=None)
    assert colored_image is not None
    assert test_image == colored_image, "Should not be colored since method is None"


@pytest.mark.skipif(not CAFFE_IS_INSTALLED, reason="Caffe is not installed")
def test_colorize_image_richzhang(farmer_image_path):
    test_image = Image.open(farmer_image_path)
    from deepcolor import richzhang

    colored_image = deepcolor.colorize_image(
        test_image, -1, method=richzhang.colorize_image
    )
    assert colored_image is not None
    assert test_image != colored_image
