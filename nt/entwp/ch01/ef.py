#!/usr/bin/python

'''
================================
module: ef.py
author: vladimir kulyukin

> f = fraction(2, 3)
> ufs = ef(f)
> ufset_to_str(r)
'1/3+1/4+1/12'
> str(sum_ufset(ufs))
'2/3'
================================
'''

from factorization import gcd, lcm
from fraction import fraction

def ef(f):
    assert f.is_proper()
    ufset = {}
    return efaux(f, ufset)

def efaux(uf, uf_set):
    f, uf = split_frac(uf)
    if f.is_unit():
        return add(f, add(uf, uf_set))
    else:
        return efaux(f, add(uf, uf_set))

def add(uf, uf_set):
    fa = find_partner_for(uf, uf_set)
    if fa is not None:
        uf2, a = fa
        remove_from_uf_set(uf2, uf_set)
        add_to_uf_set(a, uf_set)
        return uf_set
    elif not is_in_uf_set(uf, uf_set):
        add_to_uf_set(uf, uf_set)
        return uf_set
    else:
        suf1, suf2 = fraction.unit_split_frac(uf)
        #print suf1, suf2
        return add(suf1, add(suf2, uf_set))

def find_partner_for(uf, ufset):
    for _, f in ufset.items():
        a = fraction.add(uf, f)
        if a.is_unit() and not is_in_uf_set(a, ufset):
            return f, a
    return None

def split_frac(frac):
    assert fraction.is_proper(frac) and not frac.is_unit()
    n, d = frac.get_numerator(), frac.get_denominator()
    return fraction.reduce_to_lowest_terms(fraction(n-1, d)), fraction(1, d)

def add_to_uf_set(frac, frac_set):
    assert frac.is_unit()
    frac_set[frac.get_denominator()] = frac

def remove_from_uf_set(frac, frac_set):
    assert frac.is_unit()
    assert frac_set.has_key(frac.get_denominator())
    frac_set.pop(frac.get_denominator(), None)
         
def is_in_uf_set(frac, fset):
    assert frac.is_proper()
    return fset.has_key(frac.get_denominator())

def ufset_to_list(ufset):
    rslt = []
    for _, f in ufset.items():
        rslt.append(f)
    return rslt

def sum_ufset(ufset):
    return fraction.add_fracs(ufset_to_list(ufset))

def ufset_to_str(ufset):
    ul = ufset_to_list(ufset)
    ul.sort(key = lambda f: f.get_denominator())
    rslt = ''
    for f in ul[:-1]:
        rslt += str(f) + '+'
    rslt += str(ul[-1])
    return rslt
