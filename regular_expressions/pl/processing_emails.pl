#!/usr/bin/perl

######################################################
## using PL regular expressions to find and
## retrieve the components of an email address: 1)
## user name; 2) host name; 3) host extension.
## @author: vladimir kulyukin
######################################################

use strict;
use warnings;

my $TXT_01 = '
John   Balbiro	A1001	john.balbiro@usu.edu
Alice  Nelson	A0011	alice.nelson@workflow.net
Jacob  Roberts	A1100	j.s.roberts@gmail.com
';

my $email_pat_1 = '([\w.-]+@[\w.-]+\.(?:com|net|org|edu))';
my @emails_1 = ();
while ( $TXT_01 =~ m/$email_pat_1/g ) {
    push(@emails_1, $1);
}

my $email_pat_2 = '([\w.-]+@[\w.-]+)\.(com|net|org|edu)';
my @emails_2 = ();
while ( $TXT_01 =~ m/$email_pat_2/g ) {
    my @lst = ();
    push(@lst, $1);
    push(@lst, $2);
    push(@emails_2, \@lst);
}

my $email_pat_3 = '([\w.-]+)@([\w.-]+)\.(com|net|org|edu)';
my @emails_3 = ();
while ( $TXT_01 =~ m/$email_pat_3/g ) {
    my @lst = ();
    push(@lst, $1);
    push(@lst, $2);
    push(@lst, $3);
    push(@emails_3, \@lst);
}

print "$_\n"    foreach(@emails_1);
print "@{$_}\n" foreach(@emails_2);
print "@{$_}\n" foreach(@emails_3);
