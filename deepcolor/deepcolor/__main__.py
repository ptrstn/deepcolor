import argparse
import pathlib
import sys

from . import __version__, colorize_image, zeruniverse
from . import colornet
from .exceptions import CaffeNotFoundError
from .utils import (
    load_image,
    convert_to_grayscale,
    show_images,
    image_to_float32_array,
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="deepcoor - A tool to colorize black and white pictures"
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    parser.add_argument("image", help="Image path")

    parser.add_argument(
        "-m", "--method", default="colornet", help="Colorization method"
    )

    parser.add_argument("--gpu", action="store_true", help="Colorization method")

    return parser.parse_args()


deepcolor_logo = f"""
   _                     _ 
 _| |___ ___ ___ ___ ___| |___ ___ 
| . | -_| -_| . |  _| . | | . |  _|
|___|___|___|  _|___|___|_|___|_|
            |_|              v{__version__}
"""


def print_logo():
    print(deepcolor_logo)


def get_colorization_method(method_name):
    if method_name == "richzhang":
        try:
            from deepcolor import richzhang
        except CaffeNotFoundError as e:
            print(f"Unable to colorize with method {method_name}")
            sys.exit(e)
        return richzhang.colorize_image
    return {
        "colornet": colornet.colorize_image,
        "zeruniverse": zeruniverse.colorize_image_pytorch,
    }.get(method_name)


def main():
    args = parse_arguments()
    print_logo()

    image_path = pathlib.Path(args.image)
    method_name = args.method
    colorization_method = get_colorization_method(method_name)
    gpu = args.gpu

    original_image = load_image(image_path).convert("RGB")
    grayscale_image = convert_to_grayscale(original_image)
    colorized_image = colorize_image(
        original_image, method=colorization_method, gpu=gpu
    )

    suptitle = f"Colorized {image_path.name} ({method_name})"
    title = "Original image (left), Grayscale image (middle), Colorized image (right)"

    show_images(
        image_to_float32_array(original_image),
        image_to_float32_array(grayscale_image),
        image_to_float32_array(colorized_image),
        padding=True,
        suptitle=suptitle,
        title=title,
    )


if __name__ == "__main__":
    main()
