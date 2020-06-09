from io import BytesIO

import deepcolor
from PIL import Image
from deepcolor.exceptions import CaffeNotFoundError
from django.core.files import File
from django.http import Http404
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DeepColorResult


def create_deep_image_result(data):
    # https://stackoverflow.com/a/49065291/9907540
    file = data["file"]

    image_file_name = file.name
    original_image = Image.open(file)

    from deepcolor import richzhang

    colored_image = deepcolor.colorize_image(
        original_image, -1, method=richzhang.colorize_image
    )

    instance = DeepColorResult(original=file)
    colorized_bytes = BytesIO()
    colored_image.save(colorized_bytes, "JPEG")
    instance.colored.save(
        f"colorized_{image_file_name}", File(colorized_bytes), save=False
    )

    instance.save()

    return instance


class DeepColorResultList(APIView):
    """
    List all images
    """

    class InputSerializer(serializers.Serializer):
        file = serializers.FileField()

    class ResultSerializer(serializers.ModelSerializer):
        class Meta:
            model = DeepColorResult
            fields = ("id", "original", "colored")

    def get(self, request, format=None):
        images = DeepColorResult.objects.all()
        serializer = self.ResultSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            result = create_deep_image_result(serializer.validated_data)
            data = self.ResultSerializer(result)
            return Response(data.data, status=status.HTTP_201_CREATED)
        except CaffeNotFoundError:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)


class DeepColorResultDetail(APIView):
    """
    List all images
    """

    class DeepColorResultSerializer(serializers.ModelSerializer):
        class Meta:
            model = DeepColorResult
            fields = ("id", "original", "colored")

    def get_object(self, pk):
        try:
            return DeepColorResult.objects.get(pk=pk)
        except DeepColorResult.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = self.DeepColorResultSerializer(result)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
