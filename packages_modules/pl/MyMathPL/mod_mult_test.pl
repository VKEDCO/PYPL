#!/usr/bin/perl

#################################
# @author: vladimir kulyukin
#################################

## change this root accordingly.
use lib 'C:/Users/Vladimir/programming/pl/';
use warnings;
use strict;
use MyMathPL::Mult::MultTwo;
use MyMathPL::Mult::MultFour;

my $prod1 = 0;
my $prod2 = 0;
############# Testing MyMathPL::Mult::MultTwo ######################
MyMathPL::Mult::MultTwo::info();
$prod1 = MyMathPL::Mult::MultTwo::mult2(10, 12); 
$prod2 = MyMathPL::Mult::MultTwo::mult2(10.5, 12.5);
print $prod1, "\n";
print $prod2, "\n";
print "\n";

############# Testing MyMathPL::Mult::MultFour ######################
MyMathPL::Mult::MultFour::info();
$prod1 = MyMathPL::Mult::MultFour::mult4(10, 12, 15, 20);
$prod2 = MyMathPL::Mult::MultFour::mult4(10.5, 12.5, 15.5, 20.5); 
print $prod1, "\n";
print $prod2, "\n";
print "\n";
