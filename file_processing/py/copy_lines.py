#!/usr/bin/python

#################################################
## copy ASCII file infp to outfp line by line
##
## to run on linux:
## >>> ./copy_lines.py input_file output_file
##
## unix2dos or dos2unix to deal with ^M.
##
## bugs to vladimir dot kulyukin at gmail dot com
#################################################


import sys

def copy_lines(infp, outfp):
    with open(infp, 'r') as infile:
        with open(outfp, 'w') as outfile:
            for line in infile:
                outfile.write(line)
            outfile.flush()

if __name__ == '__main__':
    copy_lines(sys.argv[1], sys.argv[2])
    





