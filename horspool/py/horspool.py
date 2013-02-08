##################################################
## PY implementation of Horspool's algorithm
## 
## sample use:
## 
## text = 'abe abc efg';
## pat  = 'abc';
## shift_table = build_shift_table(pat);
## match_pos   = horspool(pat, text, shift_table);
## print $match_pos;
## 
## bugs to vladimir dot kulyukin at gmail dot com
###################################################

import string

rumi_poem = \
'\
Late, by Myself\n\
Late, by myself, in the boat of myself,\n\
no light and no land anywhere,\n\
cloudcover thick. I try to stay\n\
just above the surface,\n\
yet I\'m already under\n\
and living with the ocean\n\
\n\
Mewlana Jalaluddin Rumi\n\
'

def build_shift_table(pattern):
    shift_table = {}
    plen = len(pattern)
    for i in xrange(0, plen-1):
        shift_table[ord(pattern[i])] = plen-1-i
    return shift_table

def lookup_shift_value(c, pat_len, shift_table):
    if shift_table.has_key(ord(c)):
        return shift_table[ord(c)]
    else:
        return pat_len

def horspool(pat, text, shift_table):
    pat_len, txt_len = len(pat), len(text)
    ## pat_re_pos - pattern's right end position when aligned with text;
    ## it is used in index into text, not pat.
    pat_re_pos = pat_len - 1
    ## matched_char_count - count of how many characters in pat
    ## has been matched against corresponding
    ## characters in text.
    matched_char_count = 0

    ## keep going so long as pat_re_pos does not
    ## go over the right bound of text.
    while pat_re_pos <= txt_len-1:
        matched_char_count = 0

        ## keep incrementing matched_char_count so long as
        ## 1) matched_char_count <= pat_len-1 AND
        ## 2) the current character in pat (at position pat_len - matched_char_count - 1)
        ##     is the same as the corresponding character in text 
        ##    (at position pat_re_pos - matched_char_count)
        while matched_char_count <= pat_len-1 and\
                  pat[pat_len-matched_char_count-1] == text[pat_re_pos-matched_char_count]:
            matched_char_count += 1

        ## if the number of matched characters is the same
        ## as the pattern's length, return the position in text
        ## at which the first character of the matched pattern pat
        ## aligns with text
        if matched_char_count == pat_len:
            return pat_re_pos-pat_len+1
        else:
            ## lookup the shift value of the mismatched character in $text
            ## and shift $pat_re_pos right
            pat_re_pos += lookup_shift_value(text[pat_re_pos], pat_len, shift_table)
    return -1


################# Tests #######################

def generic_horspool_test(pat, text):
    shift_table = build_shift_table(pat)
    match_pos = horspool(pat, text, shift_table)
    print "match_start\t==\t", match_pos
    print "match_end\t==\t", match_pos + len(pat) - 1
    print "matched text\t==\t", repr(text[match_pos: match_pos+len(pat)])
    print

## Output
## match_start	==	4
## match_end	==	6
## matched text	==	'abc'
generic_horspool_test('abc', 'abe abc efg')

## Output
## match_start	==	8
## match_end	==	10
## matched text	==	'a c'
generic_horspool_test('a c', 'abc efg a c klm!')

## Output
## match_start	==	185
## match_end	==	189
## matched text	==	'ocean'
generic_horspool_test('ocean', rumi_poem)

## Output
## match_start	==	185
## match_end	==	190
## matched text	==	'ocean\n'
generic_horspool_test('ocean\n', rumi_poem)

## Output
## match_start	==	147
## match_end	==	157
## matched text	==	"I'm already"
generic_horspool_test('I\'m already', rumi_poem)

## Output
## match_start	==	147
## match_end	==	190
## matched text	==	"I'm already under\nand living with the ocean\n"
generic_horspool_test('I\'m already under\n\
and living with the ocean\n', rumi_poem);



