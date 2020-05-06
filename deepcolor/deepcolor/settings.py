from pathlib import Path

here = Path(__file__).parent.absolute()
PACKAGE_ROOT = here.parent if here.parent.name == "deepcolor" else here

PRETRAINED_CAFFE_MODEL_DOWNLOAD_URL = "http://eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel"
CAFFE_MODEL_DOWNLOAD_URL = "https://raw.githubusercontent.com/richzhang/colorization/master/models/colorization_deploy_v2.prototxt"
CLUSTER_CENTERS_DOWNLOAD_URL = (
    "https://github.com/richzhang/colorization/raw/master/resources/pts_in_hull.npy"
)

RESOURCES_PATH = Path(PACKAGE_ROOT, "resources")
PRETRAINED_MODEL_PATH = Path(RESOURCES_PATH, "colorization_release_v2.caffemodel")
CAFFE_MODEL_PATH = Path(RESOURCES_PATH, "colorization_deploy_v2.prototxt")
CLUSTER_CENTERS_PATH = Path(RESOURCES_PATH, "pts_in_hull.npy")
