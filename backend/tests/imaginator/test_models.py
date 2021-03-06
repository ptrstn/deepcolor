import pytest
from imaginator.models import DeepColorResult

pytestmark = pytest.mark.django_db


class TestDeepColorResult:
    def test_str(self):
        result = DeepColorResult(
            pk=69, original="banana.jpg", colored="sausage.jpg", strategy="richzhang"
        )
        assert "69 banana.jpg -> sausage.jpg <richzhang>" == str(result)
