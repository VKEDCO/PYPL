#!/usr/bin/perl

## change this path to where Employee.pm and Date.pm
## are defined.
use lib '/home/vladimir/programming/pl/oop/';

use strict;
use warnings;
use Employee;
use Date;

my $hd  = new Date();
$hd->setMonth(10);
$hd->setDay(10);
$hd->setYear(2010);

my $emp = new Employee();
$emp->setFirstName('John');
$emp->setLastName('Nicholson');
$emp->setHireDate($hd);

print 'First Name: ' . $emp->getFirstName(), "\n";
print 'Last  Name: ' . $emp->getLastName(), "\n";
print 'Hire Date:  ' . $emp->getHireDate()->toMDYString(), "\n";


