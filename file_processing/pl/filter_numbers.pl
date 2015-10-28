#!/usr/bin/perl

#######################################
# Read in a file of numbers and
# pick out odds or events and compute
# their sums.
# @author: vladimir kulyukin
#######################################

use strict;
use warnings;
use List::Util qw(sum);

sub is_odd  { return $_[0] % 2 != 0; }
sub is_even { return !is_odd($_[0]); }

sub filter_lines {
    my ($file_path, $fun, $pred) = @_;
    open(IN, '<', $file_path) or die $!;
    my @rslt = ();
    while(<IN>) { push(@rslt, $fun->($_)) if ($pred->($_)); }
    return \@rslt;
}

sub pick_odds  { 
    return filter_lines($_[0], 
			sub { return int($_[0]); }, 
			\&is_odd);  
}

sub pick_evens { 
    return filter_lines($_[0], 
			sub { return int($_[0]); }, 
			\&is_even); 
}

sub sum_odds  { return sum(@{pick_odds($_[0])});  }
sub sum_evens { return sum(@{pick_evens($_[0])}); }

print $_, "\n" foreach(@{pick_odds($ARGV[0])});
print sum_odds($ARGV[0]), "\n\n";
print $_, "\n" foreach(@{pick_evens($ARGV[0])});
print sum_evens($ARGV[0]), "\n\n";
