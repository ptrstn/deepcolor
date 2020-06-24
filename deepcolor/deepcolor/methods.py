from . import colornet, zeruniverse
from .exceptions import CaffeNotFoundError


def get_colorization_method(method_name):
    if method_name == "richzhang":
        try:
            from deepcolor import richzhang
        except CaffeNotFoundError as e:
            print(f"Error: Unable to colorize with method {method_name}")
            raise e
        return richzhang.colorize_image
    return {
        "colornet": colornet.colorize_image,
        "zeruniverse": zeruniverse.colorize_image_pytorch,
    }.get(method_name)


def create_method_entry(name, short, description, url=None):
    return {
        "method_name": name,
        "short": short,
        "description": description,
        "url": url,
    }


def available_methods():
    return [
        create_method_entry(
            "richzhang",
            "Richard Zhang",
            '"Colorful Image Colorization" by Richard Zhang',
            "https://richzhang.github.io/",
        ),
        create_method_entry(
            "colornet",
            "Colornet",
            'Self trained network based on "Let there be Color!" by Satoshi Iizuka',
            "http://iizuka.cs.tsukuba.ac.jp/projects/colorization/en/",
        ),
        create_method_entry(
            "zeruniverse",
            "neural-colorization",
            '"neural-colorization" by Jeffery (Zeyu) Zhao',
            "https://github.com/zeruniverse/neural-colorization",
        ),
    ]


def available_method_names():
    return [method["method_name"] for method in available_methods()]
