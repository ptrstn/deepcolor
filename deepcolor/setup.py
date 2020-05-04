from setuptools import setup

setup(
    name="deepcolor",
    version="0.0.1",
    description="Colorize a black and white image",
    packages=["deepcolor"],
    install_requires=[
        "Pillow",
        "protobuf",
        "numpy",
        "matplotlib",
        "scikit-image",
        "scipy",
        "wget",
    ],
    entry_points={"console_scripts": ["deepcolor=deepcolor.__main__:main"]},
)
