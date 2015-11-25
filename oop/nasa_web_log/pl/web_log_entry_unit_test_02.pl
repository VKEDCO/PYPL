#!/usr/bin/perl

## change this directory to where WebLogEntry.pm is
use lib 'C:/Users/Vladimir/programming/nasa_wlog/pl_nasa_wlog/';
use WebLogEntry;
use strict;
use warnings;

my $str2 = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 -';
my $wle2 = WebLogEntry->toWebLogEntry($str2);

if ( $wle2 ) {
    print 'IP:      ' . $wle2->getIP() . "\n";
    print 'TS:      ' . $wle2->getTimestamp()->toString() . "\n";
    print 'METHOD:  ' . $wle2->getMethod() . "\n";
    print 'URL:     ' . $wle2->getURL() . "\n";
    print 'PROTOCOL ' . $wle2->getProtocol() . "\n";
    print 'STATUS   ' . $wle2->getStatusCode() . "\n";
    print 'TRBYTES  ' . $wle2->getTransBytes() . "\n";

    print "\n\nGENERATED HTML\n\n";
    print $wle2->toHtmlUL(), "\n";
}
