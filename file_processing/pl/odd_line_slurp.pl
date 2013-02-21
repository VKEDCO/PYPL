#!/usr/bin/perl

#####################################################
## to run:
## > ./old_line_slurp.pl <file_name>
## > perl old_line_slurp.pl <file_name>
## e.g. 
## perl old_line_slurp.pl al_ghazali_knowledge.txt
## bugs to vladimir dot kulyukin at gmail dot com
#####################################################

use strict;
use warnings;

sub print_odd_lines {
    my $file_path = shift();
    open(IN, '<', $file_path) or die $!;
    my @lines = <IN>;
    for(my $i = 1; $i <= $#lines+1; $i++) {
      if ( $i % 2 != 0 ) {
	print $i, ":\t$lines[$i-1]";
      }
    }
    close(IN);
}

my $fp = shift;
print_odd_lines($fp);
