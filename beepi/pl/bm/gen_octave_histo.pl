#!/usr/bin/perl

use strict;
use warnings;

print "Y = [\n";
while ( <> ) {
    if ( $_ =~ /\S+/ ) {
	my @matches = split('\t', $_);
	if ( scalar(@matches) > 0 ) {
	    print int($matches[1]) . ",\n";
	}
    }
}
print "];\n";
print "figure;\n";
print "bar(Y, 'FaceColor', [0, 0.5, 0.5],\n";
print "'EdgeColor', [0, 0.5, 0.5],\n";
print "'LineWidth', 2);\n";
print "title('A440 Note Frequencies');\n";
