from pathlib import Path

here = Path(__file__).parent.absolute()
PACKAGE_ROOT = here.parent
PROJECT_ROOT = PACKAGE_ROOT.parent

CAFFE_MODEL_DOWNLOAD_URL = "http://eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel"

MODELS_PATH = Path(PACKAGE_ROOT, "models")
RESOURCES_PATH = Path(PACKAGE_ROOT, "resources")
DATA_PATH = Path(PACKAGE_ROOT, "data")

PRETRAINED_MODEL_PATH = Path(MODELS_PATH, "colorization_release_v2.caffemodel")
CAFFE_MODEL_PATH = Path(MODELS_PATH, "colorization_deploy_v2.prototxt")
CLUSTER_CENTERS_PATH = Path(RESOURCES_PATH, "pts_in_hull.npy")
TEST_IMAGE_PATH = Path(DATA_PATH, "einstein.jpg")
