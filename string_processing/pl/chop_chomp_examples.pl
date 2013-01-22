#!/usr/bin/perl

#########################################################
## examples of chop() and chomp()
##
## bugs to vladimir dot kulyukin at gmail dot com
#########################################################
use strict;
use warnings;

my @lst_01 = qw(the sail just needs to open);
print "@lst_01\n";

## chop() chops off the last character of
## each string in the list of strings given
## to it.
chop(@lst_01);
## this prints 'th sai jus need t ope'
print "@lst_01\n";

## this illustrates that chop executes in the
## scalar string context: $x is converted to '12'
## and then '2' is chopped off.
my $x = 12;
chop($x);
print "$x\n";

print "\$/ is the input record separator whose ASCII value is " . ord($/) . "\n";
print 'ASCII value of \n is ' . ord("\n") . "\n";

my @lst_02 = qw(the sail just needs to open);
print "@lst_02\n";
## does not remove any characters
chomp(@lst_02);
print "@lst_02\n";

my @list_03 = ("the\n", "sail\n", "just\n", "needs\n", "to\n", "open\n");
print "@list_03\n";
chomp(@list_03); ## chomp does remove each "\n"
print "@list_03\n";

## chomp() is frequently used to chomp the newline off the user input.
## this asks the user to enter two scalars, chomps off the newline
## and returns their sum in the scalar numeric context.
print 'Input a number: ';
my $x1 = <STDIN>;
chomp($x1);
print 'Input a number: ';
my $x2 = <STDIN>;
chomp($x2);
print $x1 + $x2, "\n";





