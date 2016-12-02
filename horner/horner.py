## 1. Horner's Rule for Evaluating Polynomials
## 2. Synthetic Division of Polynomials with Horner's Rule
## 3. Two-part screencast is available: part 01  and part 02
## Horner's Rule's pseudocode:
##
## pv = coeffs[0]
## for i from 1 upto n
##   pv = x0 * pv + coeffs[i]
## return pv

def horner_poly(coeffs, x0):
    pv = coeffs[0]
    for c in coeffs[1:]:
        pv = x0 * pv + c
    return pv


## 4x^3 - 2x^2 + 5x - 2, at x0 = 2
## 4*8 - 8 + 10 - 2 = 32
def test_00():
    coeffs = [4,-2,5,-2]
    x0 = 2
    pv = horner_poly(coeffs, 2)
    print pv

# test_00()

def synthetic_poly_div(coeffs, x0):
    pv = coeffs[0]
    div_coeffs = [pv]
    for c in coeffs[1:]:
        pv = x0 * pv + c
        div_coeffs.append(pv)
    return div_coeffs

## (4x^3 - 2x^2 + 5x - 2)/(x-2) =
## 4x^2 + 6x + 17 + 32/(x-2)

def test_01():
    coeffs = [4,-2,5,-2]
    x0 = 2
    div_coeffs = synthetic_poly_div(coeffs, x0)
    print div_coeffs

## test_01()
