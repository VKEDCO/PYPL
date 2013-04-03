'''
========================================================
Module: pixel_sequence.py
Description: An example of the Python Mutable Sequence
Protocol PixSeq treats a PIL image as a mutable sequence.

Example:

>>> ps = PixSeq(5, 3) ## construct 5x3 PIL image
>>> ps[7]             ## access pixel 7
(0, 0, 0)
>>> ps[7] = (10, 255, 201) ## assign value to pixel 7
>>> len(ps)   ## compute number of pixels
15
>>> del ps[7] ## delete pixel 7
>>> ps[7]     ## accessing pixel 7 returns KeyError
KeyError
>>> ps[7] = (10, 11, 203) ## reassign value to pixel 7
>>> ps[7]     ## check reassigned value of pixel 7
(10, 11, 203)
>>> ps[15]    ## key 15 is not in pixel sequence
IndexError
>>> ps['15']  ## strings are not legal keys
TypeError
>>> ps[7] = (1, 1, -1) ## -1 is not in [0, 255]
ValueError
>>> ps[7] = (1, 256, 1) ## 256 is not in [0, 255]
ValueError

Bugs to vladimir dot kulyukin at gmail dot com
=======================================================
'''

__metaclass__ = type

## import PIL's Image
import Image

class PixSeq:
    ## x - width, y - height
    def __init__(self, x=0, y=0):
        self.__img = Image.new('RGB', (x, y), (0, 0, 0))
        ## __delPix is a dictionary of deleted pixels
        self.__delPix = {}

    def __del__(self):
        del self.__img

    ## ************************************************
    ## (semi)private support functions: __isValidKey,
    ## __isValidValue, and __pixCoords
    ## ************************************************
    
    ## key is valid if it is int or long and
    ## is in the range [0, length-1], where
    ## length = x * y = __img.size[0]*__img.size[1]-1.
    def __isValidKey(self, key):
        if not isinstance(key, (int, long)):
            raise TypeError
        elif key < 0 or key > self.__img.size[0] * self.__img.size[1] - 1:
            raise IndexError
        else:
            return True

    ## value is valid if it is a tuple with three elements
    ## each of which is in the range [0, 255]
    def __isValidValue(self, value):
        if not isinstance(value, tuple):
            raise TypeError
        elif len(value) != 3:
            raise ValueError
        else:
            v1, v2, v3 = value
            if v1 < 0 or v1 > 255:
                raise ValueError
            elif v2 < 0 or v2 > 255:
                raise ValueError
            elif v3 < 0 or v3 > 255:
                raise ValueError
            else:
                return True

    ## y * width + x = key
    ## x = key % width
    ## y = (key - x)/width
    ## Since we are in PIL, x is horizontal dimension,
    ## y is vertical
    ## Example: Consider this 5 x 3 image
    ##    | 0 | 1 | 2 | 3 | 4 |
    ## -------------------------
    ##  0 |   |   |   |   |   |
    ## -------------------------
    ##  1 |   |   |   |   |   |
    ## -------------------------
    ##  2 |   |   |   |   |   |
    ## -------------------------
    ## 1) __pixCoords(self, 2):
    ## Then key = 2, width = 5.
    ## x = 2 % 5 = 2
    ## y = (2 - 2)/5 = 0
    ## so __pixCoords returns (2, 0) marked with *
    ## in the image below:
    ##    | 0 | 1 | 2 | 3 | 4 |
    ## -------------------------
    ##  0 |   |   | * |   |   |
    ## -------------------------
    ##  1 |   |   |   |   |   |
    ## -------------------------
    ##  2 |   |   |   |   |   |
    ## -------------------------
    ## 2) __pixCoords(self, 7)
    ## Then key = 7, width = 5
    ## x = 7 % 5 = 2
    ## y = (7 - 2)/5 = 1
    ## so __pixCoords returns (2, 1) marked with *
    ## in the image below:
    ##    | 0 | 1 | 2 | 3 | 4 |
    ## -------------------------
    ##  0 |   |   |   |   |   |
    ## -------------------------
    ##  1 |   |   | * |   |   |
    ## -------------------------
    ##  2 |   |   |   |   |   |
    ## -------------------------
    def __pixCoords(self, key):
        width = self.__img.size[0]
        x = key % width
        y = (key - x)/width
        return (x, y)

    ## ************************************************
    ## Magic Methods of the Python Sequence Protocol:
    ## __len__, __getitem__, __setitem__, __delitem__
    ## ************************************************
    def __len__(self):
        x, y = self.__img.size
        return x * y

    def __getitem__(self, key):
        try:
            self.__isValidKey(key)
        except (TypeError, IndexError), ex:
            raise ex
        else:
            if not self.__delPix.has_key(key):
                return self.__img.getpixel(self.__pixCoords(key))
            else:
                raise KeyError

    def __setitem__(self, key, value):
        try:
            self.__isValidKey(value)
            self.__isValidValue(value)
        except (TypeError, IndexError), ex:
            raise ex
        else:
            ## get the x,y coords from key
            pix_coords = self.__pixCoords(key)
            if self.__delPix.has_key(key):
                ## if key has been deleted, reinstate it
                del self.__delPix[key]
                self.__img.putpixel(pix_coords, value)
            else:
                self.__img.putpixel(pix_coords, value)

    def __delitem__(self, key):
        try:
            self.__isValidKey(key)
        except (TypeError, IndexError), ex:
            raise ex
        else:
            self.__delPix[key] = True
    

     
