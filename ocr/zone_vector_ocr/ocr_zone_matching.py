'''
=========================================================================
Module: ocr_zone_matching.py
Description: implements basics of zone vector matching in OCR.
Zone matching is a technique used in computer vision for image matching.
An image is divided into several sub-images, called zones. In each zone,
a specific statistic is computed. For example, that statistic can be the
number of horizontal lines or the number of pixels of a specific color.
The sequence of statistics constitutes the zone vector for the image.
More info at:
http://www.youtube.com/watch?v=Q5zucrH8aEw
http://www.youtube.com/watch?v=Q5zucrH8aEw

The module implements the following basic functions described below:
1) zone_vector(imgpath, zone_coords);
2) build_zone_vector_map(dir, zone_coords);
3) find_best_zv_char_match(char_zv, zv_map, similarity=cosine_similarity);
4) find_all_zv_char_matches(char_zv, zv_map, similarity=cosine_similarity).

Bugs to vladimir dot kulyukin at gmail dot com

1) zone_vector(imgpath, zone_coords)
- imgpath is a path of an 20 x 20 RGB bitmap with a single character
- zone_coords is a list of 4-tuples, each of which specifies the top
left and bottom right coordinates of a 5x5 zone
 
The zone_vector function returns the list of black pixel counts in each
of the 16 zones:

>>> zone_vector('letter_images_courR18/A.BMP', zone_coords)
[2, 13, 1, 0, 0, 12, 10, 0, 6, 13, 15, 0, 6, 6, 10, 2]

2) build_zone_vector_map(dir, zone_coords)
- dir is a directory, zone_coords is a sequence of zone coords (4-tuples)
- dir is assumped to store 20x20 RGB bitmaps of 26 ASCII characters: A.bmp,
B.bmp, C.bmp, etc.

The function build_zone_vector_map returns a dictionary that maps characters
to their zone vectors:

>>> zv_map = build_zone_vector_map('letter_images_courR18/',
                                    zone_coords)
>>> zv_map
{'A': [2, 13, 1, 0, 0, 12, 10, 0, 6, 13, 15, 0, 6, 6, 10, 2],
'C': [1, 10, 12, 0, 9, 2, 4, 0, 8, 4, 2, 0, 0, 8, 8, 0],
'B': [4, 12, 10, 0, 0, 16, 16, 0, 0, 10, 7, 5, 4, 10, 9, 0],
'E': [4, 12, 12, 0, 0, 16, 12, 0, 0, 10, 7, 3, 4, 10, 10, 2],
'D': [7, 11, 9, 0, 5, 5, 7, 4, 5, 5, 8, 3, 6, 10, 7, 0],
'G': [1, 10, 11, 3, 9, 2, 2, 2, 8, 4, 14, 5, 0, 8, 8, 0],
'F': [4, 12, 11, 3, 0, 16, 10, 2, 0, 10, 4, 0, 4, 10, 2, 0],
'I': [2, 12, 8, 0, 0, 10, 0, 0, 0, 10, 0, 0, 2, 10, 8, 0],
'H': [7, 7, 12, 2, 5, 13, 14, 0, 5, 5, 10, 0, 6, 6, 10, 2],
'K': [7, 7, 13, 0, 5, 18, 3, 0, 5, 9, 11, 0, 6, 6, 6, 2],
'J': [0, 8, 12, 2, 0, 0, 10, 0, 8, 1, 11, 0, 1, 10, 3, 0],
'M': [8, 4, 10, 2, 10, 11, 19, 0, 10, 4, 10, 0, 6, 4, 8, 2],
'L': [4, 12, 2, 0, 0, 10, 0, 0, 0, 10, 6, 0, 4, 10, 10, 0],
'O': [1, 10, 9, 0, 9, 2, 7, 4, 8, 4, 9, 3, 0, 8, 6, 0],
'N': [5, 7, 10, 2, 5, 15, 10, 0, 5, 7, 18, 0, 4, 6, 7, 0],
'Q': [1, 10, 9, 0, 9, 2, 7, 4, 8, 4, 9, 3, 0, 19, 16, 2],
'P': [4, 12, 10, 1, 0, 10, 6, 5, 0, 16, 8, 0, 4, 10, 2, 0],
'S': [1, 11, 12, 0, 3, 13, 7, 0, 6, 2, 14, 0, 4, 9, 7, 0],
'R': [7, 11, 7, 0, 5, 9, 12, 0, 5, 10, 11, 0, 6, 6, 6, 2],
'U': [5, 7, 10, 2, 5, 5, 10, 0, 4, 6, 10, 0, 0, 9, 7, 0],
'T': [6, 12, 12, 0, 6, 10, 6, 0, 0, 10, 0, 0, 0, 10, 6, 0],
'W': [8, 4, 10, 2, 10, 14, 14, 0, 7, 11, 18, 0, 2, 4, 6, 0],
'V': [8, 4, 10, 2, 5, 5, 10, 0, 0, 11, 9, 0, 0, 6, 2, 0],
'Y': [8, 7, 13, 2, 1, 13, 10, 0, 0, 10, 0, 0, 0, 10, 6, 0],
'X': [8, 7, 13, 2, 1, 14, 9, 0, 3, 11, 12, 0, 6, 6, 10, 2],
'Z': [3, 11, 13, 0, 2, 5, 11, 0, 1, 13, 6, 0, 2, 10, 10, 0]}

3) find_best_zv_char_match(char_zv, zv_map, similarity=cosine_similarity)
- char_zv is a zone vector of a specific character
- zv_map is a dictionary computed by build_zone_vector_map
- similarity if a similarity function that computes the similarity coefficient
of two vectors as explained above; the function defaults to cosine_similarity

The  find_best_zv_char_match function computes the similarity coefficients
between char_zv and each zone vector in zv_map and returns a 2-tuple
(character, similarity) describing the best matching character, i.e., the
character in zv_map whose zone vector is closest to char_zv.

## Assume that these two directories store 26 images each of characters generated
## with two PIL fonts: helvR18 (helvetica)
## and courR18 (courier). You can download both directories from the links below.
>>>  helvR18_dir = 'letter_images_helvR18/'
>>> courR18_dir = 'letter_images_courR18/'
## Build zone vector maps of both directories
>>> zv_helvR18_map = build_zone_vector_map(helvR18_dir, zone_coords)
>>> zv_courR18_map = build_zone_vector_map(courR18_dir, zone_coords)
## Find which courier character in the courier map best matches 'A' in the helvetica map:
>>> find_best_zv_char_match(zv_helvR18_map['A'], zv_courR18_map)
('A', 0.8921846206693678)

4) find_all_zv_char_matches(char_zv, zv_map, similarity=cosine_similarity)
- char_zv is a zone vector of a specific character
- zv_map is a dictionary computed by build_zone_vector_map
- similarity if a similarity function that computes the similarity coefficient
of two vectors as explained above; the function defaults to cosine_similarity

The  find_all_zv_char_match returns a list of all the 2-tuple matches to char_zv in
zv_map sorted by similarity from largest to smallest:

## Build the zone vector maps
>>> zv_helvR18_map = build_zone_vector_map(helvR18_dir, zone_coords)
>>> zv_courR18_map = build_zone_vector_map(courR18_dir, zone_coords)
## Fetch all the matches in the courier map to 'A' in the helvetica map
>>> find_all_zv_char_matches(zv_helvR18_map['A'], zv_courR18_map)
[('A', 0.8921846206693678), ('R', 0.8867527803753008), ('N', 0.857364436133189), ...]
## Fetch all the matches in the courier map to 'A' in the helvetica map
>>> find_all_zv_char_matches(zv_helvR18_map['B'], zv_courR18_map)
[('D', 0.8875154490908648), ('H', 0.8735458011442355), ('M', 0.8631289484030148), ('C', 0.8230426492867466), ...]
=========================================================================
'''

