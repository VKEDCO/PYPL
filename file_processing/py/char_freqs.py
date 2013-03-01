#!/usr/bin/python

#################################################
## compute character frequencies ASCII input file 
## specified by infp and place them in a 
## dictionary.
##
## to run on linux:
## >>> ./char_freqs.py input_file_path
##
## unix2dos or dos2unix to deal with ^M.
##
## bugs to vladimir dot kulyukin at gmail dot com
#################################################

import sys

def build_char_freq_dict(infp, d, line_processor):
    with open(infp, 'r') as infile:
        for line in infile:
            line_processor(line, d)

def line_char_freqs(line, d):
    for c in line:
        if d.has_key(c):
            d[c] += 1
        else:
            d[c] = 1

if __name__ == '__main__':
    char_freq_dict = {}
    build_char_freq_dict(sys.argv[1], char_freq_dict, line_char_freqs)
    for c, f in char_freq_dict.iteritems():
        print c, '->', f
