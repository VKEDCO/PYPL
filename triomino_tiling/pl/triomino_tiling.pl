#!/usr/bin/perl

###################################################
## triomino_tiling.pl
##
## A Perl solution to the Triomino Tiling
## puzzle
##
## bugs to vladimir dot kulyukin at gmail dot com
###################################################

use strict;
use warnings;

my @board_22 =
(
 [0, 0],
 [0, 0]
);

my @board_44 = 
(
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]
);

my @board_88 = 
(
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]
);

my @board_1616 = 
(
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
);

sub display_board
{
  my ($board, $size) = @_;
  for(my $r = 0; $r < $size; $r++) {
    for(my $c = 0; $c < $size; $c++) {
      print $board->[$r]->[$c], "\t";
    }
    print "\n";
  }
  print "\n";
}

sub clear_board
{
  my ($board, $size) = @_;
  for(my $r = 0; $r < $size; $r++) {
    for(my $c = 0; $c < $size; $c++) {
      $board->[$r]->[$c] = 0;
    }
  }
}

sub mark_missing_tile
{
  my ($board, $tile_c, $tile_r, $mark) = @_;
  $board->[$tile_r]->[$tile_c] = $mark;
}

sub get_board_size
{
  my ($tlc, $tlr, $brc, $brr) = @_;
  my $hsize = ($brc - $tlc + 1);
  my $vsize = ($brr - $tlr + 1);
  ($hsize == $vsize) or die 'non square board';
  return $hsize;
}

sub get_quarter_coords 
{
  my ($tlc, $tlr, $brc, $brr, $qn) = @_;
  ($qn >= 1 && $qn <= 4) or die 'wrong quarter number';
  my $size = get_board_size($tlc, $tlr, $brc, $brr);
  my @coords = ();
  my $new_tlc;
  my $new_tlr;
  my $new_brc;
  my $new_brr;
  if ( $qn == 1 ) {
    $new_tlc = $tlc;
    $new_tlr = $tlr;
    $new_brc = $tlc + $size/2 - 1;
    $new_brr = $tlr + $size/2 - 1;
    push(@coords, $new_tlc);
    push(@coords, $new_tlr);
    push(@coords, $new_brc);
    push(@coords, $new_brr);
  }
  elsif ( $qn == 2 ) {
    $new_tlc = $tlc + $size/2;
    $new_tlr = $tlr;
    $new_brc = $tlc + $size - 1;
    $new_brr = $tlr + $size/2 - 1;
    push(@coords, $new_tlc);
    push(@coords, $new_tlr);
    push(@coords, $new_brc);
    push(@coords, $new_brr);    
  }
  elsif ( $qn == 3 ) {
    $new_tlc = $tlc + $size/2;
    $new_tlr = $tlr + $size/2;
    $new_brc = $tlc + $size - 1;
    $new_brr = $tlr + $size - 1;    
    push(@coords, $new_tlc);
    push(@coords, $new_tlr);
    push(@coords, $new_brc);
    push(@coords, $new_brr);    
  }
  elsif ( $qn == 4 ) {
    $new_tlc = $tlc;
    $new_tlr = $tlr + $size/2;
    $new_brc = $tlc + $size/2 - 1;
    $new_brr = $tlr + $size - 1;    
    push(@coords, $new_tlc);
    push(@coords, $new_tlr);
    push(@coords, $new_brc);
    push(@coords, $new_brr);    
  }
  return \@coords;
}

sub get_missing_tile_quarter
{
  my ($tlc, $tlr, $brc, $brr, $tile_c, $tile_r) = @_;
  my $qtlc; my $qtlr; my $qbrc; my $qbrr;
  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 1)};
  if ( $tile_c >= $qtlc && $tile_c <= $qbrc &&
       $tile_r >= $tlr && $tile_r <= $qbrr ) {
    return 1;
  }

  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 2)};
  if ( $tile_c >= $qtlc && $tile_c <= $qbrc &&
       $tile_r >= $tlr && $tile_r <= $qbrr ) {
    return 2;
  }

  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 3)};
  if ( $tile_c >= $qtlc && $tile_c <= $qbrc &&
       $tile_r >= $tlr && $tile_r <= $qbrr ) {
    return 3;
  }

  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 4)};
  if ( $tile_c >= $qtlc && $tile_c <= $qbrc &&
       $tile_r >= $tlr && $tile_r <= $qbrr ) {
    return 4;
  }

  return -1;
}