import string
import math
import Image, ImageDraw, ImageFont

zone_coords = ((0, 0, 4, 4),   (5, 0, 9, 4),   (10, 0, 14, 4),   (15, 0, 19, 4),
               (0, 5, 4, 9),   (5, 5, 9, 9),   (10, 5, 14, 9),   (15, 5, 19, 9),
               (0, 10, 4, 14), (5, 10, 9, 14), (10, 10, 14, 14), (15, 10, 19, 14),
               (0, 15, 4, 19), (5, 15, 9, 19), (10, 15, 14, 19), (15, 15, 19, 19))

def zone_color_count(img, xyzw, pix_color=(0, 0, 0)):
    '''
    zone_color_count(img, xyzw, color=(0, 0, 0).
    - img is an RGB bitmap
    - xyzw is a four tuple that specifies the zone in img
    - pix_color specifies the color of the pixels that are counted
    in the zone
    '''
    count = 0
    top_x, top_y, bottom_x, bottom_y = xyzw
    for x in xrange(top_x, bottom_x+1):
        for y in xrange(top_y, bottom_y+1):
            if img.getpixel((x,y)) == pix_color:
                count += 1
    return count

def zone_vector(imgpath, zone_coords, pix_color=(0, 0, 0)):
    '''
    zone_vector(impgpath, zone_specs) -> list of zone counts.
    - imgpath is a path to an 20 x 20 bitmap with a single character.
    - zone_specs is a list of 4-tuples. Each 4-tuple specifies
    the top left and bottom right coordinates of a 5x5 zone.
    - zone_vector returns the list of black pixel counts in each
    of the 16 zones.
    '''
    vector = []
    img = Image.open(imgpath)
    for zc in zone_coords:
        vector.append(zone_color_count(img, zc, pix_color))
    del img
    return vector

