#!/usr/bin/perl

## bugs to vladimir dot kulyukin at gmail dot com

use lib "/home/vladimir/Dropbox/teaching/PythonPerl/s13/lectures/18/";
use warnings;
use strict;
use MyMathPL::Subt::SubtTwo;
use MyMathPL::Subt::SubtThree;
use MyMathPL::Subt::SubtFour;

############# Testing MyMathPL::Subt::SubtTwo ######################
MyMathPL::Subt::SubtTwo::info();
my $subt2_n01 = MyMathPL::Subt::SubtTwo::subt2(12, 10);
my $subt2_n02 = MyMathPL::Subt::SubtTwo::subt2(15.5, 10.2);
print $subt2_n01, "\n";
print $subt2_n02, "\n";
print "\n";

############# Testing MyMathPL::Subt::SubtThree ######################
MyMathPL::Subt::SubtThree::info();
my $subt3_n01 = MyMathPL::Subt::SubtThree::subt3(15, 5, 3);
my $subt3_n02 = MyMathPL::Subt::SubtThree::subt3(15.5, 5.5, 3.5);
print $subt3_n01, "\n";
print $subt3_n02, "\n";
print "\n";

############# Testing MyMathPL::Subt::SubtFour ######################
MyMathPL::Subt::SubtFour::info();
my $subt4_n01 = MyMathPL::Subt::SubtFour::subt4(15, 5, 3, 2);
my $subt4_n02 = MyMathPL::Subt::SubtFour::subt4(15.5, 5.5, 3.5, 2.5);
print $subt4_n01, "\n";
print $subt4_n02, "\n";
print "\n";




