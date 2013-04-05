'''
==============================================================
Module: run_length_tile_ornament.py
Description:

1. Drawing tile ornaments with run-length encoding.
2. A tile ornament is defined as an RGB image divided into
rows of square tiles. Each row of square tiles is
represented as a sequence of runs of squares of specific
colors.

Example:

Let us define three RGB colors: r - red, w - white, o - blue

r, w, o = (255, 0, 0), (255, 255, 255), (0, 0, 255)

Then we can represent a 10x10 tile ornament as follows:

ornament_01 = [
        [(1, r, o), (8, w, o), (1, r, o)],
        [(1, w, o), (1, r, o), (6, w, o), (1, r, o), (1, w, o)],
        [(2, w, o), (1, r, o), (4, w, o), (1, r, o), (2, w, o)],
        [(3, w, o), (1, r, o), (2, w, o), (1, r, o), (3, w, o)],
        [(4, w, o), (2, r, o), (4, w, o)],
        [(4, w, o), (2, r, o), (4, w, o)],
        [(3, w, o), (1, r, o), (2, w, o), (1, r, o), (3, w, o)],
        [(2, w, o), (1, r, o), (4, w, o), (1, r, o), (2, w, o)],
        [(1, w, o), (1, r, o), (6, w, o), (1, r, o), (1, w, o)],
        [(1, r, o), (8, w, o), (1, r, o)],
        ]

In this ornament, row 0 consists of 1 red tile with blue outline (1, r, 0),
8 white tiles with a blue outline (8, w, 0), and 1 red tile with a blue
outline. Row 1 consists of 1 white tile with a blue outline, 1 red tile
with a blue outline, 6 white tiles with a blue outline, 1 red tile with
a blue outline, and 1 white tile with a blue outline.

See http://www.youtube.com/watch?v=piWKJpiC94o for details.

3. Tiles can be generated for ornament representations with

- draw_tile_ornament(imgpath='', imgsize=(0, 0), ornament=[], tileside=1)
- draw_tile_ornament_with_ImageDraw(idraw, ornament, side)

See tests at the end of the module for examples.

Bugs, comments to vladimir dot kulyukin at gmail dot com
=========================================================
'''

import Image
import ImageDraw

def square_bottom_right(top_left_xy, side):
    '''
    square_bottom_right returns the tuple encoding the x, y coordinates
    of the bottom right of the square given the square's top left coordinates
    and its side
    '''
    top_x, top_y = top_left_xy[0], top_left_xy[1]
    return (top_x + side-1, top_y + side-1)

def draw_square(idraw, top_left=(0, 0), side=1,
                fill_color=(0,0,0), outline_color=(0,0,0)):
    '''
    draw_square uses ImageDraw.rectangle() to draw a square
    - idraw is ImageDraw
    - top_left is the top left of the square
    - side is the number of pixels in the side of the square
    - fill_color is the fill color of the square
    - outline color is the outline color of the square
    '''
    idraw.rectangle((top_left, square_bottom_right(top_left, side)),
                    fill=fill_color, outline=outline_color)

## Sample row_run is [(1, r, o), (8, w, o), (1, r, o)].
def draw_tile_run(idraw, row_run, row_num, tileside):
    '''
    draw_tile_run draws a row of square tiles in the image
    - idraw is an ImageDraw object
    - run_run is a list with run-length encodings of tiles
    - row_num is the number of the tile row in the image
    - side is the side of the square tile
    '''
    current_x, y_coord = 0, tileside*row_num
    for re in row_run:
        run_len, fill, outline = re[0], re[1], re[2]
        while run_len > 0:
            draw_square(idraw, top_left=(current_x, y_coord),
                        side=tileside,
                        fill_color=fill,
                        outline_color=outline)
            run_len -= 1
            current_x += tileside

def draw_tile_ornament(imgpath='', imgsize=(0, 0),
                       ornament=[], tileside=1):
    '''
    Create an RGB image with white background, draw a tile ornament on it
    and save the image.
    - imgpath is a path to the file where the generated image is saved
    - imgsize is the size of the image (should be a multiple of tileside)
    - ornament is the run length encoding of a tile ornament
    - tileside is the side of the square tile in pixels
    '''
    im = Image.new('RGB', imgsize, (255, 255, 255))
    idraw = ImageDraw.Draw(im)
    for row_run, row_num in zip(ornament, xrange(len(ornament))):
        draw_tile_run(idraw, row_run, row_num, tileside)
    im.save(imgpath)
    del im
    del idraw

def draw_tile_ornament_with_ImageDraw(idraw, ornament, side):
    '''
    Use an ImageDraw object to draw a tile ornament in the image
    associated with that object
    - idraw is an ImageDraw object
    - ornament is a run-length encoding of a tile ornament
    - side is the length of a square tile in pixels
    '''
    for row_run, row_num in zip(ornament, xrange(len(ornament))):
        ## print (row_num, row_num)
        draw_tile_run(idraw, row_run, row_num, side)

############################## TESTS ###############################
      
## r is red, w -is white, o is outline color (blue)
r, w, o = (255, 0, 0), (255, 255, 255), (0, 0, 255)

