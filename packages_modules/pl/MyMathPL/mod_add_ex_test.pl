#!/usr/bin/perl

## bugs to vladimir dot kulyukin at gmail dot com

## change this root accordingly.
use lib "/home/vladimir/Dropbox/teaching/PythonPerl/s13/lectures/18/";
use warnings;
use strict;
use MyMathPL::Add::AddTwoEx;
use MyMathPL::Add::AddThreeEx;
use MyMathPL::Add::AddFourEx;

############# Testing MyMathPL::Add::AddTwoEx ######################
MyMathPL::Add::AddTwoEx::info(); ## info is not exported
my $add2_n01 = add2(10, 12); ## add2 is exported
my $add2_n02 = add2(10.5, 12.5); ## add2 is exported
print $add2_n01, "\n";
print $add2_n02, "\n";
print "\n";

############# Testing MyMathPL::Add::AddThreeEx ######################
MyMathPL::Add::AddThreeEx::info(); ## info is not exported
my $add3_n01 = add3(10, 12, 15); ## add3 is exported
my $add3_n02 = add3(10.5, 12.5, 15.5); ## add3 is exported
print $add3_n01, "\n";
print $add3_n02, "\n";
print "\n";

############# Testing MyMathPL::Add::AddFourEx ######################
MyMathPL::Add::AddFourEx::info(); ## info is not exported
my $add4_n01 = add4(10, 12, 15, 20); ## add4 is exported
my $add4_n02 = add4(10.5, 12.5, 15.5, 20.5); ## add4 is exported
print $add4_n01, "\n";
print $add4_n02, "\n";
print "\n";




