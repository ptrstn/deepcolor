from PIL import Image


def colorize_image(image: Image, method, args=None) -> Image:
    if not method:
        print(
            "Warning: No colorization method was specified. Returning original image."
        )
        return image
    if args is None:
        return method(image)
    else:
        return method(image, args)