## first tile ornament.
## row 0 consists of 1 red tile with blue outline,
## 8 white tiles with blue outline, and 1 red
## tile with blue outline, etc.
## This ornament has 10 rows each of which has 10 tiles
ornament_01 = [
        [(1, r, o), (8, w, o), (1, r, o)],
        [(1, w, o), (1, r, o), (6, w, o), (1, r, o), (1, w, o)],
        [(2, w, o), (1, r, o), (4, w, o), (1, r, o), (2, w, o)],
        [(3, w, o), (1, r, o), (2, w, o), (1, r, o), (3, w, o)],
        [(4, w, o), (2, r, o), (4, w, o)],
        [(4, w, o), (2, r, o), (4, w, o)],
        [(3, w, o), (1, r, o), (2, w, o), (1, r, o), (3, w, o)],
        [(2, w, o), (1, r, o), (4, w, o), (1, r, o), (2, w, o)],
        [(1, w, o), (1, r, o), (6, w, o), (1, r, o), (1, w, o)],
        [(1, r, o), (8, w, o), (1, r, o)],
        ]

## second tile ornament
## this ornament has 9 rows each of which has 31 tiles
ornament_02 = [
    [(5, w, o), (1, r, o), (3, w, o), (1, r, o), (11, w, o), (1, r, o), (3, w, o), (1, r, o), (5, w, o)],
    [(4, w, o), (3, r, o), (1, w, o), (3, r, o), (9, w, o), (3, r, o), (1, w, o), (3, r, o), (4, w, o)],
    [(5, w, o), (5, r, o), (11, w, o), (5, r, o), (5, w, o)],
    [(2, w, o), (1, r, o), (3, w, o), (3, r, o), (3, w, o), (1, r, o), (5, w, o), (1, r, o), (3, w, o), (3, r, o),
     (3, w, o), (1, r, o), (2, w, o)],
    [(1, w, o), (3, r, o), (1, w, o), (5, r, o), (1, w, o), (3, r, o), (3, w, o), (3, r, o),
     (1, w, o), (5, r, o), (1, w, o), (3, r, o), (1, w, o)],
    [(2, w, o), (5, r, o), (1, w, o), (5, r, o), (5, w, o), (5, r, o), (1, w, o), (5, r, o), (2, w, o)],
    [(3, w, o), (3, r, o), (3, w, o), (3, r, o), (3, w, o), (1, r, o), (3, w, o), (3, r, o), (3, w, o),
     (3, r, o), (3, w, o)],
    [(1, r, o), (1, w, o), (3, r, o), (5, w, o), (3, r, o), (1, w, o), (3, r, o), (1, w, o), (3, r, o),
     (5, w, o), (3, r, o), (1, w, o), (1, r, o)],
    [(31, r, o)]
    ]

## test draw_square()
## Example:
## >>> test_01('test_01.bmp', 100, 100)
def tile_01(impath, imx, imy):
    im = Image.new('RGB', (imx, imy), (255, 255, 255))
    idraw = ImageDraw.Draw(im)
    draw_square(idraw, (10, 10), 20,
                fill_color=(255, 0, 0),
                outline_color=(0, 0, 255))
    im.save(impath)
    del im
    del idraw

## test draw_tile_run
## Example:
## row_run = [(1, r, o), (8, w, o), (1, r, o)]
## >>> test_02('test_02.bmp', 100, 100, row_run)
def tile_02(impath, imx, imy, row_run):
    im = Image.new('RGB', (imx, imy), (255, 255, 255))
    idraw = ImageDraw.Draw(im)
    red, white = (255, 0, 0), (255, 255, 255)
    outline = (0, 0, 255)
    draw_tile_run(idraw, row_run, 0, 10)
    im.save(impath)
    del im
    del idraw

## drawing ornament_01 with draw_tile_ornament
## Example:
## >>> test_03('test_03.bmp')
def tile_03(impath):
    draw_tile_ornament(imgpath=impath, imgsize=(100, 100), ornament=ornament_01,
                       tileside=10)

## drawing ornament_01 with draw_tile_ornament_with_ImageDraw
## Example:
## >>> test_04('test_04.bmp', 200, 200, 20)
def tile_04(impath, imx, imy, tileside):
    im = Image.new('RGB', (imx, imy), (255, 255, 255))
    idraw = ImageDraw.Draw(im)
    draw_tile_ornament_with_ImageDraw(idraw, ornament_01, tileside)
    im.save(impath)
    del im
    del idraw

## drawing ornament_02 with draw_tile_ornament
## Example:
## >>> test_05('test_05.bmp')
def tile_05(impath):
    ## imx=310 and imy=90 are multiples of tileside=10
    draw_tile_ornament(imgpath=impath, imgsize=(310, 90),
                       ornament=ornament_02,
                       tileside=10)

## drawing ornament_02 with draw_tile_ornament_with_ImageDraw
## Example:
## >>> test_06('test_06.bmp', 620, 180, 20)
## Note that imx=620 and imy=180 are multiples of tileside=20.
def tile_06(impath, imx, imy, tileside):
    im = Image.new('RGB', (imx, imy), (255, 255, 255))
    idraw = ImageDraw.Draw(im)
    draw_tile_ornament_with_ImageDraw(idraw, ornament_02, tileside)
    im.save(impath)
    del im
    del idraw

## run all tests
## Example:
## >>> test_07('images/tile_ornaments/')
def all_tiles(dir):
    tile_01(dir + 'tile_01.bmp', 100, 100)
    tile_02(dir + 'tile_02.bmp', 100, 100,
            [(1, r, o), (8, w, o), (1, r, o)])
    tile_03(dir + 'tile_03.bmp')
    tile_04(dir + 'tile_04.bmp', 200, 200, 20)
    tile_05(dir + 'tile_05.bmp')
    tile_06(dir + 'tile_06.bmp', 620, 180, 20)
