## ======================================================================
## A Python implementation of the Levenshtein Edit Distance
## Named after Vladimir Levenshtein who discovered it in the 1960's.
## Author: Vladimir Kulyukin
## =======================================================================

## To run:
## >> edits = levenshtein_dp_01(source='abde', target='aabd')
## The above call returns a table of edits and associated costs.
## To recover the edit operations:
## >> recover_edits_dp_01('abde', 'aabd', edits, 4, 4)
## In the above call, the 1st argument is source, the 2nd - target, the
## 3rd is the number of rows in the edits table + 1, the 4th argument
## is the number of cols in the edits table + 1. It also takes option arguments
## that specify the costs of edit operations. See comments below.
## If interested in the cost only, run levenshtein_cost
## There is also a recursive implementation that is illustrative but less
## efficient than levenshtein_dp_01 that uses dynamic programming. Here
## are a few examples:
## >>> levenshtein_rec(source='ab', target='ab')
## (0, [('mat', 'a', 'a', 0), ('mat', 'b', 'b', 0)])
## >>> levenshtein_rec(source='abc', target='ab')
## (1, [('mat', 'a', 'a', 0), ('mat', 'b', 'b', 0), ('del', 'c', 1)])
## >>> levenshtein_rec('ab', 'abc')
## (1, [('mat', 'a', 'a', 0), ('mat', 'b', 'b', 0), ('ins', 'c', 1)])
## >>> levenshtein_rec(source='intention', target='execution')
## (5, [('sub', 'e', 'i', 1), ('sub', 'x', 'n', 1), ('sub', 'e', 't', 1), ('sub', 'c', 'e', 1),
##     ('sub', 'u', 'n', 1), ('mat', 't', 't', 0), ('mat', 'i', 'i', 0), ('mat', 'o', 'o', 0),
##     ('mat', 'n', 'n', 0)])
## levenshtein_rec(source='intention', target='execution', sub_cost=2)
## (8, [('del', 'i', 1), ('del', 'n', 1), ('del', 't', 1), ('mat', 'e', 'e', 0),
##     ('ins', 'x', 1), ('ins', 'e', 1), ('ins', 'c', 1), ('sub', 'u', 'n', 2),
##     ('mat', 't', 't', 0), ('mat', 'i', 'i', 0), ('mat', 'o', 'o', 0), ('mat', 'n', 'n', 0)])


import copy

def lev_ed_rec(source_str, target_str, edit_ops, edit_cost, ins_cost=1, del_cost=1, sub_cost=1):

    #print 'lev_ed_rec:', source_str, target_str, edit_ops
    target_len, source_len = len(target_str), len(source_str)

    edit_ops_copy = copy.deepcopy(edit_ops)
    
    if source_len == 0:
        #print 'source_len == 0:', edit_cost + target_len, edit_ops
        for c in target_str:
            edit_ops_copy.append(('ins', c, ins_cost))
        return edit_cost + target_len, edit_ops_copy
    if target_len == 0:
        #print 'target_len == 0:', edit_cost + source_len, edit_ops
        for c in source_str:
            edit_ops_copy.append(('del', c, del_cost))
        return edit_cost + source_len, edit_ops_copy

    if source_str[source_len-1] == target_str[target_len-1]:
        cost = 0
    else:
        cost = sub_cost

    #print 'Check 01'
    dc_cost, dc_edit_ops = lev_ed_rec(source_str[0:source_len-1], target_str,
                                      edit_ops, edit_cost,
                                      ins_cost=ins_cost, del_cost=del_cost, sub_cost=sub_cost)
    #print 'Check 02'
    ic_cost, ic_edit_ops = lev_ed_rec(source_str, target_str[0:target_len-1],
                                      edit_ops, edit_cost,
                                      ins_cost=ins_cost, del_cost=del_cost, sub_cost=sub_cost)
    #print 'Check 03'
    sc_cost, sc_edit_ops = lev_ed_rec(source_str[0:source_len-1], target_str[0:target_len-1],
                                      edit_ops, edit_cost,
                                      ins_cost=ins_cost, del_cost=del_cost, sub_cost=sub_cost)
    #print 'Check 04'

    min_cost = min(dc_cost, ic_cost, sc_cost)
    edit_ops_copy = None
    
    #print 'Check 05'
    
    if min_cost == dc_cost:
        #print 'min_cost == dc_cost ==', dc_cost
        edit_ops_copy = copy.deepcopy(dc_edit_ops)
        edit_ops_copy.append(('del', source_str[source_len-1], del_cost))
    elif min_cost == ic_cost:
        #print 'min_cost == ic_cost'
        edit_ops_copy = copy.deepcopy(ic_edit_ops)
        edit_ops_copy.append(('ins', target_str[target_len-1], ins_cost))
    elif min_cost == sc_cost:
        #print 'min_cost == sc_cost'
        edit_ops_copy = copy.deepcopy(sc_edit_ops)
        if cost == 0:
            edit_ops_copy.append(('mat', target_str[target_len-1], source_str[source_len-1], cost))
        else:
            edit_ops_copy.append(('sub', target_str[target_len-1], source_str[source_len-1], cost))
    else:
        #print 'min_cost is unique'
        edit_ops_copy = copy.deepcopy(edit_ops)

    #print 'Check 06'
    dc_edit_ops = None
    ic_edit_ops = None
    sc_edit_ops = None

    min_cost = sum((edit_op[-1] for edit_op in edit_ops_copy))
    
    #print 'Returning', min_cost, edit_ops_copy
    return min_cost, edit_ops_copy
    
