#!/usr/bin/perl

###############################################
# mapping over strings one character at a time
# author: vladimir kulyukin
###############################################

use strict;
use warnings;
use 5.10.0;

## takes a string and returns the character code
## of each character.
sub chars_to_codes {
    my $str = $_[0];
    my @codes = map ord($_), split('', $str);
    return \@codes;
}

## convert a string to a list of character codes
## and print the char -> code map.
sub test_chars_to_codes {
    my $str = 'the sail opens';
    say 'CHARS -> CODES';
    print chr($_) . ' -> ' . $_ . "\n" foreach(@{chars_to_codes($str)});
}

## takes a string and returns the character code
## of each character
sub codes_to_chars {
    my @chars = map chr($_), @_;
    return \@chars;
}

## convert a string to a list of character codes;
## convert the list of character codes to a list of characters;
## print the code -> char map.
sub test_codes_to_chars {
    my $str = 'the sail opens';
    my @codes = @{chars_to_codes($str)};
    my @chars = @{codes_to_chars(@codes)};
    say 'CODES -> CHARS';
    print ord($_) . ' -> ' . $_ . "\n" foreach(@chars);
}

test_chars_to_codes();
test_codes_to_chars();
