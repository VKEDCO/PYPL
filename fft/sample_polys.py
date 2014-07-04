## =============================================
## Examples of FFT polynomial multiplication
##
## Author: Vladimir Kulyukin
## Bugs to vladimir dot kulyukin at gmail dot com
## =============================================

from fft_mult_poly import convolve_poly_split, convolve_poly, mult_poly

## poly01 = 9 - 10x + 7x^2 + 6x^3
poly01 = [9, -10, 7, 6]
## poly02 = -5 + 4x - 2x^3
poly02 = [-5, 4, 0, -2]
## poly01*poly2 = -45 + 86x - 75x^2 - 20x^3 + 44x^2 - 14x^5 - 12x^6

print 'POLY01 x POLY02'
poly01xpoly02 = convolve_poly_split(poly01, poly02)
print poly01xpoly02
poly01xpoly02 = convolve_poly(poly01, poly02)
print poly01xpoly02
poly01xpoly02 = mult_poly(poly01, poly02)

## poly03 = -10 + x - x^2 + 7x^3
poly03 = [-10, 1, -1, 7]
## poly04 = 3 - 6x + 8x^3
poly04 = [3, -6, 0, 8]
## poly03*poly04 = -30 + 63x - 9x^2 - 53x^3 - 34x^4 - 8x^5 + 56x^6

print 'POLY03 x POLY04'
poly03xpoly04 = convolve_poly_split(poly03, poly04)
print poly03xpoly04
poly03xpoly04 = convolve_poly(poly03, poly04)
print poly03xpoly04
poly03xpoly04 = mult_poly(poly03, poly04)

## poly05 = 2 + 5x
poly05 = [2, 5, 0, 0, 0, 0, 0]
## poly06 = 5 + 2x^5 + 3x^6
poly06 = [5, 0, 0, 0, 0, 2, 3]
## poly05*poly06 = 10 + 25x + 45x^5 + 16x^6 + 15x^7

print 'POLY05 x POLY06'
poly05xpoly06 = convolve_poly_split(poly05, poly06)
print poly05xpoly06
poly05xpoly06 = convolve_poly(poly05, poly06)
print poly05xpoly06
poly05xpoly06 = mult_poly(poly05, poly06)
print poly05xpoly06

import random
rand_poly_01 = [random.randint(0, 100) for i in range(0, 101)]
rand_poly_02 = [random.randint(0, 100) for i in range(0, 101)]

rand_rslt = convolve_poly_split(rand_poly_01, rand_poly_02)
print rand_rslt
rand_rslt = convolve_poly(rand_poly_01, rand_poly_02)
print rand_rslt
rand_rslt = mult_poly(rand_poly_01, rand_poly_02)
print rand_rslt
