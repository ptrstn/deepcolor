from pathlib import Path

import numpy
import skimage
import wget
from PIL import Image
from matplotlib import pyplot
from skimage import color
from skimage import transform

import requests


def download_to_path(url, path):
    print(f"Downloading {url} \nto {path}\n")
    path.parent.mkdir(parents=True, exist_ok=True)
    wget.download(url, str(path), bar=wget.bar_adaptive)
    print()


def download_to_path_with_requests(url, path):
    print(f"Downloading {url} \nto {path}\n")
    response = requests.get(url, stream=True)
    save_response_content(response, path)
    print()


def save_response_content(response, destination):
    chunk_size = 32768

    Path(destination.parent).mkdir(parents=True, exist_ok=True)
    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def load_image(path):
    return Image.open(path)


def image_to_float32_array(image: Image) -> numpy.ndarray:
    image_as_array = numpy.array(image)
    return skimage.img_as_float32(image_as_array)


def float32_array_to_image(array: numpy.ndarray) -> Image:
    uint8_array = float_array_to_uint8(array)
    return Image.fromarray(uint8_array)


def convert_to_grayscale(image):
    print(f"Converting {image.format} image with mode {image.mode} to grayscale")
    if image.mode == "RGB":
        rgb_image = image
    elif image.mode == "L":
        rgb_image = image.convert("RGB")
    else:
        raise ValueError(f"Unsupported mode {image.mode} for {image.format} image.")

    lab_image = color.rgb2lab(rgb_image)
    lab_image = lab_image.copy()
    lab_image[:, :, 1:] = 0
    return color.lab2rgb(lab_image)


def extract_l_channel(rgb_image):
    return color.rgb2lab(rgb_image)[:, :, 0]


def float_array_to_uint8(array: numpy.ndarray) -> numpy.ndarray:
    return (255 * numpy.clip(array, 0, 1)).astype("uint8")


def resize_image(image, height, width):
    return transform.resize(image, (height, width))


def intersperse(*items, delimiter):
    tmp = []
    for item in items[:-1]:
        tmp.append(item)
        if delimiter is not None:
            tmp.append(delimiter)
    if items:
        tmp.append(items[-1])
    return tmp


def show_image_rgb_channel(image, title=None):
    shape = image.shape
    for channel, channel_name in enumerate(["red", "green", "blue"]):
        channel_image = numpy.zeros(shape)
        channel_image[:, :, channel] = image[:, :, 0]

    red_channel = image.copy()
    red_channel[:, :, 1] = 0
    red_channel[:, :, 2] = 0
    green_channel = image.copy()
    green_channel[:, :, 0] = 0
    green_channel[:, :, 2] = 0
    blue_channel = image.copy()
    blue_channel[:, :, 0] = 0
    blue_channel[:, :, 1] = 0

    show_images(
        image,
        red_channel,
        green_channel,
        blue_channel,
        title=f"{title} {image.shape}",
        padding=True,
    )


def show_images(*images, title=None, suptitle=None, padding=False):
    if padding:
        first_image = images[0]
        (height, width) = first_image.shape[:2]
        if first_image.ndim == 3:
            image_padding = numpy.ones((height, int(width / 10), 3))
        elif first_image.ndim == 2:
            image_padding = numpy.ones((height, int(width / 10)))
        else:
            raise ValueError(f"Unsupported image dimensions: {first_image.ndim}")

        images = intersperse(*images, delimiter=image_padding)

    pyplot.imshow(numpy.hstack(images))
    if suptitle:
        pyplot.suptitle(suptitle)
    if title:
        pyplot.title(title)
    pyplot.axis("off")
    pyplot.show()
