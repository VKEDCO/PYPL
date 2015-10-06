#!/usr/bin/perl

##########################################
## matching special characters
## author: vladimir kulyukin
##########################################

use strict;
use warnings;

my $txt_01 = '12345';
my $txt_02 = 'abcde';
my $txt_03 = ' .;!?\\';
my $txt_04 = ' .;!?\\_';
my $txt_05 = ' .;!?\\_\n';

my @txt_lst = ($txt_01, $txt_02, $txt_03, $txt_04, $txt_05);

sub find_digit_char {
    my $txt = $_[0];
    if ( $txt =~ /\d/ ) {
	print "there is at least one digit char in \'$txt\'\n";
    }
    else {
	print "there are no digit chars in \'$txt\'\n";
    }
}

sub digit_char_tests {
    print '**** /\\d/ Tests ****', "\n";
    find_digit_char($_) foreach(@_);
    print "\n";
}

sub find_nondigit_char {
    my $txt = $_[0];
    if ( $txt =~ /\D/ ) {
	print "there is at least one non-digit char in \'$txt\'\n";
    }
    else {
	print "there are no non-digit chars in \'$txt\'\n";
    }
}

sub nondigit_char_tests {
    print '**** /\\D/ Tests ****', "\n";
    find_nondigit_char($_) foreach(@_);
    print "\n";
}

sub find_word_char {
    my $txt = $_[0];
    if ( $txt =~ /\w/ ) {
	print "there is at least one word char in \'$txt\'\n";
    }
    else {
	print "there are no word chars in \'$txt\'\n";
    }
}

sub word_char_tests {
    print '**** /\\w/ Tests ****', "\n";
    find_word_char($_) foreach(@_);
    print "\n";
}

sub find_nonword_char {
    my $txt = $_[0];
    if ( $txt =~ /\W/ ) {
	print "there is at least one non-word char in \'$txt\'\n";
    }
    else {
	print "there are no non-word chars in \'$txt\'\n";
    }
}

sub nonword_char_tests {
    print '**** /\\W/ Tests ****', "\n";
    find_nonword_char($_) foreach(@_);
    print "\n";
}

sub find_whitespace_char {
    my $txt = $_[0];
    if ( $txt =~ /\s/ ) {
	print "there is at least one whitespace char in \'$txt\'\n";
    }
    else {
	print "there are no whitespace chars in \'$txt\'\n";
    }
}

sub whitespace_char_tests {
    print '**** /\\s/ Tests ****', "\n";
    find_whitespace_char($_) foreach(@_);
    print "\n";
}

sub find_nonwhitespace_char {
    my $txt = $_[0];
    if ( $txt =~ /\S/ ) {
	print "there is at least one non-whitespace char in \'$txt\'\n";
    }
    else {
	print "there are no non-whitespace chars in \'$txt\'\n";
    }
}

sub nonwhitespace_char_tests {
    print '**** /\\S/ Tests ****', "\n";
    find_nonwhitespace_char($_) foreach(@_);
    print "\n";
}

## uncomment to run these tests
#digit_char_tests(@txt_lst);
#nondigit_char_tests(@txt_lst);
#word_char_tests(@txt_lst);
#nonword_char_tests(@txt_lst);
#whitespace_char_tests(@txt_lst);
#nonwhitespace_char_tests(@txt_lst);

