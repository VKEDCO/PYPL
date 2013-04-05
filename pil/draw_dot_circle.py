#!/usr/bin/python

'''
==============================================
draw_dot_circle.py

bugs to vladmir dot kulyukin at gmail dot com
==============================================
'''
import Image
from math import cos, sin, pi, radians

def make_dot_circle_image(img_fp, img_size=100, radius=30,
                          img_background='white',
                          dot_color=(0, 0, 255)):
    """
    creates an image with a circle drawn in its center dot by dot
    """
    img = Image.new('RGB', (img_size, img_size), img_background)

    center_x = center_y = img_size / 2 

    # make sure circle can fit in image
    if radius > (img_size/2 - 1): radius = img_size/2 - 1

    # Does not draw line, only 360 dots
    for angle in range(361):
        theta = radians(angle)
        x = center_x + radius * cos(theta)
        y = center_y + radius * sin(theta)
        img.putpixel((int(x), int(y)), dot_color)
        

    # save img object into image_fp
    img.save(img_fp)
    # delete img object
    del img
    

print "Creating image file"
make_dot_circle_image("dot_circle.bmp")
