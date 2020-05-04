#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is based on the work "Colorful Image Colorization" by Richard Zhang
# See: https://github.com/richzhang/colorization

import numpy
from PIL import Image
from deepcolor.caffeutils import load_model, resize_image
from deepcolor.settings import (
    CAFFE_MODEL_DOWNLOAD_URL,
    PRETRAINED_MODEL_PATH,
    CAFFE_MODEL_PATH,
    CLUSTER_CENTERS_PATH,
)
from deepcolor.utils import (
    extract_l_channel,
    download_to_path,
    image_to_array,
    float_array_to_uint8,
)
from matplotlib import pyplot
from scipy.ndimage import interpolation
from skimage import color


def download_caffe_model_if_necessary(
    url=CAFFE_MODEL_DOWNLOAD_URL, path=PRETRAINED_MODEL_PATH, force=False
):
    if not path.exists() or force:
        download_to_path(url, path)
    else:
        print(f"Found caffe model in {path}")


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


def colorize_image(image):
    download_caffe_model_if_necessary()

    pyplot.rcParams["figure.figsize"] = (12, 6)
    network = load_model(
        models_path=CAFFE_MODEL_PATH, pretrained_path=PRETRAINED_MODEL_PATH
    )

    populate_cluster_center(network)

    original_image = image_to_array(image)

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

    output_image = float_array_to_uint8(color.lab2rgb(concatenated_l_a_b_channels))

    return Image.fromarray(output_image)
