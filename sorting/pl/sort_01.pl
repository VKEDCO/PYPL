#!/usr/bin/perl

use strict;
use warnings;

################################################
#
# illustrates that the default sort in PL is ASCII 
# lexicographic, i.e., numbers are converted into 
# string scalars and sorted lexicographically. if
# the ASCII lexicographic order happens to coincide
# with the numerical order, as is the case in the first
# example below, then everything looks normal. however,
# when the ASCII lexicographic order is different from
# the numerical order, as is the case in the second
# example, then the output may look unusual.
#
# author: vladimir kulyukin
#
# ... nor shall they enter the Garden, until
# the camel enters the eye of the needle.
#################################################

sub sorting_test_0 {
    print "**** SORTING TEST 0 ****\n\n";
    my @numbers = (2, 1, 3, 4, -1);
    print '@numbers before sort:', "\t@numbers\n";
    ## this prints out -1 1 2 3 4
    my @sorted_numbers = sort @numbers;
    print '@sorted_numbers:', "\t@sorted_numbers\n";
    ## @numbers did not change. sorting is not in place
    print '@numbers after sort:', "\t@numbers\n";
    print "\n";
}

## the sorted array below prints out as -1 1 11 2 22 3 4. 
## What gives? PL's default sorting behavior is ASCII sort, i.e.,
## each number is converted into an ASCII string and
## lexicographically sorted.
## In the first application of sort above to the list (2 1 3 4 -1)
## ASCII lexicographic order is the same as the numerical
## order. In this application, however, the ASCII sort order is 
## different. Hence, this puzzling result.

sub sorting_test_1 {
    print "**** SORTING TEST 1 ****\n\n";
    
    my @numbers = (11, 2, 1, 22, 3, 4, -1);
    print '@numbers before sort:', "\t@numbers\n";
    
    my @sorted_numbers = sort @numbers;
    print '@sorted_numbers:', "\t@sorted_numbers\n";

    ## @numbers2 did not change. sorting is not in place
    print '@numbers2 after sort:', "\t@numbers\n";
    print "\n";
}

## the output will be the same as for sorting_test_0, which
## proves that the default sort is ASCII lexicographic.
sub sorting_test_2 {
    print "**** SORTING TEST 2 ****\n\n";
    
    my @numbers = ('2', '1', '3', '4', '-1');
    print '@numbers before sort:', "\t@numbers\n";
    my @sorted_numbers = sort @numbers;
    print '@sorted_numbers:', "\t@sorted_numbers\n";
    print "\n";
}

sub sorting_test_3 {
    print "**** SORTING TEST 3 ****\n\n";
    
    my @numbers = ('11', '2', '1', '22', '3', '4', '-1');
    print '@numbers before sort:', "\t@numbers\n";
    my @sorted_numbers = sort @numbers;
    print '@sorted_numbers:', "\t@sorted_numbers\n";
    print "\n";
}

sorting_test_0();
sorting_test_1();
sorting_test_2();
sorting_test_3();
