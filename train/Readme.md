# Training

This Folder is used to train colornet

# How to use

1. Build the container:
```
$ docker build
```
2. Edit `start.sh` to use the correct docker container ID.
```
docker run --gpus 2 -v [path to image data]:/mnt/md0/work0/dl-ss20/T1/data -v [output directory]:/out --ipc=host [CONTAINER ID]
```
3. Create the file `pt1/labelme/train.txt` in the following Format:
```
/mnt/data/vision/torralba/deeplearning/images256/b/bamboo_forest/gsun_b24193d1d14ec76ea05d672da95ed434.jpg 0
/mnt/data/vision/torralba/deeplearning/images256/b/bamboo_forest/gsun_c21c9207ffe05f3876c9d080f689a023.jpg 0
/mnt/data/vision/torralba/deeplearning/images256/b/bamboo_forest/gsun_45b0c8949e9460b930c1ed0296304631.jpg 0
/mnt/data/vision/torralba/deeplearning/images256/b/bamboo_forest/gsun_dd1edc1940fc6ec8db888487c61604c3.jpg 0
/mnt/data/vision/torralba/deeplearning/images256/b/bamboo_forest/gsun_9672a229e27cfc884097fe18023d060a.jpg 0
/mnt/data/vision/torralba/deeplearning/images256/b/bamboo_forest/gsun_27fb23c53d956f4cdc71fbe52cc76ca3.jpg 0
```
Where the first parameter is the absolute path to the images and the second a numeric ID for the label. You can use `pt1/places.py` to automate this

4. Execute `start.sh`
