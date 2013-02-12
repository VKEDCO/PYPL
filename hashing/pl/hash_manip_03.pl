#!/usr/bin/perl

##################################################################
## - more examples of Perl hashes from lists and quoted lists;
## - converting lists to hashes and hashes to lists;
## - functions keys(), values(), each()
## - sorting keys and values
## 
## bugs to vladimir dot kulyukin at gmail dot com
##################################################################

use strict;
use warnings;

## This table maps integers to names; it is created from a list 
## of key/value pairs; The key is an integer, the value is a string.
my %cs_phd_students_hash_01 = 
  (
   1, 'Chaitanya Gharpure',
   2, 'John Nicholson',
   3, 'Aliasgar Kutiyanawala'
  );

## $cs_phd_students{1} refers to the scalar 'Chaitanya Gharpure'
## $cs_phd_students{2} refers to the scalar 'John Nicholson'
## $cs_phd_students{3} refers to the scalar 'Aliasgar Kutiyanawala'
print $cs_phd_students_hash_01{1}, "\n"; 
print $cs_phd_students_hash_01{2}, "\n";
print $cs_phd_students_hash_01{3}, "\n";
## print $cs_phd_students_hash_01{4}, "\n";

## The => operator can be used to create a hash. What appears to 
## the left of => it treated as a double-quoted string. It cannot 
## have spaces.
my %cs_phd_students_hash_02 =
  (
   student_01 => 'Chaitanya Gharpure',
   student_02 => 'John Nicholson',
   student_03 => 'Aliasgar Kutiyanawala'
   );

## three identical ways of referencing the same value element.
print $cs_phd_students_hash_02{student_01}, "\n";
print $cs_phd_students_hash_02{'student_01'}, "\n";
print $cs_phd_students_hash_02{"student_01"}, "\n";

## key/value pair 01: 'Chaitanya'/'Gharpure'
## key/value pair 02: 'John'/'Nicholson'
## key/value pair 03: 'Aliasgar'/'Kutiyanawala'
my @cs_phd_student_names = qw(Chaitanya Gharpure John Nicholson Aliasgar Kutiyanawala);
my %cs_phd_students_hash_03 = @cs_phd_student_names;

print $cs_phd_students_hash_03{'Chaitanya'}, "\n";
print $cs_phd_students_hash_03{'John'}, "\n";
print $cs_phd_students_hash_03{'Aliasgar'}, "\n";

## You can also convert a hash to an array so long as you do not 
## care about the exact order of the keys.
my @hash_cs_phd_student_names = %cs_phd_students_hash_03;

print "\nArray of Names: ";
print "$_ " foreach(@hash_cs_phd_student_names);
print "\n";

## You can delete keys

## key/value pair 1/'Chaitanya Gharpure' is deleted.
delete $cs_phd_students_hash_01{1};
print $cs_phd_students_hash_01{1}, "\n";

## We insert a new key/value pair
$cs_phd_students_hash_01{4} = 'Chaitanya Gharpure';
print $cs_phd_students_hash_01{4}, "\n";

## keys function: keys(%hash) - list of keys in %hash 
## this prints out 4, 3, 2 on my machine but the order of keys
## is not guaranteed.
print "$_\n" foreach(keys(%cs_phd_students_hash_01));

## this sorts the keys as numbers
my @sorted_keys = sort { $a <=> $b } keys(%cs_phd_students_hash_01);
print "@sorted_keys\n";

## this sorts the keys as strings and prints 
## out 'Aliasgar Chaitanya John'
my @sorted_first_names = sort { $a cmp $b } keys(%cs_phd_students_hash_03);
print "@sorted_first_names\n";

## values function: values(%hash) - list of values in %hash
my @last_names = values(%cs_phd_students_hash_03);
## prints out "Gharpure Kutiyanawala Nicholson"
print "@last_names\n";

my @sorted_last_names = sort { $a cmp $b } 
values(%cs_phd_students_hash_03);
print "@sorted_last_names\n";

## each(%hash) is a hash iterator: it returns each key/value pair in %hash.
## Chaitanya --> Gharpure
## Aliasgar --> Kutiyanawala
## John --> Nicholson
while ( my ($key, $val) = each(%cs_phd_students_hash_03) ) {
  print "$key --> $val\n";
}

## this destructively modifies the passed hash.
sub modify_hash_01 {
  my $ht = $_[0];
  $ht->{'new key'} = 'new value';
}

sub test_modify_hash_01 {
  my %ht_to_test = qw(one 1 two 2);
  modify_hash_01(\%ht_to_test);
  while ( my ($key, $val) = each(%ht_to_test)) {
    print "$key --> $val\n";
  }
}
