#!/usr/bin/perl

##########################################################################################
## A solution to the hyperlink element extraction problem
## at http://www.vkedco.blogspot.com/2013/02/python-perl-html-hyperlink-parsing-with.html
##
## bugs to vladimir dot kulyukin at gmail dot com
##########################################################################################

use strict;
use warnings;

## regex that matches any non empty sequence of characters
my $non_empty_txt_re = '.+';

## test hyperlink strings
my @hyperlinks = 
(
 '<a href="/wiki/State_highway">state highway</a>',
 '<a href="/wiki/State_highway" title="State highway">state highway</a>', 
 '<a href="/wiki/Interstate_84_(Utah)" title="Interstate 84 (Utah)" class="mw-redirect">Interstate 84</a>',
 '<a href="/wiki/Interstate_84_(Utah)" title="Interstate 84 (Utah)" class="mw-redirect">Interstate 84</a>',
 '<a href="/wiki/U.S._Route_89_(Utah)" title="U.S. Route 89 (Utah)" class="mw-redirect">U.S. Route 89</a>',
 '<a href="/wiki/Nevada" title="Nevada">Nevada</a>',
 '<a href="/wiki/Wyoming" title="Wyoming">Wyoming</a>',
 '<a href="/wiki/First_Transcontinental_Railroad" title="First Transcontinental Railroad">First Transcontinental Railroad</a>',
 '<a href="/wiki/California_Trail" title="California Trail">California Trail</a>',
 '<a href="/wiki/Bear_Lake_(Utah-Idaho)" title="Bear Lake (Utah-Idaho)" class="mw-redirect">Bear Lake</a>',
 '<a href="/wiki/Utah_Scenic_Byways" title="Utah Scenic Byways">Utah Scenic Byways</a>',
 '<a href="/wiki/Interstate_70_in_Utah" title="Interstate 70 in Utah">I-70</a>',
 '<a href="/wiki/Utah_State_Route_72" title="Utah State Route 72">SR-72</a>',
 '<a href="#cite_note-5"><span>[</span>5<span>]</span></a>',
 '<a href="/wiki/Huntington_State_Park" title="Huntington State Park">Huntington State Park</a>',
 '<a href="/wiki/Price,_Utah" title="Price, Utah">Price</a> at <a href="/wiki/Utah_State_Route_55" title="Utah State Route 55">SR-55</a>',
 '<a href="/wiki/U.S._Route_6_(Utah)" title="U.S. Route 6 (Utah)" class="mw-redirect">US-6</a>',
 '<a href="/wiki/U.S._Route_50_(Utah)" title="U.S. Route 50 (Utah)" class="mw-redirect">/50</a>'
);

################## Hyperlink's Name ############################################

## regex for a hyperlink's name
my $name_re = '<a\s+(?:' .$non_empty_txt_re. ')>(' .$non_empty_txt_re. ')<\/a>'; 

## sub that extracts the name of a hyperlink from a string using $name_re.
## if there is a match, it returns a list of attribute/value pair ('name', <extracted match>).
sub get_hyperlink_name {
  my $txt = shift();
  my @matches = $txt =~ /$name_re/;
  if ( @matches ) {
    return ('name', $matches[0]);
  }
  else {
    return ();
  }
}

################## Hyperlink's Class ############################################

## regex for a hyperlink's class
my $class_re = 'class=\"(' .$non_empty_txt_re. ')\"';

## sub that extracts the class of a hyperlink from a string using $name_re.
## if there is a match, it returns a list of attribute/value pair ('class', <extracted match>).
sub get_hyperlink_class {
  my $txt = shift();
  my @matches = $txt =~ /$class_re/;

  if ( @matches ) {
    return ('class', $matches[0]);
  }
  else {
    return ();
  }
}

############################ Hyperlink's Title ###############################

## regex for a hyperlink's title
my $title_re = 'title=\"(' .$non_empty_txt_re. ')\"\s+';

## sub that extracts the title of a hyperlink from a string using $title_re.
## if there is a match, it returns a list of attribute/value pair ('title', <extracted match>).
sub get_hyperlink_title {
  my $txt = shift();
  my @matches = $txt =~ /$title_re/;
  
  if ( @matches ) {
    return ('title', $matches[0]);
  }
  else {
    return ();
  }
}

############################ Hyperlink's Elements ###############################

## use the three subs above to extract all elements of a hyperlink.