def cosine_similarity(zv1, zv2):
    '''
    cosine_similarity(zv1, zv2) -> float
    this function computes the cosine similarity between two
    vectors zv1 and zv2.
    '''
    dotp = sum(map(lambda x, y: x * y, zv1, zv2))
    zmagn1 = math.sqrt(sum([v1*v1 for v1 in zv1]))
    zmagn2 = math.sqrt(sum([v2*v2 for v2 in zv2]))
    return float(dotp)/(zmagn1 * zmagn2)

def build_zone_vector_map(dir, zone_coords):
    '''
    build_zone_vector_map(dir, zone_coords) -> dictionary
    - dir is a directory, zone_coords is a sequence of zone coords (4-tuples).
    - dir is assumped to store 20x20 bitmaps of 26 ASCII characters: A.bmp, B.bmp, C.bmp, etc.
    - build_zone_vector_map returns a dictionary that maps characters to their
    zone vectors.
    '''
    dict = {}
    for letter in string.ascii_uppercase:
        dict[letter] = zone_vector(dir + letter + '.bmp', zone_coords)
    return dict

def find_best_zv_char_match(char_zv, zv_map, similarity=cosine_similarity):
    '''
    - char_zv is a zone vector of a specific character
    - zv_map is a dictionary computed by build_zone_vector_map
    - similarity if a similarity function that computes the similarity coefficient
    of two vectors as explained above; the function defaults to cosine_similarity

    The  find_best_zv_char_match function computes the similarity coefficients
    between char_zv and each zone vector in zv_map and returns a 2-tuple
    (character, similarity) describing the best matching character, i.e., the
    character in zv_map whose zone vector is closest to char_zv.
    '''
    best_zv_match = 0.0
    best_char = None
    for char, zone_vector in zv_map.items():
        curr_match = similarity(char_zv, zone_vector)
        if curr_match > best_zv_match:
            best_zv_match = curr_match
            best_char = char 
    return (best_char, best_zv_match)

def find_all_zv_char_matches(char_zv, zv_map, similarity=cosine_similarity):
    '''
    - char_zv is a zone vector of a specific character
    - zv_map is a dictionary computed by build_zone_vector_map
    - similarity if a similarity function that computes the similarity
    coefficient of two vectors as explained above; the function defaults
    to cosine_similarity

    The  find_all_zv_char_match returns a list of all the 2-tuple matches
    to char_zv in zv_map sorted by similarity from largest to smallest.
    '''
    def zv_match_cmp(m1, m2):
        return -cmp(m1[1], m2[1])
    scores = []
    for char, zone_vector in zv_map.items():
        scores.append((char, similarity(char_zv, zone_vector)))
    scores.sort(zv_match_cmp)
    return scores


#####################################################################
##
##    CREATING TEXT IMAGES WITH DIFFERENT PIL FONTS
##
#####################################################################

## Change these variables to reference the directories where
## you want to store letter bitmaps (folder) and which font
## you want to use (fontpath).
folder = 'letter_images/'
fontpath = 'C:/Python27/pilfonts/helvR18.pil'


## Sample calls:
## make_centered_text('default_text.png', 'Hello, Python!', color=(255, 0, 0))
## make_helvetica_centered_text('helvetica_text.png', 'Hello, Python!', color=(0, 0, 255))
def make_centered_text(imageName, text, size = 300,
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
    im = Image.new('RGB', (size, size), 'white')

    ## 3. get ready to draw
    draw = ImageDraw.Draw(im)

    ## 4. figure out how big the text will be in the font
    sWidth, sHeight =  font.getsize(text)

    ## 5. find the center of the image
    centerX = centerY = (size/2 - 1)

    ## 6. find the position for the upper left corner of the text
    x = centerX - sWidth/2
    y = centerY - sHeight/2

    ## 7. draw the text
    draw.text((x,y), text, font = font, fill = color)
    del draw

    ## 8. save the image
    im.save(imageName)
    del im

def make_helvetica_centered_text(imageName, text, size = 300,
                                 color = (0,0,0)):
    """
    Draws the text on an image.
    If you have not downloaded the font, this function will
    probably crash.
    """

    # Try loading the font
    my_font = ImageFont.load('C:/Python27/pilfonts/helvR24.pil')
    make_centered_text(imageName, text, size, my_font, color)


def make_letter_image(imgName, fontpath, letter, size=20, color=(0, 0, 0)):
    '''
    creates an bitmap image where letter letter is centered.
    '''
    my_font = ImageFont.load(fontpath)
    make_centered_text(imgName, letter, size, my_font, color)

def create_ascii_uppercase_images(folder, fontpath, size=20, color=(0, 0, 0)):
    '''
    creates 26 bitmaps of ASCII uppercase letters with the font specified by font
    in folder specified by fontpath.
    '''
    for c in string.ascii_uppercase:
        make_text_image(folder + c + '.BMP', fontpath, c, size, color)



    


    
