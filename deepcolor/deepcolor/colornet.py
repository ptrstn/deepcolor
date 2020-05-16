from torchvision.transforms import transforms

from .exceptions import PyTorchNotFoundError
from .settings import (
    CLUSTER_CENTERS_DOWNLOAD_URL,
    CLUSTER_CENTERS_PATH,
    PRETRAINED_COLORNET_MODEL_DOWNLOAD_ID,
    PRETRAINED_COLORNET_MODEL_PATH,
)

from .utils import (
    download_gdrive_to_path,
    extract_l_channel,
    image_to_float32_array,
    resize_image,
    float32_array_to_image,
)

from skimage.color import lab2rgb, rgb2gray
from skimage import io
from .colornet_core import ColorNet
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

try:
    import torch
    from torch.autograd import Variable
    from torchvision.utils import make_grid, save_image
except ModuleNotFoundError as e:
    raise PyTorchNotFoundError(str(e))


scale_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.RandomCrop(224),
])


def download_pytorch_model_if_necessary(force=False):
    if not PRETRAINED_COLORNET_MODEL_PATH.exists() or force:
        download_gdrive_to_path(PRETRAINED_COLORNET_MODEL_DOWNLOAD_ID, PRETRAINED_COLORNET_MODEL_PATH)


def setup_model(pretrained_path):
    color_model = ColorNet()
    color_model.load_state_dict(torch.load(pretrained_path))
    if torch.cuda.is_available():
        color_model.cuda()
    color_model.eval()
    return color_model


def setup_image(image: Image):
    img_scale = image.copy()
    img_original = image
    img_scale = scale_transform(img_scale)

    img_scale = np.array(img_scale)
    img_original = np.array(img_original)

    img_scale = rgb2gray(img_scale)
    img_scale = torch.from_numpy(img_scale)
    img_original = rgb2gray(img_original)
    img_original = torch.from_numpy(img_original)
    return img_original, img_scale


def process_image(data):
    w = data[0].size()[0]
    h = data[0].size()[1]
    original_img = data[0].reshape((1, w, h)).unsqueeze(1).float()
    gray_name = './0.jpg'
    pic = original_img.squeeze().numpy()
    pic = pic.astype(np.float64)
    plt.imsave(gray_name, data[0], cmap='gray')
    scale_img = data[1].reshape((1, 224, 224)).unsqueeze(1).float()

    return original_img.cuda(), scale_img.cuda(), w, h


def colorize_image(image: Image):
    download_pytorch_model_if_necessary()
    color_model = setup_model(PRETRAINED_COLORNET_MODEL_PATH)
    data = setup_image(image)
    original_img, scale_img, w, h = process_image(data)

    original_img, scale_img = Variable(original_img), Variable(scale_img)
    print(original_img.shape)
    _, output = color_model(original_img, scale_img)
    color_img = torch.cat((original_img, output[:, :, 0:w, 0:h]), 1)
    color_img = color_img.data.cpu().numpy().transpose((0, 2, 3, 1))
    for img in color_img:
        img[:, :, 0:1] = img[:, :, 0:1] * 100
        img[:, :, 1:3] = img[:, :, 1:3] * 255 - 128
        img = img.astype(np.float64)
        img = lab2rgb(img)
        color_name = './0_c.jpg'
        plt.imsave(color_name, img)
