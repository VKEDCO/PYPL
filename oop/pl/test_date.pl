#!/usr/bin/perl
## author: vladimir kulyukin
## change this path to where Date.pm is 
use lib '/home/vladimir/programming/pl/oop/';
use Date;
use strict;
use warnings;

my $d1 = new Date();

$d1->setYear(2015);
$d1->setMonth(11);
$d1->setDay(19);
print '1st date: ', $d1->toMDYString(), "\n";

my $d2 = new Date();
Date::setYear($d2, 2015);
Date::setMonth($d2, 11);
Date::setDay($d2, 19);
print '2nd date: ', $d2->toYMDString(), "\n";

## this is an example of how to call make method
my $DATE_FACTORY = new Date();
my $d3 = $DATE_FACTORY->make(11, 19, 2015);
print '3rd date: ', $d2->toYMDString(), "\n";



