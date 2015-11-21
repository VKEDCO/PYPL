#!/usr/bin/perl

## change this path to where Date.pm is defined
use lib '/home/vladimir/programming/pl/oop/';
use Date;
use strict;
use warnings;

my @dates = ();

push(@dates, Date->make(11, 19, 2015));
push(@dates, Date->make(11, 20, 2015));
push(@dates, Date->make(11, 21, 2015));

## sort dates by day
print $_->toMDYString() . "\n" foreach(sort { $a->getDay() <=> $b->getDay() } @dates);
