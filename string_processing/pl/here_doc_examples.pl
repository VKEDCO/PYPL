#!/usr/bin/perl

######################################################
## several examples of Perl's here docs
##
## bugs to vladimir dot kulyukin at gmail dot com
######################################################

use strict;
use warnings;

# your basic everyday here-document
print "*** Example 1 ***\n";

print <<EOT;
This is a line of text.
This is another line of text ...
Good bye.
EOT

# we can use the same label in
# multiple here documents
print "\n*** Example 2 ***\n";

print <<EOT;
This is another here-document
which uses the same terminating label.
EOT

# We can make a different label
print "\n*** Example 3 ***\n";

print <<THIS_IS_MY_TEXT;
This is the third here-document
which uses a 
different terminating label called: 'END_OF_MY_TEXT'.


This is the last line of this here-document.
THIS_IS_MY_TEXT

# Here-documents can be assigned to varaibles
print "\n*** Example 4 ***\n";
my $txt_var = <<TXT_VAR;
On a day
when the wind is perfect,
the sail just needs to open and the world is full of beauty.
Today is such a
day.
	Jalal ad-Din Rumi
TXT_VAR

print "$txt_var\n";



