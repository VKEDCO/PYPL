## ===================================================
## A recursive implementation of discrete fourier
## transform (DFT) and inverse discrete fourier
## transform as outlined in Ch. 32 in "Introduction
## to Algorithms" by Cormen, Leiserson, and Rivest.
##
## sample run:
## >>> a = [random.randint(0, 100) for i in range(8)]
## >>> r = recursive_fft(a, 0.0001)
## >>> a
## [47, 23, 69, 71, 62, 72, 70, 76]
## >>> r
## [490, (-46.112698372208094-39.18376618407356j), (-30.00000000000001-52j),
## (16.11269837220808-37.183766184073576j), 6,
## (16.112698372208094+37.18376618407356j), (-29.99999999999999+52j),
## (-46.11269837220808+39.183766184073576j)]
## >>> rr = recursive_inverse_fft(r, 0.0001)
## >>> rr
## [(47+0j), (23+4.440892098500626e-15j), (69-1.1102230246251565e-16j), (71-3.3306690738754696e-15j),
## (62+0j),
## (72+8.881784197001252e-16j), (70+1.1102230246251565e-16j), (76-1.9984014443252818e-15j)]
##
## the second argument to recursive_fft and recursive_inverse_fft is an error value.
## it can be set to 0 or some small number.
##
## Author: Vladimir Kulyukin
## bugs to vladimir dot kulyukin at gmail dot com
## ===================================================

import cmath
import math
import copy

## check if n is a power of 2.
def is_pow_of_2(n):
    if n < 1:
        return False
    else:
        p_of_2 = math.log(n, 2)
        return abs(p_of_2 - int(p_of_2)) == 0

## formula for the n-th complex root of unity on p. 784 of Cormen's Algorithms book
## the only addition is the error argument: when the real or imaginary parts of a complex
## number is less than error, it is set to 0.
def omega_with_error(k, n, error=0):
    if n <= 0:
        return None
    else:
        x = cmath.exp((2 * cmath.pi * 1j * k)/n)
        xr = x.real
        xi = x.imag
        if abs(xr) < error: xr = 0
        if abs(xi) < error: xi = 0
        return complex(xr, xi)

## another commonly used version of omega where there is -1 in the exponent.
## for example, this is the version used on
## http://scistatcalc.blogspot.com/2013/12/fft-calculator.html.
def omega2_with_error(k, n, error=0):
    if n <= 0:
        return None
    else:
        x = cmath.exp(-(2 * cmath.pi * 1j * k)/n)
        xr = x.real
        xi = x.imag
        if abs(xr) < error: xr = 0
        if abs(xi) < error: xi = 0
        return complex(xr, xi)

## same as above but error is ignored.
def omega(k, n, error):
    if n <= 0:
        return None
    else:
        return cmath.exp((2 * cmath.pi * 1j * k)/n)

## same as above but error is ignored.
def omega2(k, n, error):
    if n <= 0:
        return None
    else:
        return cmath.exp(-(2 * cmath.pi * 1j * k)/n)

## This is an implementation of FFT on p. 788 in Cormen's book.
## This runs in O(nlogn). If the length is not a power of 2,
## the array is padded with 0 until its length is a power of 2.
def recursive_fft(A, wf=omega, error=0):
    n = len(A)
    if not is_pow_of_2(n):
        return recursive_fft_aux(pad_with_zeros(A), wf, error)
    else:
        return recursive_fft_aux(A, wf, error)

def recursive_fft_aux(A, wf, error):
    n = len(A)
    if n == 1: return A
    w_n = wf(1, n, error)
    w = 1
    A_0 = get_even_elements(A)
    A_1 = get_odd_elements(A)
    Y_0 = recursive_fft_aux(A_0, wf, error)
    Y_1 = recursive_fft_aux(A_1, wf, error)
    Y = Y_0 + Y_1
    delta = int(n/2)
    ##print('A_0:' + str(A_0))
    ##print('A_1:' + str(A_1))
    ##print('Y: ' + str(Y))
    ##print('delta: ' + str(delta))
    for k in range(0, delta):
        Y[k] = Y_0[k] + w * Y_1[k]
        Y[k + delta] = Y_0[k] - w * Y_1[k]
        w = w * w_n
    return Y

def recursive_fft_split(A, wf=omega, error=0):
    real = []
    imag = []
    for x in recursive_fft(A, wf=wf, error=error):
        real.append(x.real)
        imag.append(x.imag)
    return real, imag

## take Y obtained from recursive_fft above and
## restore the original array.
def recursive_inverse_fft(Y, wf=omega, error=0):
    n = len(Y)
    if not is_pow_of_2(n):
        return [x/n for x in recursive_inverse_fft_aux(pad_with_zeros(Y), wf, error)]
    else:
        return [x/n for x in recursive_inverse_fft_aux(Y, wf, error)]

def recursive_inverse_fft_aux(Y, wf, error):
    n = len(Y)
    if n == 1: return Y
    w_n = wf(-1, n, error)
    w = 1
    Y_0 = get_even_elements(Y)
    Y_1 = get_odd_elements(Y)
    A_0 = recursive_inverse_fft_aux(Y_0, wf, error)
    A_1 = recursive_inverse_fft_aux(Y_1, wf, error)
    A = A_0 + A_1
    delta = int(n/2)
    for k in range(0, delta):
        A[k] = A_0[k] + w * A_1[k]
        A[k + delta] = A_0[k] - w * A_1[k]
        w = w * w_n
    return A

def recursive_inverse_fft_split(Y, wf=omega, error=0):
    real = []
    imag = []
    for x in recursive_inverse_fft(Y, wf=wf, error=error):
        real.append(x.real)
        imag.append(x.imag)
    return real, imag

## slower version of DFT in O(n^2).
def dft(a, wf=omega, error=0):
    rslt = []
    n = len(a)
    for k in range(n):
        y_k = 0
        for j in range(n):
            y_k += a[j]*wf(k*j, n, error)
        rslt.append(y_k)
    return rslt

def get_even_elements(a):
    n = len(a)
    rslt = []
    for i in range(0, n, 2):
        rslt.append(a[i])
    return rslt

def get_odd_elements(a):
    n = len(a)
    rslt = []
    for i in range(1, n, 2):
        rslt.append(a[i])
    return rslt

def pad_with_zeros(a):
    ln = len(a)
    padded_a = copy.copy(a)
    if ln > 2 and is_pow_of_2(ln):
        return padded_a
    while True:
        padded_a.append(0)
        if is_pow_of_2(len(padded_a)):
            return padded_a

