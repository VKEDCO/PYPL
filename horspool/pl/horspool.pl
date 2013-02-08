#!/usr/bin/perl

##############################################################
## PL implementation of Horspool's algorithm
## 
## sample use:
## 
## my $text = 'abe abc efg';
## my $pat  = 'abc';
## my %shift_table = build_shift_table($pattern);
## my $match_pos   = horspool($pattern, $text, \%shift_table);
## print $match_pos;
## 
## bugs to vladimir dot kulyukin at gmail dot com
##############################################################

use strict;
use warnings;

sub build_shift_table {
  my $pattern = shift();
  my %shift_table = ();
  my $plen = length($pattern);
  for(my $i = 0; $i < $plen-1; $i++) {
    $shift_table{substr($pattern, $i, 1)} = $plen-1-$i;
  }
  return %shift_table;
}

sub lookup_shift_value {
  my ($c, $pat_len, $shift_table) = @_;
  if ( exists($shift_table->{$c}) ) {
    return $shift_table->{$c};
  }
  else {
    return $pat_len;
  }
}

sub horspool {
  my ($pat, $text, $shift_table) = @_;
  my $pat_len    = length($pat);
  my $txt_len    = length($text);
  ## $pat_re_pos - $pat's right end position in $text when $pat is aligned with $text;
  ## it is used in index into $text, not #pat.
  my $pat_re_pos = $pat_len-1;

  ## $match_char_count - count of how many characters in $pat
  ## has been matched against corresponding
  ## characters in $text.
  my $matched_char_count = 0;

  ## keep going so long as $pat_re_pos does not
  ## go over the right bound of $text.
  while ( $pat_re_pos <= $txt_len-1 ) {
    $matched_char_count = 0;
    ##print "\$k = $k\n";
    ##print 'pc  = ', substr($pat, $pat_len-1-$k, 1), "\n";
    ##print 'tc  = ', substr($text, $i-$k, 1), "\n";

    ## keep incrementing $matched_char_count so long as
    ## 1) $matched_char_count <= $pat_len-1 AND
    ## 2) the current character in $pat ($pat_len - $matched_char_count - 1)
    ##    is the same as the corresponding character in $text 
    ##    (i.e., character at position $pat_re_pos - $matched_char_count)
    while ( ($matched_char_count <= $pat_len-1) && 
	    (substr($pat,  $pat_len - $matched_char_count - 1, 1) eq 
	     substr($text, $pat_re_pos - $matched_char_count, 1)) 
	  ) 
    {
      $matched_char_count += 1;
    }

    ## if the number of matched characters is the same
    ## as the pattern's length, return the position in $text
    ## at which the first character of the matched pattern $pat
    ## aligns with $text
    if ( $matched_char_count == $pat_len ) {
      return $pat_re_pos - $pat_len + 1;
    }
    else {
      ## lookup the shift value of the mismatched character in $text
      ## and shift $pat_re_pos right
      $pat_re_pos += lookup_shift_value(substr($text, $pat_re_pos, 1), 
					$pat_len, 
					$shift_table);
    }
  }
  ## no match found so return -1
  return -1;
}

################# Tests #######################

## prints the shift table for pattern 'abc'
## a -> 2
## b -> 1
sub horspool_test_01 
{
  my %tab = build_shift_table('abc');
  
  while ( my ($key, $val) = each(%tab) ) {
    print $key, ' -> ', $val, "\n";
  }
  print "\n";
}

sub horspool_test_02
{
  my $pat = 'abc';
  my $txt = 'abe abc efg';
  my %shift_tab = build_shift_table($pat);
  my $match_pos = horspool($pat, $txt, \%shift_tab);
  print $match_pos, "\n";
}

horspool_test_01();
horspool_test_02();

my $rumi_poem =
'\n
Late, by Myself\n
Late, by myself, in the boat of myself,\n
no light and no land anywhere,\n
cloudcover thick. I try to stay\n
just above the surface,\n
yet I\'m already under\n
and living with the ocean\n
\n
Mewlana Jalaluddin Rumi\n
';

sub horspool_test_03 
{
  my $pat = 'ocean';
  my %shift_table = build_shift_table($pat);
  print horspool($pat, $rumi_poem, \%shift_table), "\n";
}

horspool_test_03();

sub generic_horspool_test
{
  my ($pat, $text) = @_;
  my %shift_table = build_shift_table($pat);
  my $match_pos = horspool($pat, $text, \%shift_table);
  print "\$match_start\t==\t$match_pos\n";
  print "\$match_end\t==\t", $match_pos + length($pat) - 1,  "\n";
  print "matched text\t==\t", substr($text, $match_pos, length($pat)), "\n\n";
}


## Output
## $match_start    ==      8
## $match_end      ==      10
## matched text    ==      a c
generic_horspool_test('a c', 'abc efg a c klm!');

## Output
## $match_start    ==      200
## $match_end      ==      204
## matched text    ==      ocean
generic_horspool_test('ocean', $rumi_poem);

## Output
## $match_start    ==      200
## $match_end      ==      206
## matched text    ==      ocean\n
generic_horspool_test('ocean\n', $rumi_poem);

## Output
## $match_start    ==      160
## $match_end      ==      170
## matched text    ==      I'm already
generic_horspool_test('I\'m already', $rumi_poem);

## Output
## $match_start    ==      160
## $match_end      ==      206
## matched text    ==      I'm already under\n
## and living with the ocean\n
generic_horspool_test('I\'m already under\n
and living with the ocean\n', $rumi_poem);

