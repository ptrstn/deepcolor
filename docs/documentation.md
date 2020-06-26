# Image Colorization

*Deep Learning, Hochschule Kaiserslautern*
*30. June 2020*

This project is about the colorization of black and white images. 
The goal of the project was to create a website where you can upload a black and white image and get the colored image back. 
The "Colorful Image Colorization" project by Richard Zhang served as a reference, providing the website, the neural network architecture and a descriptive paper. In addition to the network just described, an own network "colornet" was trained. 
This project can be extended by further colorization strategies, because an interface was introduced that is used dynamically by the website.

## Concept

Describe how the colorization works

- Colorspaces
    - RGB
    - L*a*b*

## Architecture

This project was divided into three isolated units. 
The centrepiece of the project is the Python package ```deepcolor```, which is responsible for the application of the deep learning algorithms. 
This package also provides a command line client that allows the colorization of images via the console according to the desired network.

The ```deepcolor``` package is used by the ```backend```, which provides a REST interface that is used by ```frontend```.

(image of architecture)

### ```deepcolor```

Describe how it works

### ```backend```

Describe how it works

- Django
- Django REST framework
- Endpoints

### ```frontend```

Describe how it works

- React
