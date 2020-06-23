#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is based on the work "neural-colorization "neural-colorization" by Jeffery (Zeyu) Zhao
# See: https://github.com/zeruniverse/neural-colorization

import cv2
import numpy as np
import torch
from PIL import Image
from scipy.ndimage import zoom
from skimage.color import rgb2yuv, yuv2rgb
from torch.autograd import Variable

from .zeruniverse_network import generate_network
from .settings import (
    ZERUNIVERSE_MODEL_DOWNLOAD_URL,
    ZERUNIVERSE_MODEL_PATH,
)
from .utils import download_to_path


def generate_image(network, input, gpu=False):
    # convert input image to RGB
    image_rgb = input
    image_yuv = rgb2yuv(image_rgb)
    height, width, _ = image_yuv.shape
    infimg = np.expand_dims(np.expand_dims(image_yuv[..., 0], axis=0), axis=0)
    image_variable = Variable(torch.Tensor(infimg - 0.5))
    if gpu:
        image_variable = image_variable.cuda(gpu)
    res = network(image_variable)
    uv = res.cpu().detach().numpy()
    uv[:, 0, :, :] *= 0.436
    uv[:, 1, :, :] *= 0.615
    (_, _, H1, W1) = uv.shape
    uv = zoom(uv, (1, 1, height / H1, width / W1))
    yuv = np.concatenate([infimg, uv], axis=1)[0]
    rgb = yuv2rgb(yuv.transpose(1, 2, 0))
    # create image
    cv2.imwrite("data/output.jpg", (rgb.clip(min=0, max=1) * 256)[:, :, [2, 1, 0]])
    # convert image to RGB
    output_image = Image.open("data/output.jpg").convert("RGB")
    return output_image


def colorize_image_pytorch(image: Image, gpu=False):
    download_pytorch_model_if_necessary()

    network = generate_network()

    if gpu:
        assert torch.cuda.is_available(), "CUDA is unavailable. Cannot use GPU mode."
        network = network.cuda(gpu)
        network.load_state_dict(
            torch.load(ZERUNIVERSE_MODEL_PATH, map_location="cuda:0")
        )
    else:
        network.load_state_dict(
            torch.load(ZERUNIVERSE_MODEL_PATH, map_location=torch.device("cpu"))
        )

    return generate_image(network, image, gpu)


def download_pytorch_model_if_necessary(force=False):
    if not ZERUNIVERSE_MODEL_PATH.exists() or force:
        download_to_path(ZERUNIVERSE_MODEL_DOWNLOAD_URL, ZERUNIVERSE_MODEL_PATH)
