#!/usr/bin/python

import math
import Image
import sys
import itertools

## @author: vladimir kulyukin

def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

## im is a PIL Image object.
def is_in_range(im, cr):
    return cr[0] > 0 and cr[0] < im.size[0]-1 and cr[1] > 0 and cr[1] < im.size[1]-1

## In PIL, c = x, r = y
def rgb_pix_dy(rgb_img, cr, flumin, default_delta):
    if not is_in_range(rgb_img, cr): return default_delta
    c, r = cr
    dy = flumin(rgb_img.getpixel((c, r-1))) - flumin(rgb_img.getpixel((c, r+1)))
    if dy == 0:
        return default_delta
    else:
        return float(dy)
    
def rgb_pix_dx(rgb_img, cr, flumin, default_delta):
    if not is_in_range(rgb_img, cr): return default_delta
    c, r = cr
    dx = flumin(rgb_img.getpixel((c+1, r))) - flumin(rgb_img.getpixel((c-1, r)))
    if dx == 0:
        return default_delta
    else:
        return float(dx)

def grad_magn(pdx, pdy):
    return math.sqrt(math.pow(pdx, 2.0) + math.pow(pdy, 2.0))

## if pdy == pdx, we return a default_theta value outside of [-pi, pi]
## gradient orientation
def grad_theta(pdx, pdy, default_delta, default_theta):
    if pdy == pdx == default_delta: return default_theta
    th = math.atan2(pdy,pdx)*(180/math.pi)
    if th < 0:
        return math.floor(th)
    elif th > 0:
        return math.ceil(th)
    else:
        return th

def gen_cr(num_cols, num_rows):
    r, c = 0, 0
    while r != num_rows:
        c = c % num_cols
        yield (c, r)
        if c == num_cols - 1: r += 1
        c += 1

def detect_edges(rgb_img, ftheta=grad_theta, fmagn=grad_magn,
                 fpixdx=rgb_pix_dx, fpixdy=rgb_pix_dy, flumin=luminosity,
                 default_delta=1.0, default_theta=-200,
                 theta_thresh=360, magn_thresh=20):
    output_img = Image.new('L', rgb_img.size)
    num_cols, num_rows = rgb_img.size
    gdxdy = ((fpixdx(rgb_img, cr, flumin, default_delta),
              fpixdy(rgb_img, cr, flumin, default_delta))
             for cr in gen_cr(num_cols, num_rows))
    gthetas_magns = ((int(ftheta(dxdy[0], dxdy[1], default_delta, default_theta)),
                      int(fmagn(dxdy[0], dxdy[1])))
                     for dxdy in gdxdy)
    for cr_thmagn in itertools.izip(gen_cr(num_cols, num_rows), gthetas_magns):
        cr, thetamagn = cr_thmagn
        theta, magn = thetamagn
        if abs(theta) <= theta_thresh and magn >= magn_thresh:
            output_img.putpixel(cr, 255)
        else:
            output_img.putpixel(cr, 0)
    return output_img

if __name__ == '__main__':
    input_image = Image.open(sys.argv[1])
    output_image = detect_edges(input_image)
    output_image.save(sys.argv[2])
    del input_image
    del output_image


