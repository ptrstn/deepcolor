from PIL import Image


def colorize_image(image: Image, strategy, gpu=False) -> Image:
    if not strategy:
        print(
            "Warning: No colorization strategy was specified. Returning original image."
        )
        return image
    return strategy(image, gpu)
