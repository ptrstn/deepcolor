import os
import pathlib

import pytest

here = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
TEST_IMAGE_PATH = pathlib.Path(here.parent, "data", "test_data", "einstein.jpg")


@pytest.fixture
def test_image_path():
    return TEST_IMAGE_PATH