## recursive implementation of the levenshtein distance.
def levenshtein_rec(source='', target='', ins_cost=1, del_cost=1, sub_cost=1):
    return lev_ed_rec(source, target, [], 0, ins_cost=ins_cost, del_cost=del_cost, sub_cost=sub_cost)

##       a  b  c
##   [0, 1, 2, 3]
## a [1, 0, 0, 0]
## b [2, 0, 0, 0]
##
##       a  b  c
## a [0, 1, 2, 3]
## b [1, 0, 1, 2]
## c [2, 2, 0, 1]
##
## levenshtein_dp_01(source='intention', target='execution')
##       e  x  e  c  u  t  i  o  n
##   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
## i [1, 1, 2, 3, 4, 5, 6, 6, 7, 8]
## n [2, 2, 2, 3, 4, 5, 6, 7, 7, 7]
## t [3, 3, 3, 3, 4, 5, 5, 6, 7, 8]
## e [4, 3, 4, 3, 4, 5, 6, 6, 7, 8]
## n [5, 5, 4, 5, 4, 5, 6, 7, 7, 7]
## t [6, 6, 6, 5, 6, 5, 5, 6, 7, 8]
## i [7, 7, 7, 7, 6, 7, 6, 5, 6, 7]
## o [8, 8, 8, 8, 8, 7, 8, 7, 5, 6]
## n [9, 9, 9, 9, 9, 9, 8, 9, 8, 5]
##
##
## levenshtein_dp_01(source='intention', target='execution', sub_cost=2)
##       e  x  e   c   u   t   i   o   n
##   [0, 1, 2, 3,  4,  5,  6,  7,  8,  9]
## i [1, 2, 3, 4,  5,  6,  7,  6,  7,  8]
## n [2, 3, 4, 5,  6,  7,  8,  7,  8,  7]
## t [3, 4, 5, 6,  7,  8,  7,  8,  9,  8]
## e [4, 3, 4, 5,  6,  7,  8,  9,  10, 9]
## n [5, 4, 5, 6,  7,  8,  9,  10, 11, 10]
## t [6, 5, 6, 7,  8,  9,  8,  9,  10, 11]
## i [7, 6, 7, 8,  9,  10, 9,  8,  9,  10]
## o [8, 7, 8, 9,  10, 11, 10, 9,  8,  9]
## n [9, 8, 9, 10, 11, 12, 11, 10, 9,  8]

