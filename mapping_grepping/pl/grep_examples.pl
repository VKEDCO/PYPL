use strict;
use warnings;

## Your thinking is like a camel driver,
## and you are the camel:
## it drives you in every direction under its bitter control.
## -- Rumi

#########################################################
##
## grep syntax is grep PREDICATE, LIST, where
## PREDICATE is an expression, a code block or subroutine 
## that puts each value in LIST in $_ and returns 
## true (in Perl, it is anything but 0) or false.
## if true is returned, the value in $_ is placed
## into the output list.
##
## In a list context, grep returns a list of
## selected elements in LIST for which PREDICATE
## is true.
##
## In a scalar context, grep returns the number of
## elements in LIST for which PREDICATE is true.
##
## author: vladimir kulyukin
###########################################################

my @numbers = (1..11);

## This call to grep places each value in @list inside $_
## and then checks if $_ % 2 == 0. If this equality is true, 
## then the current value of $_ is placed into the output list. 
## This call to grep is made in a list context, so @evens 
## becomes bound is the list of even numbers in @numbers.
my @evens = grep $_ % 2 == 0, @numbers;
## @evens == (2, 4, 6, 8, 10)
print "\n\@evens = @evens\n";

## In a scalar context, grep returns the number of selected elements.
## This call to grep illustrates how grep is called in a scalar
## context. $number_of_evens is the number of even numbers in
## @numbers. 
my $number_of_evens = grep $_ % 2 == 0, @numbers;
## There are 5 even numbers in @numbers;
print "\n\$number_of_evens = $number_of_evens\n";

## this is a quote by Hafiz.
my @hafiz_quote = qw(For I have learned that every heart will get what it prays for most);

## Here is an example of using grep with a code block. Code blocks
## can be used for side effects, e.g., print some info when each
## selection is being made. from the quote we select the strings 
## whose length is greater than 4 and print each string in double 
## quotes that we include into the output.
my @selected_words = grep {
	print 'Processing ' . "\"$_\"" . "...\n";
	if ( length($_) > 4 ) {
		print 'Including ' . "\"$_\" to output list...\n";
		1;
	}
	else {
		0;
	}
} @hafiz_quote;
## @selected == ('learned', 'every', 'heart', 'prays');
print "\n\@selected_words = @selected_words\n\n";

## Here is an example of how grep can be used with subroutines.
## A subroutine is applied to $_.
sub is_odd { return $_[0] % 2 != 0; }

my @odds = grep is_odd($_), @numbers;
my $number_of_odds = grep is_odd($_), @numbers;

## there 6 odd numbers in odds so 
## @odds == (1, 3, 5, 7, 9, 11)
print "\n\@odds = @odds\n";
## $number_of_odds == 6.
print "\n\$number_of_odds = $number_of_odds\n";

## a couple of more examples of code blocks and list and
## scalar contexts.
## return all numbers x from @numbers if x + 5 is even.
my @list_of_nums = grep {
  my $i = $_;
  my $i_plus_5 = $i + 5;
  print "$i, $i_plus_5\n" if $i_plus_5 % 2 == 0;
  $i_plus_5 % 2 == 0 ? 1: 0;
} @numbers;

print "\n\@list_of_nums = @list_of_nums\n";

## In a scalar context, grep returns the number of x
## in @numbers if x + 5 is even.
my $count_of_nums = grep {
  my $i = $_;
  my $i_plus_5 = $i + 5;
  print "$i, $i_plus_5\n" if $i_plus_5 % 2 == 0;
  $i_plus_5 % 2 == 0 ? 1: 0;
} @numbers;

print "\n\$count_of_nums = $count_of_nums\n";





