import os
import pathlib

import pytest
from imaginator.models import DeepColorResult

pytestmark = pytest.mark.django_db

here = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))


class TestDeepColorResult:
    def test_str(self):
        image_path = pathlib.Path(here.parent.parent, "data", "test_data", "face.png")
        result = DeepColorResult(original=image_path, colored=image_path)
        assert "face.png -> face.png" in str(result)
