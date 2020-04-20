import deepcolor
from django.http import Http404
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DeepColorResult


def create_deep_image_result(data):
    original_image = data["file"]
    colored_image = deepcolor.colorize_image(original_image)
    return DeepColorResult.objects.create(
        original=original_image, colored=colored_image
    )


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
        result = create_deep_image_result(serializer.validated_data)
        data = self.ResultSerializer(result)
        return Response(data.data, status=status.HTTP_201_CREATED)


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
