#!/usr/bin/perl

######################################
# @author: vladimir kulyukin
######################################

use lib 'C:/Users/Vladimir/programming/pl/';
use warnings;
use strict;
use MyMathPL::Subt::SubtTwo;
use MyMathPL::Subt::SubtThree;
use MyMathPL::Subt::SubtFour;

my $diff1 = 0;
my $diff2 = 0;
############# Testing MyMathPL::Subt::SubtTwo ######################
MyMathPL::Subt::SubtTwo::info();
$diff1 = MyMathPL::Subt::SubtTwo::subt2(12, 10);
$diff2 = MyMathPL::Subt::SubtTwo::subt2(15.5, 10.2);
print $diff1, "\n";
print $diff2, "\n";
print "\n";

############# Testing MyMathPL::Subt::SubtThree ######################
MyMathPL::Subt::SubtThree::info();
$diff1 = MyMathPL::Subt::SubtThree::subt3(15, 5, 3);
$diff2 = MyMathPL::Subt::SubtThree::subt3(15.5, 5.5, 3.5);
print $diff1, "\n";
print $diff2, "\n";
print "\n";

############# Testing MyMathPL::Subt::SubtFour ######################
MyMathPL::Subt::SubtFour::info();
$diff1 = MyMathPL::Subt::SubtFour::subt4(15, 5, 3, 2);
$diff2 = MyMathPL::Subt::SubtFour::subt4(15.5, 5.5, 3.5, 2.5);
print $diff1, "\n";
print $diff2, "\n";
print "\n";