## levenshtein distance computed with dynamic programming.
def levenshtein_dp_01(source='', target='', ins_cost=1, del_cost=1, sub_cost=1):
    m, n = len(source), len(target)
    edit_costs = [0 for i in xrange(0, m+1)]
    for r in xrange(0, m+1):
        edit_costs[r] = [0 for i in xrange(0, n+1)]
    
    ## source prefixes are transformed into empty target by deleting all characters
    for r in xrange(1, m+1):
        edit_costs[r][0] = r

    ## empty source string can be transformed into non-empty target by inserting
    ## a specific number of target characters
    for c in xrange(1, n+1):
        edit_costs[0][c] = c

    for c in xrange(1, n+1):
        for r in xrange(1, m+1):
            if source[r-1] == target[c-1]:
                edit_costs[r][c] = edit_costs[r-1][c-1]
            else:
                #if r == 1 and c == 1:
                #    print min(edit_costs[r-1][c-1] + del_cost, edit_costs[r][c-1] + ins_cost, edit_costs[r-1][c-1] + sub_cost)
                edit_costs[r][c] = min(edit_costs[r-1][c] + del_cost,
                                       edit_costs[r][c-1] + ins_cost,
                                       edit_costs[r-1][c-1] + sub_cost)

    ## print edit_costs
    
    return edit_costs

## recover_edits_dp_01 takes the table, edit_costs, computed by levenshtein_dp_01 and
## returns a sequence of moves that transforms the string source into the string target.
def recover_edits_dp_01(source, target, edit_costs, m, n, ins_cost=1, sub_cost=1, del_cost=1, mat_cost=0):
    r, c = m, n
    edits = []
    print 'r=', r, 'c=', c
    while r > 0 or c > 0:
        ## print 'insert cost is', ins_cost
        if r == 0:
            edits.insert(0, ('ins', target[c-1], ins_cost, c-1))
            c = c - 1
        elif c == 0:
            edits.insert(0, ('del', source[r-1], del_cost, r-1))
            r = r - 1
        elif source[r-1] == target[c-1]:
            edits.insert(0, ('mat', source[r-1], target[c-1], r-1, c-1, mat_cost))
            c = c - 1
            r = r - 1
        else:
            scost = edit_costs[r-1][c-1]
            dcost = edit_costs[r-1][c]
            icost = edit_costs[r][c-1]
            min_cost = min(scost, dcost, icost)
            if min_cost == scost:
                edits.insert(0, ('sub', target[c-1], source[r-1], r-1, c-1, sub_cost))
                r = r - 1
                c = c - 1
            elif min_cost == dcost:
                edits.insert(0, ('del', source[r-1], r-1, del_cost))
                r = r - 1
            elif min_cost == icost:
                ## print 'insertion cost is', ins_cost
                edits.insert(0, ('ins', target[c-1], c-1, ins_cost))
                c = c - 1
    return edits

## levenshtein_dp_2r computes the edit distance using only 2 rows.
## c iterates over target
## r iterates over source
def levenshtein_dp_2r(source='', target='', ins_cost=1, del_cost=1, sub_cost=1):
    m, n = len(source), len(target)
    prev_edit_costs = [0 for i in xrange(0, n+1)]
    curr_edit_costs = [0 for i in xrange(0, n+1)]
    
    ## empty source string can be transformed into non-empty target by inserting
    ## a specific number of target characters
    for c in xrange(1, n+1):
        prev_edit_costs[c] = c

    ## iterate over source
    for r in xrange(1, m+1):
        for c in xrange(0, n+1):
            if c == 0:
                ## delete the first r characters in the source
                curr_edit_costs[c] = r
            elif source[r-1] == target[c-1]:
                curr_edit_costs[c] = prev_edit_costs[c-1]
            else:
                curr_edit_costs[c] = min(prev_edit_costs[c] + del_cost,
                                         curr_edit_costs[c-1] + ins_cost,
                                         prev_edit_costs[c-1] + sub_cost)
        ## copy the current row to the previous row
        for c in xrange(0, n+1):
            prev_edit_costs[c] = curr_edit_costs[c]

    ## if target's length is 0, then prev_edit_costs is an array with
    ## 1 element.
    return prev_edit_costs

## return just the cost of transforming source to target
def levenshtein_cost(source='', target='', ins_cost=1, del_cost=1, sub_cost=1):
    edits = levenshtein_dp_2r(source=source, target=target, ins_cost=ins_cost,
                              sub_cost=sub_cost)
    return edits[len(edits)-1]
        
            
    

    
    
