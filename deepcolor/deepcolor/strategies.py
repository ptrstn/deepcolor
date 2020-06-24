from . import colornet, zeruniverse
from .exceptions import CaffeNotFoundError


def get_colorization_strategy(strategy_name):
    if strategy_name == "richzhang":
        try:
            from deepcolor import richzhang
        except CaffeNotFoundError as e:
            print(f"Error: Unable to colorize with strategy {strategy_name}")
            raise e
        return richzhang.colorize_image
    return {
        "colornet": colornet.colorize_image,
        "zeruniverse": zeruniverse.colorize_image_pytorch,
    }.get(strategy_name)


def create_strategy_entry(name, short, description, url=None):
    return {
        "strategy_name": name,
        "short": short,
        "description": description,
        "url": url,
    }


def available_strategies():
    return [
        create_strategy_entry(
            "richzhang",
            "Richard Zhang",
            '"Colorful Image Colorization" by Richard Zhang',
            "https://richzhang.github.io/",
        ),
        create_strategy_entry(
            "colornet",
            "Colornet",
            'Self trained network based on "Let there be Color!" by Satoshi Iizuka',
            "http://iizuka.cs.tsukuba.ac.jp/projects/colorization/en/",
        ),
        create_strategy_entry(
            "zeruniverse",
            "neural-colorization",
            '"neural-colorization" by Jeffery (Zeyu) Zhao',
            "https://github.com/zeruniverse/neural-colorization",
        ),
    ]


def available_strategy_names():
    return [strategy["strategy_name"] for strategy in available_strategies()]
