#!/bin/bash
docker run --gpus 2 -v /mnt/md0/work0/dl-ss20/T1/data:/mnt/md0/work0/dl-ss20/T1/data -v /mnt/md0/work0/dl-ss20/T1/model:/out --ipc=host e87d99aacb5b
