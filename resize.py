
# Improting Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open('/home/antpc/anuja/Pytorch-UNet1/road_4.jpeg')

# Size of the image in pixels (size of orginal image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
# left = 4
# top = height / 5
# right = 154
# bottom = 3 * height / 5

# Cropped image of above dimension
# (It will not change orginal image)
# im1 = im.crop((left, top, right, bottom))
newsize = (1280, 720)
im1 = im.resize(newsize)
im1 = im1.save("/home/antpc/anuja/Pytorch-UNet1/road_3.jpeg")
# Shows the image in image viewer
# im1.show()

