#!/usr/bin/perl

## change this directory to where WebLogEntry.pm is
use lib 'C:/Users/Vladimir/programming/nasa_wlog/pl_nasa_wlog/';
use WebLogEntry;
use strict;
use warnings;

my $str1  = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245';
my $wle1 = WebLogEntry->toWebLogEntry($str1);

if ( $wle1 ) {
    print 'IP:      ' . $wle1->getIP() . "\n";
    print 'TS:      ' . $wle1->getTimestamp()->toString() . "\n";
    print 'METHOD:  ' . $wle1->getMethod() . "\n";
    print 'URL:     ' . $wle1->getURL() . "\n";
    print 'PROTOCOL ' . $wle1->getProtocol() . "\n";
    print 'STATUS   ' . $wle1->getStatusCode() . "\n";
    print 'TRBYTES  ' . $wle1->getTransBytes() . "\n";

    print "\n\nGENERATED HTML\n\n";
    print $wle1->toHtmlUL(), "\n";
}
