use strict;
use warnings;

sub square { return $_[0]**2; }
sub cube   { return $_[0]**3; }

sub x_square_plus_n {
  my $n = $_[0];
  return sub {
    return square($_[0]) + $n;
  }
}

sub x_cube_plus_n {
  my $n = $_[0];
  return sub {
    return cube($_[0]) + $n;
  }
}

print x_square_plus_n(10)->(2), "\n";
print x_cube_plus_n(10)->(2), "\n\n";

## 1^2 + 5 = 6
## 2^2 + 5 = 9
## 3^2 + 5 = 14
## 4^2 + 5 = 21
## 5^2 + 5 = 30
foreach(1..5) {
  print "$_^2 + 5 = ", x_square_plus_n(5)->($_), "\n";
}

## 1^3 + 5 = 6
## 2^3 + 5 = 13
## 3^3 + 5 = 32
## 4^3 + 5 = 69
## 5^3 + 5 = 130
foreach(1..5) {
  print "$_^3 + 5 = ", x_cube_plus_n(5)->($_), "\n";

}
