#!/usr/bin/perl
use strict;
use warnings;

##########################################
## programmatic construction of 2D matrix 
## with list refs & push.
##
## author: vladimir kulyukin
##
## the camel always delivers...
##########################################

my @mat = ();

## add rows into 2d mat
my @row0 = (1..4);
push(@mat, \@row0);
my @row1 = (5..8);
push(@mat, \@row1);
my @row2 = (9..12);
push(@mat, \@row2);

## print each rwo in a for loop
sub print_2d_mat {
    my @mat = @_;
    for(my $r = 0; $r <= $#mat; $r++) {
	print "@{$mat[$r]}\n";
    }
}

## print with two for loops
sub print_2d_mat2 {
    my @mat = @{$_[0]};
    my $num_rows = $_[1];
    my $num_cols = $_[2];
    for(my $r = 0; $r < $num_rows; $r++) {
	for(my $c = 0; $c < $num_cols; $c++) {
	    print $mat[$r][$c], "\t";
	}
	print "\n";
    }
}

## test
print_2d_mat(@mat);
print_2d_mat2(\@mat, 3, 4);

