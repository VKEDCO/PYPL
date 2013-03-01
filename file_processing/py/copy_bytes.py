#!/usr/bin/python

#################################################
## copy file byte by byte from infp to outfp
##
## to run on linux:
## >>> ./copy_bytes.py input_file output_file
##
## unix2dos or dos2unix to deal with ^M.
##
## bugs to vladimir dot kulyukin at gmail dot com
#################################################

import sys

def copy_bytes(in_fp, out_fp):
    with open(in_fp, 'rb') as inbytes:
        with open(out_fp, 'wb') as outbytes:
            for byte in inbytes:
                outbytes.write(byte)
            outbytes.flush()

if __name__ == '__main__':
    copy_bytes(sys.argv[1], sys.argv[2])

            



