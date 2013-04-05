#!/usr/bin/python

'''
==============================================
draw_text.py

bugs to vladmir dot kulyukin at gmail dot com
==============================================
'''

import Image, ImageDraw, ImageFont
    
def make_centered_text(imageName, text, width=700,
                           height=200,
                          font = None, color = (0,0,0)):
    """
    Draws the text on an image.  If no font is provided, loads
    the default font.
    """

    ## 1. get the font, if no font available, load the
    ## default font
    if font == None:
        font = ImageFont.load_default()

    ## 2. create a new image with the white background
    im = Image.new('RGB', (width, height), 'white')

    ## 3. get ready to draw
    draw = ImageDraw.Draw(im)

    ## 4. figure out how big the text will be in the font
    font_width, font_height =  font.getsize(text)

    ## 5. find the center of the image
    img_center_x, img_center_y = width/2 - 1, height/2 - 1

    ## 6. find the position for the upper left corner of the text
    text_x = img_center_x - font_width/2
    text_y = img_center_y - font_height/2

    ## 7. draw the text
    draw.text((text_x, text_y), text, font = font, fill = color)
    del draw

    ## 8. save the image
    im.save(imageName)
    del im


def make_helvetica_centered_text(imageName, text, width=700, height=300,
                                 color = (0,0,0)):
    """
    Draws the text on an image.
    If you have not downloaded the font, this function will
    probably crash.
    """

    # Try loading the font
    my_font = ImageFont.load('C:/Python27/pilfonts/helvR24.pil')
    make_centered_text(imageName, text, width, height, my_font, color)

text = 'The way of Truth is written in the sands.'

print "Creating image default_text.png with the default font"
make_centered_text('default_text.png', text, color=(255, 0, 0))

print "Creating image helvetica_text.png with the Helvetica font"
make_helvetica_centered_text('helvetica_text.png', text,
                             color=(0, 0, 255))

 
