#!/usr/bin/perl

###############################
## @author: vladimir kulyukin
###############################    
use strict;
use warnings;
use sort '_quicksort';
use sort 'stable';

my @note_freq_toops = ();
while ( <> ) {
    if ( $_ =~ /\S+/ ) {
	my @note_freq_toop = split(/\t/, $_);
	push(@note_freq_toops, \@note_freq_toop);
    }
}
print "@{$_}[0]\t@{$_}[1]" foreach(sort { @{$b}[1] <=> @{$a}[1] } @note_freq_toops);