sub place_triomino_123
{
  my ($board, $tlc, $tlr, $brc, $brr, $tile_mark) = @_;
  my $qtlc; my $qtlr; my $qbrc; my $qbrr;
  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 1)};
  $board->[$qbrr]->[$qbrc] = $tile_mark;

  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 2)};
  $board->[$qbrr]->[$qtlc] = $tile_mark;
  
  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 3)};
  $board->[$qtlr]->[$qtlc] = $tile_mark;
}

sub place_triomino_234
{
  my ($board, $tlc, $tlr, $brc, $brr, $tile_mark) = @_;
  my $qtlc; my $qtlr; my $qbrc; my $qbrr;
  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 2)};
  $board->[$qbrr]->[$qtlc] = $tile_mark;

  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 3)};
  $board->[$qtlr]->[$qtlc] = $tile_mark;
  
  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 4)};
  $board->[$qtlr]->[$qbrc] = $tile_mark;
}

sub place_triomino_341
{
  my ($board, $tlc, $tlr, $brc, $brr, $tile_mark) = @_;
  my $qtlc; my $qtlr; my $qbrc; my $qbrr;
  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 3)};
  $board->[$qtlr]->[$qtlc] = $tile_mark;

  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 4)};
  $board->[$qtlr]->[$qbrc] = $tile_mark;
  
  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 1)};
  $board->[$qbrr]->[$qbrc] = $tile_mark;
}

sub place_triomino_412
{
  my ($board, $tlc, $tlr, $brc, $brr, $tile_mark) = @_;
  my $qtlc; my $qtlr; my $qbrc; my $qbrr;

  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 4)};
  $board->[$qtlr]->[$qbrc] = $tile_mark;
  
  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 1)};
  $board->[$qbrr]->[$qbrc] = $tile_mark;

  ($qtlc, $qtlr, $qbrc, $qbrr) = 
    @{get_quarter_coords($tlc, $tlr, $brc, $brr, 2)};
  $board->[$qbrr]->[$qtlc] = $tile_mark;
}

my $tile_num = 1;
sub tile_board_with_triominos {
  my ($board, $tile_c, $tile_r) = @_;
  my @board_ary = @{ $board };
  my $last_index = $#board_ary;
  (($last_index+1) % 2 == 0) or die 'board size must be even and > 0';
  mark_missing_tile($board, $tile_c, $tile_r, '?');
  $tile_num = 1;
  display_board($board, $last_index+1);
  tile_board_with_triominos_aux($board, 0, 0, 
				$last_index, $last_index, 
				$tile_c, $tile_r,
				$last_index+1);
}

