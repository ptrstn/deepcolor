import argparse
import os
import pathlib
import sys

os.environ["GLOG_minloglevel"] = "2"

from deepcolor import __version__, colorize_image
from deepcolor.exceptions import CaffeNotFoundError
from deepcolor.utils import (
    load_image,
    convert_to_grayscale,
    show_images,
    image_to_float32_array,
)

try:
    from deepcolor import richzhang
except CaffeNotFoundError as e:
    sys.exit(e)

from deepcolor import zeruniverse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="deepcoor - A tool to colorize black and white pictures"
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    parser.add_argument("method", type=int, default=2, help="Zhang = 1, Zeruniverse = 2")    
    parser.add_argument("image", help="Image path")
    parser.add_argument("gpu", type=int, default=-1, help="which GPU to use? [-1 for cpu], only used for Zeruniverse")    

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

    original_image = load_image(image_path).convert("RGB")
    grayscale_image = convert_to_grayscale(original_image)
    if args.method == 1:
        print("Method Zhang")
        colorized_image = colorize_image(original_image, args.gpu, method=richzhang.colorize_image)
    elif args.method == 2:
        print("Method Zeruniverse")
        colorized_image = colorize_image(original_image, args.gpu, method=zeruniverse.colorize_image_pytorch)
    else:
        print("No method under this number, use 1 for Zhang and 2 for Zeruniverse")
    
    suptitle = f"Colorized {image_path.name}"
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
