import codecs
import os

from setuptools import setup, find_packages


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


long_description = read("README.md")

setup(
    name="backend",
    version="0.2.0",
    description="A website where you can upload a black and white image to get a color image",
    long_description=long_description,
    url="https://github.com/INF-HS-KL-BEGGEL/DL-SS20-T1-image-col",
    packages=find_packages(),
    install_requires=["django>=3,<4", "djangorestframework", "Pillow", "deepcolor"],
    python_requires=">=3.6",
    license='GPLv3',
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Education',
    ],
)