sub tile_board_with_triominos_aux
{
  my ($board, $tlc, $tlr, $brc, $brr, $tile_c, $tile_r, $orig_size) = @_;
  ## print "current board $tlc $tlr $brc $brr\n";
  my $qn = get_missing_tile_quarter($tlc, $tlr, $brc, $brr, $tile_c, $tile_r);
  ## print "\nmissing tile in quarter $qn\n\n";
  ($qn != -1 ) or die 'Unknown quarter of missing tile';
  my $size = get_board_size($tlc, $tlr, $brc, $brr);
  ##display_board($board, $orig_size);
  if ( $qn == 1 ) {
    place_triomino_234($board, $tlc, $tlr, $brc, $brr, $tile_num);
    $tile_num += 1;
    display_board($board, $orig_size);    
    if ( $size == 2 ) {
      return;
    }
    else {
      my ($tlc1, $tlr1, $brc1, $brr1) 
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 1)};
      #print "$tlc1 $tlr1 $brc1 $brr1\n";
      tile_board_with_triominos_aux($board, $tlc1, $tlr1, $brc1, $brr1,
				   $tile_c, $tile_r, 
				   $orig_size);
      my ($tlc2, $tlr2, $brc2, $brr2) 
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 2)};
      #print "$tlc2 $tlr2 $brc2 $brr2\n";
      tile_board_with_triominos_aux($board, $tlc2, $tlr2, $brc2, $brr2,
				   $tlc2, $brr2, 
				   $orig_size);

      my ($tlc3, $tlr3, $brc3, $brr3)
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 3)};
      #print "$tlc3 $tlr3 $brc3 $brr3\n";
      tile_board_with_triominos_aux($board, $tlc3, $tlr3, $brc3, $brr3,
				   $tlc3, $tlr3, 
				   $orig_size);

      my ($tlc4, $tlr4, $brc4, $brr4)
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 4)};
      #print "$tlc4 $tlr4 $brc4 $brr4\n";
      tile_board_with_triominos_aux($board, $tlc4, $tlr4, $brc4, $brr4,
				   $brc4, $tlr4, 
				   $orig_size);
    }
  }      
  elsif ( $qn == 2 ) {
    place_triomino_341($board, $tlc, $tlr, $brc, $brr, $tile_num);
    $tile_num += 1;
    display_board($board, $orig_size);
    if ( $size == 2 ) {
      return;
    }
    else {
      my ($tlc1, $tlr1, $brc1, $brr1) 
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 1)};
      tile_board_with_triominos_aux($board, $tlc1, $tlr1, $brc1, $brr1,
				   $brc1, $brr1, 
				   $orig_size);

      my ($tlc2, $tlr2, $brc2, $brr2) 
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 2)};
      tile_board_with_triominos_aux($board, $tlc2, $tlr2, $brc2, $brr2,
				   $tile_c, $tile_r, 
				   $orig_size);

      my ($tlc3, $tlr3, $brc3, $brr3)
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 3)};
      tile_board_with_triominos_aux($board, $tlc3, $tlr3, $brc3, $brr3,
				   $tlc3, $tlr3, 
				   $orig_size);

      my ($tlc4, $tlr4, $brc4, $brr4)
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 4)};
      tile_board_with_triominos_aux($board, $tlc4, $tlr4, $brc4, $brr4,
				   $brc4, $tlr4, 
				   $orig_size);
    }
  }      
  elsif ( $qn == 3 ) {
    place_triomino_412($board, $tlc, $tlr, $brc, $brr, $tile_num);
    $tile_num += 1;
    display_board($board, $orig_size);
    if ( $size == 2 ) {
      return;
    }
    else {
      my ($tlc1, $tlr1, $brc1, $brr1) 
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 1)};
      tile_board_with_triominos_aux($board, $tlc1, $tlr1, $brc1, $brr1,
				   $brc1, $brr1, 
				   $orig_size);

      my ($tlc2, $tlr2, $brc2, $brr2) 
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 2)};
      tile_board_with_triominos_aux($board, $tlc2, $tlr2, $brc2, $brr2,
   				   $tlc2, $brr2, 
				   $orig_size);

      my ($tlc3, $tlr3, $brc3, $brr3)
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 3)};
      tile_board_with_triominos_aux($board, $tlc3, $tlr3, $brc3, $brr3,
				   $tile_c, $tile_r, 
				   $orig_size);

      my ($tlc4, $tlr4, $brc4, $brr4)
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 4)};
      tile_board_with_triominos_aux($board, $tlc4, $tlr4, $brc4, $brr4,
				   $brc4, $tlr4, 
				   $orig_size);
    }
  }      
  elsif ( $qn == 4 ) {
    place_triomino_123($board, $tlc, $tlr, $brc, $brr, $tile_num);
    $tile_num += 1;
    display_board($board, $orig_size);
    if ( $size == 2 ) {
      return;
    }
    else {
      my ($tlc1, $tlr1, $brc1, $brr1) 
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 1)};
      tile_board_with_triominos_aux($board, $tlc1, $tlr1, $brc1, $brr1,
				   $brc1, $brr1, 
				   $orig_size);

      my ($tlc2, $tlr2, $brc2, $brr2) 
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 2)};
      tile_board_with_triominos_aux($board, $tlc2, $tlr2, $brc2, $brr2,
      				   $tlc2, $brr2, 
				   $orig_size);

      my ($tlc3, $tlr3, $brc3, $brr3)
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 3)};
      tile_board_with_triominos_aux($board, $tlc3, $tlr3, $brc3, $brr3,
				   $tlc3, $tlr3, 
				   $orig_size);

      my ($tlc4, $tlr4, $brc4, $brr4)
	= @{get_quarter_coords($tlc, $tlr, $brc, $brr, 4)};
      tile_board_with_triominos_aux($board, $tlc4, $tlr4, $brc4, $brr4,
				   $tile_c, $tile_r, 
				   $orig_size);
    }
  }      
  else {
    die 'Unknown quarter of missing tile';
  }
}

