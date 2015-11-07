#!/usr/bin/python

#####################################
# @author: vladimir kulyukin
#####################################
import sys
import re

note_freq_toops = [ ]
for line in sys.stdin.readlines():
    match = re.match(r'\S+', line)
    if match != None:
        note_freq_toop = re.split(r'\t', line)
        note_freq_toops.append(note_freq_toop)

note_freq_toops.sort(key=lambda toop: int(toop[1]), reverse=True)
for note, freq in note_freq_toops:
    sys.stdout.write(note+"\t"+str(freq))
