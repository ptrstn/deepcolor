import argparse
import pathlib

from deepcolor.methods import (
    get_colorization_method,
    available_method_names,
    available_methods,
)

from . import __version__, colorize_image
from .utils import (
    load_image,
    convert_to_grayscale,
    show_images,
    image_to_float32_array,
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="deepcolor - A tool to colorize black and white pictures",
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=100
        ),
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    parser.add_argument("image", help="Image path")

    parser.add_argument(
        "--method",
        nargs="+",
        help=f"Colorization methods to use. Available methods: {', '.join(available_method_names())}",
        default=["colornet"],
    )

    parser.add_argument(
        "--gpu", action="store_true", help="Run in CUDA mode rather than CPU"
    )

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


def print_selected_method(method_name):
    print(f"Colorizing image using {method_name} strategy.")
    method_entry = [
        method for method in available_methods() if method["method_name"] == method_name
    ][0]
    for key, value in method_entry.items():
        print(f"{key + ':':15}{value}")
    print()


def main():
    args = parse_arguments()
    print_logo()

    image_path = pathlib.Path(args.image)
    gpu = args.gpu

    colored_images = {}

    original_image = load_image(image_path).convert("RGB")
    grayscale_image = convert_to_grayscale(original_image)

    for method_name in args.method:
        print_selected_method(method_name)
        colorization_method = get_colorization_method(method_name)

        colorized_image = colorize_image(
            original_image, method=colorization_method, gpu=gpu
        )

        colored_images[method_name] = colorized_image

        colorized_filename = (
            f"colorized_{image_path.stem}_{method_name}{image_path.suffix}"
        )
        print(f"Saving colorized image as {colorized_filename} \n")
        colorized_image.save(colorized_filename)

    suptitle = f"Colorized {image_path.name} using {', '.join(colored_images.keys())}"
    colored_image_titles = [
        f"Colorized image ({method})" for method in colored_images.keys()
    ]
    title = f"Original image (left), Grayscale image (second), {', '.join(colored_image_titles)}"

    images = [original_image, grayscale_image, *list(colored_images.values())]
    float32_images = [image_to_float32_array(image) for image in images]

    show_images(
        *float32_images, padding=True, suptitle=suptitle, title=title,
    )


if __name__ == "__main__":
    main()
