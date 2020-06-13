from PIL import Image

def colorize_image(image: Image, gpu, method) -> Image:
    if not method:
        print(
            "Warning: No colorization method was specified. Returning original image."
        )
        return image
    return method(image, gpu)
