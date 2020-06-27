import numpy as np
import torch
from PIL import Image
from PIL import ImageEnhance
from skimage.color import lab2rgb, rgb2gray
from torch.autograd import Variable
from torchvision.transforms import transforms

from .colornet_network import ColorNet
from .settings import COLORNET_MODEL_DOWNLOAD_URL, COLORNET_MODEL_PATH
from .utils import float32_array_to_image, download_to_path_with_requests


def download_colornet_model_if_necessary(force=False):
    if not COLORNET_MODEL_PATH.exists() or force:
        download_to_path_with_requests(COLORNET_MODEL_DOWNLOAD_URL, COLORNET_MODEL_PATH)


def setup_model(pretrained_path, gpu=False):
    color_model = ColorNet()

    if gpu:
        assert torch.cuda.is_available(), "CUDA is unavailable. Cannot use GPU mode."
        color_model.load_state_dict(torch.load(pretrained_path, map_location="cuda:0"))
    else:
        color_model.load_state_dict(
            torch.load(pretrained_path, map_location=torch.device("cpu"))
        )

    color_model.eval()
    return color_model


def setup_image(image: Image):
    img_scale = image.copy()
    img_original = image
    img_scale = transforms.Compose(
        [transforms.Resize(256), transforms.RandomCrop(224),]
    )(img_scale)

    img_scale = np.array(img_scale)
    img_original = np.array(img_original)

    img_scale = rgb2gray(img_scale)
    img_scale = torch.from_numpy(img_scale)
    img_original = rgb2gray(img_original)
    img_original = torch.from_numpy(img_original)
    return img_original, img_scale


def process_image(data, gpu=False):
    w = data[0].size()[0]
    h = data[0].size()[1]
    original_img = data[0].reshape((1, w, h)).unsqueeze(1).float()
    scale_img = data[1].reshape((1, 224, 224)).unsqueeze(1).float()
    if gpu:
        original_img, scale_img = original_img.cuda(), scale_img.cuda()

    return original_img, scale_img, w, h


def colorize_image(image: Image, gpu=False, model=COLORNET_MODEL_PATH) -> Image:
    download_colornet_model_if_necessary()
    color_model = setup_model(model, gpu=gpu)
    data = setup_image(image)
    original_img, scale_img, w, h = process_image(data, gpu=gpu)

    original_img, scale_img = Variable(original_img), Variable(scale_img)
    _, output = color_model(original_img, scale_img)
    color_img = torch.cat((original_img, output[:, :, 0:w, 0:h]), 1)
    color_img = color_img.data.cpu().numpy().transpose((0, 2, 3, 1))
    img = color_img[0]
    img[:, :, 0:1] = img[:, :, 0:1] * 100
    img[:, :, 1:3] = img[:, :, 1:3] * 255 - 128

    img = img.astype(np.float32)
    img = lab2rgb(img)
    colorized_image = float32_array_to_image(img)
    converter = ImageEnhance.Color(colorized_image)
    return converter.enhance(1.5)
