#!/usr/bin/python

import os, sys

if __name__ == '__main__':
    directory = sys.argv[1]
    end_mask = sys.argv[2]
    files = filter(lambda fn: fn.endswith(end_mask), os.listdir(directory)); 
    for f in files: print f


