import caffe


def load_model(models_path, pretrained_path):
    print(f"Loading pretrained model from {pretrained_path}")
    return caffe.Net(str(models_path), str(pretrained_path), caffe.TEST,)


def resize_image(image, height, width):
    return caffe.io.resize_image(image, (height, width))
