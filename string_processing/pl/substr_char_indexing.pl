#!/usr/bin/perl

########################################################
## shows how substr() can be used to index individual
## string characters.
## bugs to vladimir dot kulyukin at gmail dot com
########################################################
use strict;
use warnings;

## define two string scalars
my $str_01 = 'abc';
my $str_02 = 'the sail just needs to open and the world is full of beauty';

## retrieve a character at position $pos in string $str
## get_char_at_pos($str, $pos)
sub get_char_at_pos {
    return substr($_[0], $_[1], 1);
}

## print string characters by accessing them with substr()
## print_char($str).
sub print_chars {	
    foreach (0 .. length($_[0])-1) {
	print substr($_[0], $_, 1);
    }
    print "\n";
}

## prints str_01 followed by \n
print_chars($str_01);
## prints str_02 followed by \n
print_chars($str_02);

## 1. 'a' is printed
print get_char_at_pos($str_01, 0), "\n";
## 2. 'b' is printed
print get_char_at_pos($str_01, 1), "\n";
## 3. 'c' is printed
print get_char_at_pos($str_01, 2), "\n";
## nothing is printed
print get_char_at_pos($str_01, 3), "\n";
## 4. 'c' is printed
print get_char_at_pos($str_01, -1), "\n";
## 5. 'b' is printed
print get_char_at_pos($str_01, -2), "\n";
## 6. 'a' is printed
print get_char_at_pos($str_01, -3), "\n";
## 7. nothing is printed
print get_char_at_pos($str_01, -4), "\n";
