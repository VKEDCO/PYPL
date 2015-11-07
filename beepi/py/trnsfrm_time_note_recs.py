#!/usr/bin/python

###############################
# @author: vladimir kulyukin
###############################
import re
import sys

timestamped_notes_pat = r'^(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})\s+(\d{4,6})\s+(.+)$'

def display_time_note_record_on_one_line(rec_match):
    year, month, day, hour,  mins, secs, freq, notes = rec_match.groups()
    sys.stdout.write(str(year) + "\t" + str(month) + "\t" + str(day) + "\t" +\
                     str(hour) + "\t" + str(mins) + "\t" + str(mins) + "\t" +\
                     str(freq) + "\t" + str(secs) + "\t" + str(freq) + "\t" +\
                     str(notes) + "\n")

def get_timestamped_notes_record(line):
    match = re.match(timestamped_notes_pat, line)
    if match != None:
        return match
    else:
        return None

for rec_match in filter(lambda rm: rm != None,
                        [get_timestamped_notes_record(line)
                         for line in sys.stdin.readlines()]):
    display_time_note_record_on_one_line(rec_match)
