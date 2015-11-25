#!/usr/bin/perl

## @author: vladimir kulyukin

package WebLogEntry;

use lib 'C:/Users/Vladimir/programming/nasa_wlog/pl_nasa_wlog/';

use strict;
use warnings;
use Timestamp;

sub new {
    my $self = {
	mIP          => '',
	mTimestamp   => '',
	mMethod      => '',
	mURL         => '',
	mProtocol    => '',
	mStatusCode  => 0,
	mTransBytes  => 0
    };
    bless($self);
    return $self;
}

sub make {
    my ($type, $ip, $tm_stamp, $method, $url, $protocol, $status_code, $trans_bytes) = @_;
    my $self = {
	mIP         => $ip,
	mTimeStamp  => Timestamp->toTimestamp($tm_stamp),
	mMethod     => $method,
	mURL        => $url,
	mProtocol   => $protocol,
	mStatusCode => int($status_code),
	mTransBytes => int($trans_bytes)
    };
    bless($self);
}

## two regular expressions to extract infrom from text web log entries
my $web_log_entry_pat = '^([\d\.\W\w-]+)\s+(- -)\s+\[(.+)\]\s+\"(.+)\s+(.+)\s+(.+)\"\s+(\d+)\s+((\d+)|(-))$';
my $web_log_entry_pat2 = '^([\d\.\W\w-]+)\s+(- -)\s+\[(.+)\]\s+\"(.+)\s+(.+)"\s+(\d+)\s+((\d+)|(-))$';

sub toWebLogEntry {
    my ($type, $str) = @_;
    if ( $str =~ /$web_log_entry_pat/ ) {
	my $trbytes = ($8 eq '-')? 0: int($8);
	my $self = {
	    mIP         => $1,
	    mTimestamp  => Timestamp->toTimestamp($3),
	    mMethod     => $4,
	    mURL        => $5,
	    mProtocol   => $6,
	    mStatusCode => int($7),
	    mTransBytes => $trbytes
	};
	bless($self);
	return $self;
    }
    elsif ( $str =~ /$web_log_entry_pat2/ ) {
	my $trbytes = ($7 eq '-')? 0: int($7);
	my $self = {
	    mIP => $1,
	    mTimestamp => Timestamp->toTimestamp($3),
	    mMethod => $4,
	    mURL => $5,
	    mProtocol => 'UNKNOWN',
	    mStatusCode => int($6),
	    mTransBytes => $trbytes
	};
	bless($self);
	return $self;
    }
    else {
	return 0;
    }
}

### ==========  Getters & Setters =================

sub getIP { 
    my $self = shift(); 
    return $self->{ mIP }; 
}
sub setIP {
  if ( @_ == 2 ) {
    my ($this, $ip) = @_;
    $this->{ mIP } = $ip;
  }
  else {
    die 'method $WebLogEntry->setIP(ip) takes 2 arguments';
  }
}

sub getMethod { 
    my $self = shift();
    return $self->{ mMethod };
}
sub setMethod {
    if ( @_ == 2 ) {
	my ($this, $method) = @_;
	$this->{ mMethod } = $method;
    }
    else {
	die 'method $WebLogEntry->setMethod(method) takes 2 arguments';
    }
}

sub getTimestamp {
    my $self = shift();
    return $self->{ mTimestamp };
}
sub setTimestamp {
    if ( @_ == 2 ) {
	my ($this, $tm) = @_;
	$this->{ mTimestamp } = $tm;
    }
    else {
	die 'method $WebLogEntry->setTimestamp(timestamp) takes 2 arguments';
    }
}

sub getURL {
    my $self = shift();
    return $self->{ mURL };
}
sub setURL {
    if ( @_ == 2 ) {
	my ($this, $url) = @_;
	$this->{ mURL } = $url;
    }
    else {
	die 'method $WebLogEntry->setURL(url) takes 2 arguments';
    }
}

sub getProtocol {
    my $self = shift();
    return $self->{ mProtocol };
}
sub setProtocol {
    if ( @_ == 2 ) {
	my ($this, $prt) = @_;
	$this->{ mProtocol } = $prt;
    }
    else {
	die 'method $WebLogEntry->setProtocol(prt) takes 2 arguments';
    }
}

sub getStatusCode {
    my $self = shift();
    return $self->{ mStatusCode };
}
sub setStatusCode {
    if ( @_ == 2 ) {
	my ($this, $code) = @_;
	$this->{ mStatusCode } = $code;
    }
    else {
	die 'method $WebLogEntry->setStatusCode(prt) takes 2 arguments';
    }
}

sub getTransBytes {
    my $self = shift();
    return $self->{ mTransBytes };
}
sub setTransBytes {
    if ( @_ == 2 ) {
	my ($this, $trbytes) = @_;
	$this->{ mTransBytes } = $trbytes;
    }
    else {
	die 'method $WebLogEntry->setTransBytes(trbytes) takes 2 arguments';
    }
}

## convert a WebLogEntry object and convert it into an HTML text.
sub toHtmlUL {
    my $self = shift();
    my $html_ul = "<UL>\n";
    $html_ul = $html_ul . '<li>' . 'IP:       ' . $self->getIP() . '</li>' . "\n";
    $html_ul = $html_ul . '<li>' . 'TIME:     ' . $self->getTimestamp()->toString() . '</li>' . "\n";
    $html_ul = $html_ul . '<li>' . 'METHOD:   ' . $self->getMethod() . '</li>' . "\n";
    $html_ul = $html_ul . '<li>' . 'URL:      ' . $self->getURL()    . '</li>' . "\n";
    $html_ul = $html_ul . '<li>' . 'PROTOCOL: ' . $self->getProtocol()    . '</li>' . "\n";
    $html_ul = $html_ul . '<li>' . 'STATUS:   ' . $self->getStatusCode()    . '</li>' . "\n";
    $html_ul = $html_ul . '<li>' . 'BYTES:    ' . $self->getTransBytes()    . '</li>' . "\n";
    $html_ul = $html_ul . '</UL>' . "\n";
    return $html_ul;
}

1;
