
# Improting Image class from PIL module
# from PIL import Image

# Opens a image in RGB mode
# im = Image.open('/Pytorch-UNet1/road_4.jpeg')
# width, height = im.size
# newsize = (1280, 720)
# im1 = im.resize(newsize)
# im1 = im1.save("Pytorch-UNet1/road_3.jpeg")


from PIL import Image
import os, sys

# path = "/data/data/Labels/"
# dirs = os.listdir( path )
#
# def resize():
#     for item in dirs:
#         if os.path.isfile(path+item):
#             im = Image.open(path+item)
#             f, e = os.path.splitext(path+item)
#             imResize = im.resize((640,480), Image.ANTIALIAS)
#             imResize.save('/data/Labels_resize/' + item , 'JPEG', quality=90)
#
# resize()