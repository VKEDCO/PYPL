use strict;
use warnings;

## Your thinking is like a camel driver,
## and you are the camel:
## it drives you in every direction under its bitter control.
## -- Rumi

################################################
#
# map EXPRESSION, LIST
# where EXPRESSION is an expression that applies
# to $_ and, unlike in grep, returns a result
# the returned result is placed in LIST.
#
# author: vladimir kulyukin
#################################################

my @numbers = (1..10);

## mapping EXPRESSION
my @sums = map $_ + 5, @numbers;
print "@sums\n";

sub poly {
  my $x = $_[0];
  return $x**2 + 5*$x - 10;
}

## mapping a soubroutine
my @poly_nums = map poly($_), @numbers;
print "@poly_nums\n";

## mapping a code block
my @words = qw(one two three four five);
my @word_lengths = map {
  my $w = $_;
  my $ln = length($w);
  print "length of \'$w\' is $ln\n";
  $ln;
} @words;
print "@word_lengths\n";

my @words_and_lengths = map {
  my $w = $_;
  my $ln = length($w);
  my @lst = ($w, $ln);
  \@lst;
} @words;


print "@$_\n" foreach(@words_and_lengths);

foreach(@words_and_lengths) {
  my @lst = @$_;
  print "length of \'$lst[0]\' \t = \t $lst[1]\n";
}




