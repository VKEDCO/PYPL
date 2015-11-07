#!/usr/bin/python

##############################
# @author: vladimir kulyukin
##############################
import re
import sys

def display_note_freqs_table(tbl):
    for note, freq in tbl.items():
        sys.stdout.write(note+"\t"+str(freq)+"\n")

note_freqs_table = { }
for line in sys.stdin.readlines():
    match = re.match(r'\S+', line)
    if match != None:
        record_splits = re.split(r'\t', line)
        notes = filter(lambda s: re.match(r'\S+', s) != None,
                       re.split(r'\s', record_splits[9]))
        for note in notes:
            if note_freqs_table.has_key(note):
                note_freqs_table[note] = note_freqs_table[note] + 1
            else:
                note_freqs_table[note] = 1

display_note_freqs_table(note_freqs_table)
