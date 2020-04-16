from setuptools import setup, find_packages

setup(
    name="backend",
    version="0.0.1",
    description="A website where you can upload a black and white image to get a color image",
    url="https://github.com/INF-HS-KL-BEGGEL/DL-SS20-T1-image-col",
    author="Sebastian Dauenhauer, Eric Gaida, Peter Stein",
    packages=find_packages(),
    install_requires=["django>=3,<4"],
)
