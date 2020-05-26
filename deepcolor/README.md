# deepcolor

A tool to colorize black and white pictures, based on [Colorful Image Colorization by Richard Zhang](https://github.com/richzhang/colorization) and [neural-colorization by Jeffery (Zeyu) Zhao](https://github.com/zeruniverse/neural-colorization).

## Prerequisites

- [Python 3.6+](https://www.python.org/)
- [caffe](https://caffe.berkeleyvision.org/installation.html)
- [Pytorch](https://pytorch.org/)

## Installation

```bash
git clone https://github.com/INF-HS-KL-BEGGEL/DL-SS20-T1-image-col.git
cd DL-SS20-T1-image-col/
pip install deepcolor/
```

## Usage

```bash
usage: deepcolor [-h] [--version] method image gpu

deepcoor - A tool to colorize black and white pictures

positional arguments:
  method      Method to colorize the image, 1 for the method from Richard Zhang and 2 for the method of Jeffery (Zeyu) Zhao
  image       Image path
  gpu         Which GPU to use? [-1 for cpu], only used for neural-colorization by Jeffery (Zeyu) Zhao (can be left empty for Colorful Image Colorization by Richard Zhang)

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```

### Example

```
For Colorful Image Colorization by Richard Zhang:
deepcolor 1 data/lincoln.jpg

For neural-colorization by Jeffery (Zeyu) Zhao with GPU:
deepcolor 2 data/input.jpg 0

For neural-colorization by Jeffery (Zeyu) Zhao with CPU:
deepcolor 2 data/input.jpg -1
```

Results:

Colorful Image Colorization by Richard Zhang:
```
   _                     _ 
 _| |___ ___ ___ ___ ___| |___ ___ 
| . | -_| -_| . |  _| . | | . |  _|
|___|___|___|  _|___|___|_|___|_|
            |_|              v0.1.0

Converting JPEG image with mode RGB to grayscale
Loading pretrained model from /home/why/so/nosy/deepcolor/resources/colorization_release_v2.caffemodel
Loading cluster centers from /home/why/so/nosy/deepcolor/resources/pts_in_hull.npy
Annealed-Mean Parameters populated
Original dimensions: (640, 444)
Input dimensions: (224, 224)
Output dimensions: (56, 56)
Predicted a*b*-Dimensions: (56, 56, 2)
Upscaled predicted a*b*-Dimensions: (640, 444, 2)
Concatenated L*a*b*-Dimensions: (640, 444, 3)
```
![lincoln](docs/images/result-example.jpg)

neural-colorization by Jeffery (Zeyu) Zhao:
```
   _                     _ 
 _| |___ ___ ___ ___ ___| |___ ___ 
| . | -_| -_| . |  _| . | | . |  _|
|___|___|___|  _|___|___|_|___|_|
            |_|              v0.1.0

Converting None image with mode RGB to grayscale
Method Zeruniverse
qt5ct: using qt5ct plugin

```
![stones](docs/images/result-example2.jpg)

