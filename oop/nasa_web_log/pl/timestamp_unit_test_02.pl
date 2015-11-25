#!/usr/bin/perl

## change this path to where Timestamp.pm is 
use lib 'C:/Users/Vladimir/programming/nasa_wlog/pl_nasa_wlog/';

use strict;
use warnings;
use Timestamp;

my $str = '01/Jul/1995:00:00:01 -0400';
my $tm2 = new Timestamp();
if ( $tm2 ) {
    $tm2->setDay('01');
    $tm2->setMonth('Jul');
    $tm2->setYear('1995');
    $tm2->setHour('00');
    $tm2->setMins('00');
    $tm2->setSecs('01');

    print 'string representation: ' . $tm2->toString() . "\n";
}
else {
    print 'no timestamp created' . "\n";
}
