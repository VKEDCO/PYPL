#!/usr/bin/perl

###########################################################
## demonstrates list, scalar numeric and scalar strings
## contexts.
##
## bugs to vladimir dot kulyukin at gmail dot com
###########################################################

use warnings;
use strict;

my $str = "5";
my $num = 5.7;
print "\n\n" . '$num' . '=' . $num . ' and ' . '$str' . ' = ' . 
  '\'' . $str . '\'' . "\n\n";

## add a number to a string.
## $str is converted to a number in the numeric
## context.
my $sum = $num + $str;
print 'Adding $num and $str in numeric context: ' . $sum . "\n\n";

## $num is converted to a string in the
## string context which determined by the . operator
## that works on strings
my $concat = $num . $str;
## $concat = '5.5' . "5" = '5.55'
print 'Concatenating $num and $str in string context: ' . $concat . "\n\n";

## use of $undef in a numeric context which
## is determined by the + operator.
## $undef evaluates to 0 in a numeric context.
my $x; ## $x is not defined, becomes $undef and defaults to 0
## since use strict; is in place, a runtime warning is issued that $x is not initialized
my $undef_num_add = $num + $x;
## $under_num_add = 5.5 + 0 = 5.5
print 'Adding $num and $x in numeric context: ' . $undef_num_add . "\n\n";

## use of $undef in another numeric context.
my $undef_num_mult = $num * $x; ## $undef defaults to 0
print 'Multiplying $num and $x in numeric context: '.$undef_num_mult. "\n\n";

## use of $undef in a string context which is
## determined by the . operator that works on strings
## $undef evaluates to '' in the string context.
## since use strict; is in place, a runtime warning is issued that $x is not initialized
my $undef_str_add = $str . $x;
## $under_str_add = "5" . '' = '5'
print 'Concatenating $num and $x: ' . $undef_str_add . "\n";


my @lst_01 = (1, 2, 3, 4);
my $len = length(@lst_01); ## this is incorrect: the argument
                           ## to length must be a scalar.
print $len, "\n"; ## $len is not the length of @lst_01.

my $lst_len = @lst_01; 	## numeric context in which @lst_01 is evaluated
			## as the length of @lst_01.

print $lst_len, "\n";  	## $lst_len is @lst_01's length, i.e., 4

my @y = @lst_01; 	## this is a list context which is determined
			## by assigning to an array variable @y.
print "@y\n";





