from exceptions import PyTorchNotFoundError
from settings import (
    CLUSTER_CENTERS_DOWNLOAD_URL,
    CLUSTER_CENTERS_PATH,
    PRETRAINED_COLORNET_MODEL_DOWNLOAD_ID,
    PRETRAINED_COLORNET_MODEL_PATH,
)

from utils import (
    download_gdrive_to_path,
    extract_l_channel,
    image_to_float32_array,
    resize_image,
    float32_array_to_image,
)

from skimage.color import lab2rgb
from skimage import io
from colornet_core import ColorNet
import numpy as np
import matplotlib.pyplot as plt

try:
    import torch
    from torch.autograd import Variable
    from torchvision.utils import make_grid, save_image
except ModuleNotFoundError as e:
    raise PyTorchNotFoundError(str(e))


def download_pytorch_model_if_necessary(force=False):
    if not PRETRAINED_COLORNET_MODEL_DOWNLOAD_ID.exists() or force:
        download_gdrive_to_path(PRETRAINED_COLORNET_MODEL_DOWNLOAD_ID, PRETRAINED_COLORNET_MODEL_PATH)


if __name__ == "__main__":
    download_pytorch_model_if_necessary()
