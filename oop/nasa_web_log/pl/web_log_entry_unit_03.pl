#!/usr/bin/perl

## change this directory to where WebLogEntry.pm is
use lib 'C:/Users/Vladimir/programming/nasa_wlog/pl_nasa_wlog/';
use WebLogEntry;
use strict;
use warnings;

my $str3 = 'pipe2.nyc.pipeline.com - - [01/Jul/1995:22:41:11 -0400] "GET /shuttle/missions/sts-71/sts-71-patch-small.gif" 200 12054';
my $wle3 = WebLogEntry->toWebLogEntry($str3);
if ( $wle3 ) {
    print 'IP:      ' . $wle3->getIP() . "\n";
    print 'TS:      ' . $wle3->getTimestamp()->toString() . "\n";
    print 'METHOD:  ' . $wle3->getMethod() . "\n";
    print 'URL:     ' . $wle3->getURL() . "\n";
    print 'PROTOCOL ' . $wle3->getProtocol() . "\n";
    print 'STATUS   ' . $wle3->getStatusCode() . "\n";
    print 'TRBYTES  ' . $wle3->getTransBytes() . "\n";

    print "\n\nGENERATED HTML\n\n";
    print $wle3->toHtmlUL(), "\n";
}
