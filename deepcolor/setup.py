import codecs
import os

from setuptools import setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


long_description = read("README.md")

setup(
    name="deepcolor",
    version=get_version("deepcolor/__init__.py"),
    description="Colorize a black and white image",
    long_description=long_description,
    packages=["deepcolor"],
    install_requires=[
        "Pillow",
        "protobuf",
        "numpy",
        "matplotlib",
        "scikit-image",
        "wget",
        "scipy",
        "opencv-python",
        "requests",
        "torch",
        "torchvision",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["deepcolor=deepcolor.__main__:main"]},
)
