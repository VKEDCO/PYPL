#!/usr/bin/perl

########################################################################################
# solution to the student records problem
# at http://www.vkedco.blogspot.com/2013/02/python-perl-square-bottom-line-relief.html
# bugs to vladimir dot kulyukin at gmail dot com
########################################################################################

use strict;
use warnings;

my %student_records =
(
 0 => 'J.P.;GPA=3.5;A1927;11/01/91',
 1 => 'GPA=4.0;N.K.;12/01/90;A2732',
 2 => 'A9803;GPA=3.25;M.D.;10/03/87',
 3 => '05/01/89;A1248;GPA=2.87;D.W.',
 4 => 'GPA=3.87;L.M.;03/17/89;A6752'
);

my $initials_regex = '([A-Z]\.[A-Z]\.)';
my $gpa_regex = 'GPA=(\d\.\d{1,3})';
my $anum_regex = '(A\d{4})';
my $date_regex = '(\d{2}\/\d{2}\/\d{2})';

## a test on split
my @list = split(';','J.P.;GPA=3.5;A1927;11/01/91');
print "@list\n";

## a test of regexes
foreach (@list) {
    if ( $_ =~ /^$initials_regex$/ ) {
	print "match $1\n";
    }
    if ( $_ =~ /^$gpa_regex$/ ) {
	print "match gpa = $1\n";
    }
    if ( $_ =~ /^$anum_regex$/ ) {
	print "match anum = $1\n";
    }
    if ( $_ =~ /^$date_regex$/ ) {
	print "match date = $1\n";
    }
  }

sub process_student_record_line
{
    my $line = $_[0];
    my %record = ();
    foreach (split(';', $line)) {
	if ( $_ =~ /^$initials_regex$/ ) {
	    $record{'Initials'} = $1;
	}
	if ( $_ =~ /^$gpa_regex$/ ) {
	    $record{'GPA'} = $1;
	}
	if ( $_ =~ /^$anum_regex$/ ) {
	    $record{'ANUM'} = $1;
	}
	if ( $_ =~ /^$date_regex$/ ) {
	    $record{'BirthDate'} = $1;
	}
    }
    return \%record;
}

sub build_student_record_table 
{
    my %student_table = ();
    my $current_record = ();
    while ( my ($record_num, $line) = each(%{$_[0]}) ) {
	$current_record = process_student_record_line($line);
	$student_table{$current_record->{'ANUM'}} = $current_record;
    }
    return \%student_table;
}

my $student_table_ref = build_student_record_table(\%student_records);

sub display_student_record_table
{
    while ( my ($anum, $student_record) = each(%{$_[0]}) ) {
	while ( my ($key, $val) = each(%{$student_record}) ) {
	    print "$key --> $val\n";
	}
	print "\n";
    }
}

display_student_record_table($student_table_ref);
