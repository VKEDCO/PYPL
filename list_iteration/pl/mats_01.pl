#!/usr/bin/perl
use strict;
use warnings;

##########################################
## construction of 2D matrix with
## list refs.
##
## author: vladimir kulyukin
##
## the camel always delivers...
##########################################

my @row0 = (1, 2, 3, 4);
my @row1 = (5, 6, 7, 8);
my @row2 = (9, 10, 11, 12);

my @mat = (\@row0, \@row1, \@row2);

## print each row
my @r0 = @{$mat[0]};
print "@r0\n";
my @r1 = @{$mat[1]};
print "@r1\n";
my @r2 = @{$mat[2]};
print "@r2\n";

## print each row in a for loop
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

print_2d_mat(@mat);
print_2d_mat2(\@mat, 3, 4);
