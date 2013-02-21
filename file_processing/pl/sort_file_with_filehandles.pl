#!/usr/bin/perl

## to run: 
## sort_file_with_filehandles.pl unsorted_numbers.txt sorted_numbers.txt

my $infile = shift();
my $outfile = shift();

open(IN, '<', $infile) or die $!;
open(OUT, '>', $outfile) or die $!;

print OUT sort { $a <=> $b } <IN>;
