#!/usr/bin/perl

use strict;
use warnings;

## displaying not only line numbers but also
## the file names
sub print_diamond_files {
  my $line_counter = 0;
  while ( <> ) {
    $line_counter++;
    print "$ARGV $line_counter:\t $_";
  }
}

print_diamond_files();
