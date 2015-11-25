#!/usr/bin/perl

## change this path to where Timestamp.pm is 
use lib 'C:/Users/Vladimir/programming/nasa_wlog/pl_nasa_wlog/';

use strict;
use warnings;
use Timestamp;

my $tm1 = Timestamp->make('Jul', '01', '1995', '00', '00', '01');
if ( $tm1 ) {
    print 'month: ' . $tm1->getMonth() . "\n";
    print 'day:   ' . $tm1->getDay()   . "\n";
    print 'year:  ' . $tm1->getYear()  . "\n";
    print 'hour:  ' . $tm1->getHour()  . "\n";
    print 'mins:  ' . $tm1->getMins()  . "\n";
    print 'secs:  ' . $tm1->getSecs()  . "\n";

    print 'string representation: ' . $tm1->toString() . "\n";
}
else {
    print 'no timestamp created' . "\n";
}
