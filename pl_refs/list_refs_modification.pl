#!/usr/bin/perl

use strict;
use warnings;

## shows that lists are passed by reference
## to subroutines and can be destructively
## modified; also shows how argument lists
## can be copied, modified, and returned.
##
## bugs to vladimir dot kulyukin at gmail dot com.

my @list = (1, 2, 3, 4);
print "@list\n"; ## prints 1 2 3 4

## the original lists are destructively modified.
## each number is squared.
sub list_squares_01 {
  $_ **= 2 foreach(@_);
}

list_squares_01(@list);
print "@list\n"; ## prints 1 4 9 16

## @lst scalars are again destructively modified
## by computing their square roots. @lst is set
## back to is original contents (1, 2, 3, 4)
sub list_square_roots_01 {
  $_ **= .5 foreach(@_);
}
list_square_roots_01(@list);
print "@list\n"; ## prints 1 2 3 4

## copying argument lists and returning new lists
sub copy_list_squares {
  ## @copy_list is a copy of @_
  my @copy_list = @_; 
  ## @copy_list is destructively modified
  $_ **= 2 foreach(@copy_list);
  ## @copy_list is returned.
  return @copy_list;
}

print "copy_list_squares() is called\n";
my @squares = copy_list_squares(@list);
print "\@list = @list\n"; ## @list is still (1, 2, 3, 4)
print "\@squares = @squares\n"; ## @squares is (1, 4, 9, 16)



