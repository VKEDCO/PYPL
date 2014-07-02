## ===================================================
## Multiplication of two polynomials with fast-fourier transforms.
## polynomials are represented as lists of coefficients from
## smallest degree to highest. for example, 9 - 10x + 7x^2 + 6x^2
## is represented as [9, -10, 7, 6].
##
## There are three functions for the user:
## 1. convolve_poly(A, B, wf=dft.omega2, error=0),
## 2. convolve_poly_split(A, B, wf=dft.omega2, error=0),
## 3. mult_poly(A, B)
##
## A and B are array coefficients that must be of the same length.
## wf is a function for computing the complex n-th roots of unity (see
## dft.py for details).
## error is the argument used in wf.
##
## convole_poly returns the result as a list of complex numbers.
## convolve_poly_split returns the result as a tuple of real and imaginary
## numbers by taking the result of convolve_poly and splitting it into
## real and imaginary numbers.
## mult_poly(A, B) does the classic multiplication of polynomials.
##
## Sample run:
## >>> poly01 = [9, -10, 7, 6] ## poly01 = 9 - 10x + 7x^2 + 6x^2
## >>> poly02 = [-5, 4, 0, -2] ## poly02 = -5 + 4x - 2x^2
## poly01*poly2 = -45 + 86x - 75x^2 - 20x^3 + 44x^2 - 14x^5 - 12x^6
## >>> poly01xpoly02 = convolve_poly_split(poly01, poly02)
## >>> print poly01xpoly02
## >>> poly01xpoly02 = convolve_poly(poly01, poly02)
## >>> print poly01xpoly02
## >>> poly01xpoly02 = mult_poly(poly01, poly02)
##
## Author: Vladimir Kulyukin
## bugs to vladimir dot kulyukin at gmail dot com
## ===================================================

import cmath
import math
import copy
import dft

def pad_with_zeros_until_required_length(a, n):
    padded_a = copy.copy(a)
    while True:
        padded_a.append(0)
        if dft.is_pow_of_2(len(padded_a)):
            return padded_a

## we assume that A and B are of the same degree bound. 
def convolve_poly(A, B, wf=dft.omega2, error=0):
    ## 1. ensure that coefficient arrays A and B are of the same length
    lenA, lenB = len(A), len(B)
    if lenA != lenB:
        raise Exception('Coefficient arrays must be of the same length')
    ## 2. pad A and B until their lengths are an integral power of 2
    padded_A = dft.pad_with_zeros(A)
    padded_B = dft.pad_with_zeros(B)
    ## 3. pad A and B more so that their lengths are 2n, where n
    ## is the length of padded A
    padded_A = pad_with_zeros_until_required_length(A, 2*len(padded_A))
    padded_B = pad_with_zeros_until_required_length(B, 2*len(padded_A))
    ## 4. compute dft of padded A and B
    fft_A = dft.recursive_fft(padded_A, wf=wf, error=error)
    fft_B = dft.recursive_fft(padded_B, wf=wf, error=error)
    ## 5. compute pointwise multiplication of A and B
    C = []
    for a, b in zip(fft_A, fft_B):
        C.append(a*b)
    ## 6. compute inverse dft and return the first 2*lenA-2 elements.
    return dft.recursive_inverse_fft(C, wf=wf, error=error)[0:2*lenA-1]

## we assume that A and B are of the same degree bound. 
def convolve_poly_split(A, B, wf=dft.omega2, error=0):
    lenA, lenB = len(A), len(B)
    if lenA != lenB:
        raise Exception('Coefficient arrays must be of the same length')
    ## 1. pad A and B with zeros until their lengths are an integral
    ## power of 2
    padded_A = dft.pad_with_zeros(A)
    padded_B = dft.pad_with_zeros(B)
    ## 2. pad A and B more so that their length is 2*n, where n is
    ## the length of padded_A.
    padded_A = pad_with_zeros_until_required_length(padded_A, 2*len(padded_A))
    padded_B = pad_with_zeros_until_required_length(padded_B, 2*len(padded_A))
    ## 3. compute dft of padded A and B
    fft_A = dft.recursive_fft(padded_A, wf=wf, error=error)
    fft_B = dft.recursive_fft(padded_B, wf=wf, error=error)
    ## 4. compute pointwise multiplication of A and B
    C = []
    for a, b in zip(fft_A, fft_B):
        C.append(a*b)
    ## 5. compute inverse dft of A*B and split the output into
    ## real and imaginary numbers.
    reals, imags = dft.recursive_inverse_fft_split(C, wf=wf, error=error)
    ## 6. the degree of A and B is lenA-1. the degree of A*B is
    ## 2*(lenA-1) = 2*lenA - 2.
    return reals[0:2*lenA-1], imags[0:2*lenA-1]

def mult_poly(A, B):
    lna, lnb = len(A), len(B)
    n = lna + lnb - 1
    rslt = [0 for i in range(n)]
    for i in range(0, lna):
        for j in range(0, lnb):
            rslt[i+j] += A[i]*B[j]
    return rslt
