#!/usr/bin/perl

## Testing Date.pm
## bugs to vladimir dot kulyukin at gmail dot com

## change this path as necessary
use lib "D:/Dropbox/teaching/PythonPerl/s13/lectures/20";

use Date;
use strict;
use warnings;

## ******* Method 01: Object Construction ***********
my $date_01 = new Date();

$date_01->year(2013);
$date_01->month(3);
$date_01->day(23);

print '$date_01 is '; 
$date_01->printMDY();
print "\n";

print ref($date_01), "\n";

## ******* Method 02: Object Construction ************
my $date_02 = $date_01->new();

Date::year($date_02, 2013);
Date::month($date_02, 3);
Date::day($date_02, 24);

print '$date_02 is '; 
$date_02->printMDY();
print "\n";

## ****** Method 03: Object Construction ******
my $date_03 = Date->new();

$date_03->year(2013);
$date_03->month(3);
$date_03->day(25);

print '$date_03 is '; 
$date_03->printMDY();
print "\n";

## ****** Method 04: Object Construction ******
my $date_04 = Date->make();

$date_04->year(2013);
$date_04->month(3);
$date_04->day(26);

print '$date_04 is '; 
$date_04->printMDY();
print "\n";

## ***********************************

{
  my $d = Date->make();
  $d->year(2013);
  $d->month(3);
  $d->day(27);
  ## $d will be destroyed after this scope
  ## is left.
}







