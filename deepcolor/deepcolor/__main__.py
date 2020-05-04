import os

os.environ["GLOG_minloglevel"] = "2"

import argparse
import pathlib

from deepcolor import __version__
from deepcolor.richzhang import colorize_image
from deepcolor.utils import (
    load_image,
    convert_to_grayscale,
    show_images,
    image_to_array,
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="deepcoor - A tool to colorize black and white pictures"
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    parser.add_argument("image", help="Image path")

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


def main():
    args = parse_arguments()

    print_logo()

    image_path = pathlib.Path(args.image)

    original_image = load_image(image_path)
    grayscale_image = convert_to_grayscale(original_image)
    colorized_image = colorize_image(original_image)

    suptitle = f"Colorized {image_path.name}"
    title = "Original image (left), Grayscale image (middle), Colorized image (right)"

    show_images(
        image_to_array(original_image),
        image_to_array(grayscale_image),
        image_to_array(colorized_image),
        padding=True,
        suptitle=suptitle,
        title=title,
    )


if __name__ == "__main__":
    main()
