import os
import pathlib

import pytest

here = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
DATA_PATH = pathlib.Path(here.parent, "data")


@pytest.fixture
def einstein_image_path():
    return pathlib.Path(DATA_PATH, "einstein.jpg")
