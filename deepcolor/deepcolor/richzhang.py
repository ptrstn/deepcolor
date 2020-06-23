#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is based on the work "Colorful Image Colorization" by Richard Zhang
# See: https://github.com/richzhang/colorization

from warnings import warn

import numpy
from PIL import Image
from matplotlib import pyplot
from scipy.ndimage import interpolation
from skimage import color

from .exceptions import CaffeNotFoundError
from .settings import (
    CAFFE_MODEL_DOWNLOAD_URL,
    CAFFE_MODEL_PATH,
    CLUSTER_CENTERS_DOWNLOAD_URL,
    CLUSTER_CENTERS_PATH,
    PRETRAINED_CAFFE_MODEL_DOWNLOAD_URL,
    PRETRAINED_MODEL_PATH,
)
from .utils import (
    download_to_path,
    extract_l_channel,
    image_to_float32_array,
    resize_image,
    float32_array_to_image,
)

try:
    import caffe
except ModuleNotFoundError as e:
    raise CaffeNotFoundError(str(e))


def download_caffe_model_if_necessary(force=False):
    if not PRETRAINED_MODEL_PATH.exists() or force:
        download_to_path(PRETRAINED_CAFFE_MODEL_DOWNLOAD_URL, PRETRAINED_MODEL_PATH)
    if not CAFFE_MODEL_PATH.exists() or force:
        download_to_path(CAFFE_MODEL_DOWNLOAD_URL, CAFFE_MODEL_PATH)
    if not CLUSTER_CENTERS_PATH.exists() or force:
        download_to_path(CLUSTER_CENTERS_DOWNLOAD_URL, CLUSTER_CENTERS_PATH)


def load_model(models_path, pretrained_path):
    print(f"Loading pretrained model from {pretrained_path}")
    return caffe.Net(str(models_path), str(pretrained_path), caffe.TEST,)


def load_cluster_centers(path=CLUSTER_CENTERS_PATH):
    print(f"Loading cluster centers from {path}")
    return numpy.load(str(path))


def populate_cluster_center(network):
    """
    Populates cluster centers as 1x1 convolution kernel
    """
    pts_in_hull = load_cluster_centers()
    network.params["class8_ab"][0].data[:, :, 0, 0] = pts_in_hull.transpose((1, 0))
    print("Annealed-Mean Parameters populated")


def perform_mean_centering(network, resized_image_l_channel):
    """
    Subtracts 50 for mean-centering
    """
    network.blobs["data_l"].data[0, 0, :, :] = resized_image_l_channel - 50


def predict_a_b_channels(network):
    return network.blobs["class8_ab"].data[0, :, :, :].transpose((1, 2, 0))


def colorize_image(image: Image, gpu=False):
    if gpu:
        warn("GPU Mode currently unsupported. Falling back to CPU Mode.")

    download_caffe_model_if_necessary()

    pyplot.rcParams["figure.figsize"] = (12, 6)
    network = load_model(
        models_path=CAFFE_MODEL_PATH, pretrained_path=PRETRAINED_MODEL_PATH
    )

    populate_cluster_center(network)

    original_image = image_to_float32_array(image.convert("RGB"))

    (original_height, original_width) = original_image.shape[:2]
    (input_height, input_width) = network.blobs["data_l"].data.shape[2:]
    (output_height, output_width) = network.blobs["class8_ab"].data.shape[2:]

    print(f"Original dimensions: ({original_height}, {original_width})")
    print(f"Input dimensions: ({input_height}, {input_width})")
    print(f"Output dimensions: ({output_height}, {output_width})")

    original_l_channel = extract_l_channel(original_image)

    resized_image = resize_image(original_image, input_height, input_width)
    resized_image_l_a_b = color.rgb2lab(resized_image)
    resized_image_l_channel = resized_image_l_a_b[:, :, 0]

    perform_mean_centering(network, resized_image_l_channel)
    network.forward()

    predicted_a_b_channels = predict_a_b_channels(network)

    print(f"Predicted a*b*-Dimensions: {predicted_a_b_channels.shape}")

    predicted_a_b_upscaled = interpolation.zoom(
        predicted_a_b_channels,
        (1.0 * original_height / output_height, 1.0 * original_width / output_width, 1),
    )

    print(f"Upscaled predicted a*b*-Dimensions: {predicted_a_b_upscaled.shape}")

    concatenated_l_a_b_channels = numpy.concatenate(
        (original_l_channel[:, :, numpy.newaxis], predicted_a_b_upscaled), axis=2,
    )

    print(f"Concatenated L*a*b*-Dimensions: {concatenated_l_a_b_channels.shape}")

    output_image = float32_array_to_image(color.lab2rgb(concatenated_l_a_b_channels))

    return output_image
