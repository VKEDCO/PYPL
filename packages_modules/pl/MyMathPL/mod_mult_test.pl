#!/usr/bin/perl

## bugs to vladimir dot kulyukin at gmail dot com

## change this root accordingly.
use lib "/home/vladimir/Dropbox/teaching/PythonPerl/s13/lectures/18/";
use warnings;
use strict;
use MyMathPL::Mult::MultTwo;
use MyMathPL::Mult::MultFour;

############# Testing MyMathPL::Mult::MultTwo ######################
MyMathPL::Mult::MultTwo::info();
my $mult2_n01 = MyMathPL::Mult::MultTwo::mult2(10, 12); 
my $mult2_n02 = MyMathPL::Mult::MultTwo::mult2(10.5, 12.5);
print $mult2_n01, "\n";
print $mult2_n02, "\n";
print "\n";

############# Testing MyMathPL::Mult::MultFour ######################
MyMathPL::Mult::MultFour::info();
my $mult4_n01 = MyMathPL::Mult::MultFour::mult4(10, 12, 15, 20);
my $mult4_n02 = MyMathPL::Mult::MultFour::mult4(10.5, 12.5, 15.5, 20.5); 
print $mult4_n01, "\n";
print $mult4_n02, "\n";
print "\n";




