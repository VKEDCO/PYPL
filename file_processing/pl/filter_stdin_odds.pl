#!/usr/bin/perl
## prints odd numbers from STDIN
## to test:
## > more numbers.txt | perl filter_stdin_odds.pl
use strict;
use warnings;
while ( <> ) { print $_ if ( $_ % 2 != 0 ) };
