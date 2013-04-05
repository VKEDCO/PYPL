#!/usr/bin/python

'''
================================================================================
1. Python Generator Factories, Generator Objects, and Generator Comprehension
2. Converting RGB Images to Gray-Level Images through Relative Luminance
3. Basic image processing with Python Image Library (PIL)

>>> im = Image.open('android_icon_large.png')
>>> gray_im = rgb_to_gray(im)
>>> gray_im.save('android_icon_large_gray.png')
>>> gray_im_bin = binarize_gray(gray_im)
>>> gray_im_bin.save('android_icon_large_gray_bin.png')
>>> rgb_im_bin = binarize_rgb(im)
>>> rgb_im_bin.save('android_icon_large_rgb_bin.png')

bugs to vladimir dot kulyukin at gmail dot com
================================================================================
'''
import Image
import os

## relative luminance conversion formula from
## http://en.wikipedia.org/wiki/Luminance_(relative)
def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

## take a PIL rgb image and produce a factory that yields
## ((x, y), (r, g, b)), where (x, y) are the coordinates
## of a pixel, (x, y), and its RGB values.
def gen_pix_factory(im):
    num_cols, num_rows = im.size
    c, r = 0, 0
    while r != num_rows:
        c = c % num_cols
        yield ((c, r), im.getpixel((c, r)))
        if c == num_cols - 1: r += 1
        c += 1

## take a PIL RBG image and a luminosity conversion formula,
## and return a new gray level PIL image in which
## each pixel is obtained by applying the luminosity formula
## to the corresponding pixel in the RGB image.
def rgb_to_gray(rgb_img, conversion=luminosity):
    gray_img = Image.new('L', rgb_img.size)
    gen_pix = gen_pix_factory(rgb_img)
    lum_pix = ((gp[0], conversion(gp[1])) for gp in gen_pix)
    for lp in lum_pix:
        gray_img.putpixel(lp[0], int(lp[1]))
    return gray_img

## take a gray level image an a gray level threshold
## and replace a pixel's gray level with 0 (black) if
## its gray level value is <= than the threshold and
## with 255 (white) if it is > than the threshold.
def binarize_gray(gray_img, thresh=100):
    gen_pix = gen_pix_factory(gray_img)
    for pix in gen_pix:
        if pix[1] <= thresh:
            gray_img.putpixel(pix[0], 0)
        else:
            gray_img.putpixel(pix[0], 255)
    return gray_img

def binarize_rgb(rgb_img, thresh=70):
    return binarize_gray(rgb_to_gray(rgb_img))

def img_test(img_dir, img_name):
    img_path = os.path.join(img_dir, img_name)
    file_ext = os.path.splitext(img_path)[-1].lower()
    img_gray_path = os.path.splitext(img_path)[-2] + '_gray' + file_ext
    img_bin_path = os.path.splitext(img_path)[-2] + '_bin' + file_ext
    img_bin_path_2 = os.path.splitext(img_path)[-2] + '_bin2' + file_ext
    print img_gray_path, "\n"
    im = Image.open(img_path)
    ## 1. convert rgb to gray level
    gray_im = rgb_to_gray(im)
    gray_im.save(img_gray_path)
    ## 2. binarize and save
    bin_im = binarize_gray(gray_im)
    bin_im.save(img_bin_path)
    bin_im2 = binarize_rgb(im)
    bin_im2.save(img_bin_path_2)
    del im
    del gray_im
    del bin_im
    del bin_im2



