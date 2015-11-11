#!/usr/bin/perl

##########################################
# @author: vladimir kulyukin
##########################################

use lib 'C:/Users/Vladimir/programming/pl/';
use warnings;
use strict;
use MyMathPL::Add::AddTwoEx;
use MyMathPL::Add::AddThreeEx;
use MyMathPL::Add::AddFourEx;

my $sum1 = 0;
my $sum2 = 0;
############# Testing MyMathPL::Add::AddTwoEx ######################
MyMathPL::Add::AddTwoEx::info(); ## info is not exported
$sum1 = add2(10, 12); ## add2 is exported
$sum2 = add2(10.5, 12.5); ## add2 is exported
print $sum1, "\n";
print $sum2, "\n";
print "\n";

############# Testing MyMathPL::Add::AddThreeEx ######################
MyMathPL::Add::AddThreeEx::info(); ## info is not exported
$sum1 = add3(10, 12, 15); ## add3 is exported
$sum2 = add3(10.5, 12.5, 15.5); ## add3 is exported
print $sum1, "\n";
print $sum2, "\n";
print "\n";

############# Testing MyMathPL::Add::AddFourEx ######################
MyMathPL::Add::AddFourEx::info(); ## info is not exported
$sum1 = add4(10, 12, 15, 20); ## add4 is exported
$sum2 = add4(10.5, 12.5, 15.5, 20.5); ## add4 is exported
print $sum1, "\n";
print $sum2, "\n";
print "\n";
