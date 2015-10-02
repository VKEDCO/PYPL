#!/usr/bin/python

####################################
# Py joins on sequences
# author: vladimir kulyukin
####################################

seq1 = ['your', 'thinking', 'is', 'like', 'a', 'camel', 'driver']
seq2 = ['a', 'b', 'c', 'd', 'e', 'f']

def join_seq(separator, seq):
  return separator.join(seq)

def test_join_seq(seq):
  print join_seq('*',    seq)
  print join_seq(' ** ', seq)
  print join_seq('//',   seq)

test_join_seq(seq1)
test_join_seq(seq2)
