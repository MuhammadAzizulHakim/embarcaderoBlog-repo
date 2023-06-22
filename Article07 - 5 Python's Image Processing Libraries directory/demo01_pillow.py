from __future__ import print_function
from PIL import Image
 
im = Image.open("C:/Users/YOUR_USERNAME/cat1.jpg")
box = (0, 0, 540, 720)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
region = region.transpose(Image.FLIP_LEFT_RIGHT)
im.paste(region, box)
im = im.rotate(45)
im.save("C:/Users/YOUR_USERNAME/cat1Rotated.jpg")