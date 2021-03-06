from pathlib import Path

here = Path(__file__).parent.absolute()
PACKAGE_ROOT = here.parent if here.parent.name == "deepcolor" else here
RESOURCES_PATH = Path(PACKAGE_ROOT, "resources")

# ----------
# richzhang
# ----------
RICHZHANG_PRETRAINED_MODEL_DOWNLOAD_URL = "http://eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel"
RICHZHANG_CAFFE_MODEL_DOWNLOAD_URL = "https://raw.githubusercontent.com/richzhang/colorization/caffe/models/colorization_deploy_v2.prototxt"
RICHZHANG_CLUSTER_CENTERS_DOWNLOAD_URL = (
    "https://github.com/richzhang/colorization/raw/caffe/resources/pts_in_hull.npy"
)
RICHZHANG_PRETRAINED_MODEL_PATH = Path(
    RESOURCES_PATH, "colorization_release_v2.caffemodel"
)
RICHZHANG_CAFFE_MODEL_PATH = Path(RESOURCES_PATH, "colorization_deploy_v2.prototxt")
RICHZHANG_CLUSTER_CENTERS_PATH = Path(RESOURCES_PATH, "pts_in_hull.npy")

# ---------
# colornet
# ---------
COLORNET_MODEL_DOWNLOAD_URL = "https://cloud.magical.rocks/f/082fe3bcd8d24412b9dd/?dl=1"

COLORNET_MODEL_PATH = Path(RESOURCES_PATH, "colornet_params_ep_18.pkl")

# ------------
# zeruniverse
# ------------
ZERUNIVERSE_MODEL_DOWNLOAD_URL = (
    "https://github.com/zeruniverse/neural-colorization/releases/download/1.1/G.pth"
)
ZERUNIVERSE_MODEL_PATH = Path(RESOURCES_PATH, "model.pth")
