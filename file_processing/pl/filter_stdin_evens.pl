#!/usr/bin/perl
## print input numbers from STDIN
## to test:
## > more numbers.txt | perl filter_stdin_evens.pl
use strict;
use warnings;
while ( <> ) { print $_ if ( $_ % 2 == 0 ); }
