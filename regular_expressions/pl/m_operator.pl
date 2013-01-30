#!/usr/bin/perl

use strict;
use warnings;

my $txt = "
The mind which is wrongly guided does even greater harm
than the harm inflicted by an enemy upon his foe.

Buddha
";

## the match operator m is followed by a regular expression, aka
## a pattern, inside two matching delimiters: m/<regexp>/. 
## if there is a text txt where we need to find some matches
## for a regular expression, we say
## txt =~ m/regexp/
## =~ is a binding operator, it binds txt on the left to
## the regular expression of the match operator.

if ( $txt =~ m/guided/ ) {
  print "'guided' is found\n";
}

## The delimiters // are most common, but other delimiters are possible.
## m(regexp) or m[regexp] or m{regexp}. For example: 

if ( $txt =~ m{guided} ) {
  print "'guided' is found\n";
}

## A slight advantage of using // to delimit a regexp is that
## the m operator can be completely omitted. Thus,
## $txt =~ m/guided/ is the same as $txt =~ /guided/.

if ( $txt =~ /guided/ ) {
  print "'guided' is found\n";
}

## in the absence of the binding operator =~, the m works
## on $_. In the following code segment /ab/ is searched for 
## in $_ which is iteratively bound to '001', 
## 'ababab', '10ab01', '10001', and 'bcdefg'.
## The output is
## 'ab' is found in 'ababab'
## 'ab' is found in '10ab01'

foreach ('001', 'ababab', '10ab01', '10001', 'bcdefg') {
  print "'ab' is found in '$_'\n" if /ab/;
}

## patterns can be bound to variables and properly
## interpolated. In this example, each value of $_
## is treated is as a pattern that is searched for
## in $txt. The output is
## 'guided' is FOUND
## 'harm' is FOUND
## 'Buddha' is FOUND
## 'rightly' is NOT FOUND

foreach ('guided', 'harm', 'Buddha', 'rightly') {
  if ( $txt =~ /$_/ ) {
    print "'$_' is FOUND\n";
  }
  else {
    print "'$_' is NOT FOUND\n";
  }
}

