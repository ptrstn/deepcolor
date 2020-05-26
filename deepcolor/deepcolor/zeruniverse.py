#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is based on the work "neural-colorization "neural-colorization" by Jeffery (Zeyu) Zhao
# See: https://github.com/zeruniverse/neural-colorization

import torch
from torch.autograd import Variable
from scipy.ndimage import zoom
import os
import cv2
from PIL import Image
import argparse
import numpy as np
from skimage.color import rgb2yuv,yuv2rgb

from .settings import (
    PRETRAINED_PYTORCH_MODEL_DOWNLOAD_URL,
    PRETRAINED_PYTORCH_MODEL_PATH,
    PYTORCH_MODEL_DOWNLOAD_URL,
    PYTORCH_MODEL_PATH
)
from .utils import (
    download_to_path,
    extract_l_channel,
    image_to_float32_array,
    resize_image,
    float32_array_to_image,
)
from .model import generator


def generate_image(G, input, gpu):
    original_image = input
    #convert input image to RGB
    image_rgb = input #Image.open(input).convert('RGB')
    #convert rgb image to yuv color model
    img_yuv = rgb2yuv(image_rgb)
    #get width and height of yuv image
    H,W,_ = img_yuv.shape
    #do stuff
    infimg = np.expand_dims(np.expand_dims(img_yuv[...,0], axis=0), axis=0)
    img_variable = Variable(torch.Tensor(infimg-0.5))
    if gpu>=0:
        img_variable=img_variable.cuda(gpu)
    res = G(img_variable)
    uv=res.cpu().detach().numpy()
    uv[:,0,:,:] *= 0.436
    uv[:,1,:,:] *= 0.615
    (_,_,H1,W1) = uv.shape
    uv = zoom(uv,(1,1,H/H1,W/W1))
    yuv = np.concatenate([infimg,uv],axis=1)[0]
    rgb = yuv2rgb(yuv.transpose(1,2,0))
    #create image
    cv2.imwrite("data/output.jpg",(rgb.clip(min=0,max=1)*256)[:,:,[2,1,0]])
    #convert image to RGB
    output_image = Image.open("data/output.jpg").convert("RGB")
    return output_image

def colorize_image_pytorch(image: Image, gpu):
    download_pytorch_model_if_necessary()

    G = generator()
    #check which GPU to use or only use CPU
    if gpu>=0:
        G=G.cuda(gpu)
        G.load_state_dict(torch.load(PRETRAINED_PYTORCH_MODEL_PATH, map_location='cuda:0'))
    else:
        G.load_state_dict(torch.load(PRETRAINED_PYTORCH_MODEL_PATH, map_location='cuda:0'))

    return generate_image(G, image, gpu)

def download_pytorch_model_if_necessary(force=False):
    if not PRETRAINED_PYTORCH_MODEL_PATH.exists() or force:
        download_to_path(PRETRAINED_PYTORCH_MODEL_DOWNLOAD_URL, PRETRAINED_PYTORCH_MODEL_PATH)
    #if not PYTORCH_MODEL_PATH.exists() or force:
        #download_to_path(PYTORCH_MODEL_DOWNLOAD_URL, PYTORCH_MODEL_PATH)
