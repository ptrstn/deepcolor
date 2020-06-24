from setuptools import setup, find_packages

setup(
    name="backend",
    version="0.2.0",
    description="A website where you can upload a black and white image to get a color image",
    url="https://github.com/INF-HS-KL-BEGGEL/DL-SS20-T1-image-col",
    packages=find_packages(),
    install_requires=["django>=3,<4", "djangorestframework", "Pillow", "deepcolor"],
)
