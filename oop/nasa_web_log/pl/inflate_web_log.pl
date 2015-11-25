#!/usr/bin/perl

## author: vladimir kulyukin

use lib 'C:/Users/Vladimir/programming/nasa_wlog/pl_nasa_wlog/';
use WebLogEntry;
use strict;
use warnings;

## 1. get the command line arguments
my $lower     = shift(); ## lower bound
my $upper     = shift(); ## upper bound
my $top_n     = shift(); ## top_n
my $html_fp   = shift(); ## output html file path

## 2. Read in all text entries, convert them into WebLogEntry objects,
##    and place them into @web_log_entries.
my @web_log_entries = ();
while ( <> ) {
    if ( $_ =~ /\S+/ ) {
	my $web_log_entry = WebLogEntry->toWebLogEntry($_);
	if ( $web_log_entry ) {
	    push(@web_log_entries, $web_log_entry);
	}
	else {
	    print 'FAILURE: ' . $_;
	}
    }
}

## this is a debug print to show how many objects we have constructed
print scalar(@web_log_entries), "\n";

## 3. grep all entries whose transferred bytes are in [lower, upper]
@web_log_entries = grep { $_->getTransBytes >= $lower && $_->getTransBytes() <= $upper } @web_log_entries;
## 4. sort all entries in the range from highest to lowest
@web_log_entries = sort { $b->getTransBytes() <=> $a->getTransBytes() } @web_log_entries;

## 5. open an HTML file and write an HTML header into it
open(my $outstream, '>', $html_fp) or die $!;
print $outstream "<html>\n";
print $outstream "<head>\n";
print $outstream "<title>Nasa Web Log Entries</title>\n";
print $outstream "</head>\n";
print $outstream "<body>\n";
print $outstream "<h1>Found Nasa Web Log Entries</h1>\n";

## 6. convert each WebLogEntry object into an html ul and write it out into an html file
for(my $i = 0; $i < $top_n; $i++) {
    if ( defined($web_log_entries[$i]) ) {
	print $outstream $web_log_entries[$i]->toHtmlUL();
	print $outstream "<hr><br>\n";
    }
}

## 7. match the body and html tags.
print $outstream "</body>\n";
print $outstream "</html>\n";
