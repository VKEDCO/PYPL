#!/usr/bin/python

#################################################
## mapping functions over strings
## author: vladimir kulyukin
#################################################

## takes a string and returns the character code
## of each character.
def chars_to_codes(str):
  return map(ord, str)

## convert a string to a list of character codes
## and print the char -> code map.
def test_chars_to_codes():
  print 'CHARS -> CODES'
  for code in chars_to_codes('the sail opens'):
    print chr(code) + ' -> ' + str(code)

## takes a string and returns the character code
## of each character
def codes_to_chars(codes):
  return map(chr, codes)

## convert a string to a list of character codes;
## convert the list of character codes to a list of characters;
## print the code -> char map.
def test_codes_to_chars():
  print 'CODES -> CHARS'
  for c in codes_to_chars(chars_to_codes('the sail opens')):
    print str(ord(c)) + ' -> ' + c

test_chars_to_codes()
test_codes_to_chars()