sub get_hyperlink_elements {
  my $txt = $_[0];
  my @rslt = ();
  my @name_pair = get_hyperlink_name($txt);
  my @title_pair = get_hyperlink_title($txt);
  my @class_pair = get_hyperlink_class($txt);
  
  if ( @name_pair  ) { push(@rslt, \@name_pair); }
  if ( @title_pair ) { push(@rslt, \@title_pair); }
  if ( @class_pair ) { push(@rslt, \@class_pair); }

  return @rslt;
}

############################ TESTS ###############################

sub print_matches {
  print "$_ " foreach(@_);
  print "\n";
}

## take a list of strings and an element extract function
## and test the function on each string.,
sub test_hyperlink_extractor {
  my ($links, $extractor) = @_;
  foreach ( @{$links} ) {
    print "$_\n";
    my @matches = $extractor->($_);
    if ( @matches ) {
      print_matches(@matches);
    } 
    else {
      print 'no matches found', "\n";
    }
  }
}

##test_hyperlink_extractor(\@hyperlinks, \&get_hyperlink_name);
##test_hyperlink_extractor(\@hyperlinks, \&get_hyperlink_class);
##test_hyperlink_extractor(\@hyperlinks, \&get_hyperlink_title);

foreach ( @hyperlinks ) {
  print "$_\n";
  my @matches = get_hyperlink_elements($_);
  if ( @matches ) {
    for(my $i = 0; $i <= $#matches; $i++) {
	print $matches[$i]->[0], ' ', $matches[$i]->[1], "\n";
    }
  } 
  else {
    print 'no matches found', "\n";
  }
}

## Here is the output as a here-doc
<<OUTPUT
<a href="/wiki/State_highway">state highway</a>
name state highway
<a href="/wiki/State_highway" title="State highway">state highway</a>
name state highway
<a href="/wiki/Interstate_84_(Utah)" title="Interstate 84 (Utah)" class="mw-redirect">Interstate 84</a>
name Interstate 84
title Interstate 84 (Utah)
class mw-redirect
<a href="/wiki/Interstate_84_(Utah)" title="Interstate 84 (Utah)" class="mw-redirect">Interstate 84</a>
name Interstate 84
title Interstate 84 (Utah)
class mw-redirect
<a href="/wiki/U.S._Route_89_(Utah)" title="U.S. Route 89 (Utah)" class="mw-redirect">U.S. Route 89</a>
name U.S. Route 89
title U.S. Route 89 (Utah)
class mw-redirect
<a href="/wiki/Nevada" title="Nevada">Nevada</a>
name Nevada
<a href="/wiki/Wyoming" title="Wyoming">Wyoming</a>
name Wyoming
<a href="/wiki/First_Transcontinental_Railroad" title="First Transcontinental Railroad">First Transcontinental Railroad</a>
name First Transcontinental Railroad
<a href="/wiki/California_Trail" title="California Trail">California Trail</a>
name California Trail
<a href="/wiki/Bear_Lake_(Utah-Idaho)" title="Bear Lake (Utah-Idaho)" class="mw-redirect">Bear Lake</a>
name Bear Lake
title Bear Lake (Utah-Idaho)
class mw-redirect
<a href="/wiki/Utah_Scenic_Byways" title="Utah Scenic Byways">Utah Scenic Byways</a>
name Utah Scenic Byways
<a href="/wiki/Interstate_70_in_Utah" title="Interstate 70 in Utah">I-70</a>
name I-70
<a href="/wiki/Utah_State_Route_72" title="Utah State Route 72">SR-72</a>
name SR-72
<a href="#cite_note-5"><span>[</span>5<span>]</span></a>
name ]</span>
<a href="/wiki/Huntington_State_Park" title="Huntington State Park">Huntington State Park</a>
name Huntington State Park
<a href="/wiki/Price,_Utah" title="Price, Utah">Price</a> at <a href="/wiki/Utah_State_Route_55" title="Utah State Route 55">SR-55</a>
name SR-55
title Price, Utah">Price</a> at <a href="/wiki/Utah_State_Route_55
<a href="/wiki/U.S._Route_6_(Utah)" title="U.S. Route 6 (Utah)" class="mw-redirect">US-6</a>
name US-6
title U.S. Route 6 (Utah)
class mw-redirect
<a href="/wiki/U.S._Route_50_(Utah)" title="U.S. Route 50 (Utah)" class="mw-redirect">/50</a>
name /50
title U.S. Route 50 (Utah)
class mw-redirect
OUTPUT
