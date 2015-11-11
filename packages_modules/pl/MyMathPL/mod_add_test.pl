#!/usr/bin/perl

##########################################
# @author: vladimir kulyukin
##########################################

use warnings;
use strict;
use lib 'C:/Users/Vladimir/programming/pl/';
use MyMathPL::Add::AddTwo;
use MyMathPL::Add::AddThree;
use MyMathPL::Add::AddFour;

my $sum1 = 0;
my $sum2 = 0;
############# Testing MyMathPL::Add::AddTwo ######################
MyMathPL::Add::AddTwo::info();
$sum1 = MyMathPL::Add::AddTwo::add2(10, 12);
$sum2 = MyMathPL::Add::AddTwo::add2(10.5, 12.5);
print $sum1, "\n";
print $sum2, "\n";
print "\n";

############# Testing MyMathPL::Add::AddThree ######################
MyMathPL::Add::AddThree::info();
$sum1 = MyMathPL::Add::AddThree::add3(10, 12, 15);
$sum2 = MyMathPL::Add::AddThree::add3(10.5, 12.5, 15.5);
print $sum1, "\n";
print $sum2, "\n";
print "\n";

############# Testing MyMathPL::Add::AddFour ######################
MyMathPL::Add::AddFour::info();
$sum1 = MyMathPL::Add::AddThree::add3(10, 12, 15, 20);
$sum2 = MyMathPL::Add::AddThree::add3(10.5, 12.5, 15.5, 20.5);
print $sum1, "\n";
print $sum2, "\n";
print "\n";
