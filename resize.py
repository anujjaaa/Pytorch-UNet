
# Improting Image class from PIL module
# from PIL import Image

# Opens a image in RGB mode
# im = Image.open('/home/antpc/anuja/Pytorch-UNet1/road_4.jpeg')
# width, height = im.size
# newsize = (1280, 720)
# im1 = im.resize(newsize)
# im1 = im1.save("/home/antpc/anuja/Pytorch-UNet1/road_3.jpeg")


#!/usr/bin/python
from PIL import Image
import os, sys

path = "/home/antpc/anuja/Pytorch-UNet1/data/data/Labels/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((640,480), Image.ANTIALIAS)
            imResize.save('/home/antpc/anuja/Pytorch-UNet1/data/data/Labels_resize/' + item , 'JPEG', quality=90)

resize()