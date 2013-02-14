#!/usr/bin/python

#################################################
## Three finite-state machines for the 
## following languages:
## - L1 = {a};
## - L2 = {{(ab)^n | n >= 1}
## - L3 = {a^n | n is even} U {b^n | n is odd}
## 
## bugs to vladimir dot kulyukin at gmail dot com
##################################################

import re

test_strings = [
    '', 'ab', 'abab', 
    'ababab', 'abbb', 
    'aaaa', 'aaa', 'aaaaaa', 
    'b', 'bbb', 'bbbbb', 
    'abbaabba', 'abababababababab', 
    'aa', 'bbbb'
    ]

## fsa_01 accepts {a}.
tran_tbl_01 = {}
tran_tbl_01['a'] = {1 : [2]}
fsa_01 = (1, [2], tran_tbl_01)

## fsa_02 accepts {(ab)^n | n >= 1} or (ab)+.
tran_tbl_02 = {}
tran_tbl_02['a'] = {1 : [2], 2 : []}
tran_tbl_02['b'] = {1 : [], 2 : [3]}
tran_tbl_02['']   = {3 : [1]}
fsa_02 = (1, [3], tran_tbl_02)

## fsa_03 accepts {a^n | n is even} U {b^n | n is odd}
tran_tbl_03 = {}
tran_tbl_03['']   = {1 : [2, 4]}
tran_tbl_03['a'] = {2 : [3], 3 : [2]}
tran_tbl_03['b'] = {4 : [5], 5 : [4]}
fsa_03 = (1, [2, 5], tran_tbl_03)

def get_start_state(fsa): return fsa[0]
def get_fin_states(fsa): return fsa[1]
def get_tran_table(fsa): return fsa[2]

def tran_table_lookup(sym, state, tran_tbl):
    if tran_tbl.has_key(sym):
        return tran_tbl.get(sym, []).get(state, [])
    else:
        return []

def tran_table_epsilon_lookup(state, tran_tbl):
    return tran_table_lookup('', state, tran_tbl)

def match_fsa(fsa, txt):
    return match_fsa_aux(txt, 0, len(txt), get_start_state(fsa),
                         get_fin_states(fsa), get_tran_table(fsa))

def match_fsa_aux(txt, i, n, cur_state, fin_states, tran_tbl):
    print i, cur_state
    if i == n:
        if cur_state in fin_states:
            return True
        else:
            next_epsilon_states = tran_table_epsilon_lookup(cur_state, tran_tbl)
            for nes in next_epsilon_states:
                if nes in fin_states:
                    return True
            return False
    else:
        next_states = tran_table_lookup(txt[i], cur_state, tran_tbl)
        next_epsilon_states = tran_table_epsilon_lookup(cur_state, tran_tbl)
        if next_states == [] and next_epsilon_states == []:
            return False
        else:
            for ns in next_states:
                print 'ns=', ns
                rslt = match_fsa_aux(txt, i+1, n, ns, fin_states, tran_tbl)
                if rslt == True:
                    return True
            for nes in next_epsilon_states:
                print 'nes=', nes
                rslt = match_fsa_aux(txt, i, n, nes, fin_states, tran_tbl)
                if rslt == True:
                    return True
            return False

print match_fsa(fsa_01, 'ab')

def match_regexp(regexp, txt):
    pat = re.compile(regexp)
    if pat.match(txt):
        return True
    else:
        return False

def test_fsa(fsa, string_list):
    for s in string_list:
        if match_fsa(fsa, s):
            print s + " -- yes"
        else:
            print s + " -- no"

print 'Testing FSA 01'
test_fsa(fsa_01, test_strings)
print

print 'Testing FSA 02'
test_fsa(fsa_02, test_strings)
print

print 'Testing FSA 03'
test_fsa(fsa_03, test_strings)
print

