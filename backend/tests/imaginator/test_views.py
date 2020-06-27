import pytest
from deepcolor.checks import CAFFE_IS_INSTALLED
from imaginator.models import DeepColorResult
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


@pytest.mark.skipif(not CAFFE_IS_INSTALLED, reason="Caffe is not installed.")
def test_image_upload(test_image_path):
    file = open(test_image_path, "rb")
    client = APIClient()
    url = "/api/v1/images/"

    assert DeepColorResult.objects.count() == 0

    response = client.post(
        url, {"file": file, "strategy": "richzhang"}, format="multipart"
    )
    assert response.status_code == 201
    assert "id" in response.data
    assert DeepColorResult.objects.count() == 1

    file = open(test_image_path, "rb")
    response = client.post(
        url, {"file": file, "strategy": "colornet"}, format="multipart"
    )
    assert response.status_code == 201
    assert "id" in response.data
    assert DeepColorResult.objects.count() == 2

    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2
    assert "id" in response.data[0]
    assert DeepColorResult.objects.count() == 2

    response = client.get(f"{url}1/")
    assert response.status_code == 200
    response = client.get(f"{url}2/")
    assert response.status_code == 200
    response = client.get(f"{url}3/")
    assert response.status_code == 404

    response = client.delete(f"/api/v1/images/1/")
    assert response.status_code == 204
    assert DeepColorResult.objects.count() == 1
    client.delete(f"/api/v1/images/2/")
    assert DeepColorResult.objects.count() == 0


@pytest.mark.skipif(CAFFE_IS_INSTALLED, reason="Caffe is installed.")
def test_image_upload_when_caffe_not_installed(test_image_path):
    file = open(test_image_path, "rb")
    client = APIClient()
    url = "/api/v1/images/"

    assert DeepColorResult.objects.count() == 0
    response = client.post(
        url, {"file": file, "strategy": "richzhang"}, format="multipart"
    )
    assert response.status_code == 503
    assert response.data is None
    assert DeepColorResult.objects.count() == 0