######################### TESTS on 2x2 BOARD ##############################

sub test_22_01 {
  print 'TEST 2x2 01', "\n\n";
  tile_board_with_triominos(\@board_22, 0, 0);
  clear_board(\@board_22, 2);
}

sub test_22_02 {
  print 'TEST 2x2 02', "\n\n";
  tile_board_with_triominos(\@board_22, 1, 0);
  clear_board(\@board_22, 2);
}

sub test_22_03 {
  print 'TEST 2x2 03', "\n\n";
  tile_board_with_triominos(\@board_22, 1, 1);
  clear_board(\@board_22, 2);
}

sub test_22_04 {
  print 'TEST 2x2 04', "\n\n";
  tile_board_with_triominos(\@board_22, 0, 1);
  clear_board(\@board_22, 2);
}


#test_22_01();
#test_22_02();
#test_22_03();
#test_22_04();

######################## TESTS on 4x4 BOARD ##############################

sub test_44_01 {
  print 'TEST 4x4 01', "\n\n";
  tile_board_with_triominos(\@board_44, 0, 1);
  clear_board(\@board_44, 4);
}

sub test_44_02 {
  print 'TEST 4x4 02', "\n\n";
  tile_board_with_triominos(\@board_44, 0, 0);
  clear_board(\@board_44, 4);
}

sub test_44_03 {
  print 'TEST 4x4 03', "\n\n";
  tile_board_with_triominos(\@board_44, 2, 1);
  clear_board(\@board_44, 4);
}

sub test_44_04 {
  print 'TEST 4x4 04', "\n\n";
  tile_board_with_triominos(\@board_44, 2, 1);
  clear_board(\@board_44, 4);
}

sub test_44_05 {
  print 'TEST 4x4 05', "\n\n";
  tile_board_with_triominos(\@board_44, 3, 3);
  clear_board(\@board_44, 4);
}

sub test_44_06 {
  print 'TEST 4x4 06', "\n\n";
  tile_board_with_triominos(\@board_44, 0, 3);
  clear_board(\@board_44, 4);
}

sub test_44_07 {
  print 'TEST 4x4 07', "\n\n";
  tile_board_with_triominos(\@board_44, 3, 3);
  clear_board(\@board_44, 4);
}

#test_44_01();
#test_44_02();
#test_44_03();
#test_44_04();
#test_44_05();
#test_44_07();

######################## TESTS on 8x8 BOARD ##############################

sub test_88 {
  my ($tile_c, $tile_r) = @_;
  print 'TEST 8x8 ', 'missing tile at ', $tile_c, ' ', $tile_r, "\n";
  tile_board_with_triominos(\@board_88, $tile_c, $tile_r);
  clear_board(\@board_88, 8);
}

sub run_tests_88 {
  for(my $tile_c = 0; $tile_c < 8; $tile_c++) {
    for(my $tile_r = 0; $tile_r < 8; $tile_r++) {
      test_88($tile_c, $tile_r);
    }
  }
}

## test_88(0, 0);
## test_88(1, 1)
## run_tests_88();

######################## TESTS on 16x16 BOARD ##############################

sub test_1616 {
  my ($tile_c, $tile_r) = @_;
  print 'TEST 16x16 ', 'missing tile at ', $tile_c, ' ', $tile_r, "\n";
  tile_board_with_triominos(\@board_1616, $tile_c, $tile_r);
  clear_board(\@board_1616, 16);
}

sub run_tests_1616 {
  for(my $tile_c = 0; $tile_c < 16; $tile_c++) {
    for(my $tile_r = 0; $tile_r < 16; $tile_r++) {
      test_1616($tile_c, $tile_r);
    }
  }
}

## run_tests_1616();




