#!/usr/bin/perl

## bugs to vladimir dot kulyukin at gmail dot com

use lib "/home/vladimir/Dropbox/teaching/PythonPerl/s13/lectures/18/";
use warnings;
use strict;
use MyMathPL::Add::AddTwo;
use MyMathPL::Add::AddThree;
use MyMathPL::Add::AddFour;

############# Testing MyMathPL::Add::AddTwo ######################
MyMathPL::Add::AddTwo::info();
my $add2_n01 = MyMathPL::Add::AddTwo::add2(10, 12);
my $add2_n02 = MyMathPL::Add::AddTwo::add2(10.5, 12.5);
print $add2_n01, "\n";
print $add2_n02, "\n";
print "\n";

############# Testing MyMathPL::Add::AddThree ######################
MyMathPL::Add::AddThree::info();
my $add3_n01 = MyMathPL::Add::AddThree::add3(10, 12, 15);
my $add3_n02 = MyMathPL::Add::AddThree::add3(10.5, 12.5, 15.5);
print $add3_n01, "\n";
print $add3_n02, "\n";
print "\n";

############# Testing MyMathPL::Add::AddFour ######################
MyMathPL::Add::AddFour::info();
my $add4_n01 = MyMathPL::Add::AddThree::add3(10, 12, 15, 20);
my $add4_n02 = MyMathPL::Add::AddThree::add3(10.5, 12.5, 15.5, 20.5);
print $add4_n01, "\n";
print $add4_n02, "\n";
print "\n";




