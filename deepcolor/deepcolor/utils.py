import numpy
import skimage
import wget
from PIL import Image
from matplotlib import pyplot
from skimage import color


def download_to_path(url, path):
    print(f"Downloading {url} \nto {path}\n")
    path.parent.mkdir(exist_ok=True)
    wget.download(url, str(path), bar=wget.bar_adaptive)
    print()


def load_image(path):
    return Image.open(path)


def image_to_array(image: Image) -> numpy.ndarray:
    image_as_array = numpy.array(image)
    image_as_float32 = skimage.img_as_float32(image_as_array)
    return image_as_float32


def convert_to_grayscale(rgb_image):
    print("Converting RGB image to grayscale")
    lab_image = color.rgb2lab(rgb_image)
    lab_image = lab_image.copy()
    lab_image[:, :, 1:] = 0
    return color.lab2rgb(lab_image)


def extract_l_channel(rgb_image):
    return color.rgb2lab(rgb_image)[:, :, 0]


def float_array_to_uint8(image):
    return (255 * numpy.clip(image, 0, 1)).astype("uint8")


def intersperse_images(*images, delimiter):
    tmp = []
    for image in images:
        tmp.append(image)
        tmp.append(delimiter)
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
            print("Catastrophic failure")
            numpy.exit(0)
        images = intersperse_images(*images, delimiter=image_padding)

    pyplot.imshow(numpy.hstack(images))
    if suptitle:
        pyplot.suptitle(suptitle)
    if title:
        pyplot.title(title)
    pyplot.axis("off")
    pyplot.show()