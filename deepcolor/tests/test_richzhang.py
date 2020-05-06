import pytest
from deepcolor.checks import CAFFE_IS_INSTALLED


@pytest.mark.skipif(not CAFFE_IS_INSTALLED, reason="Caffe is not installed")
def test_colorize_image():
    assert True
