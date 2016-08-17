#!/usr/bin/perl
use 5.010;
use strict;
use warnings;

my $comp_num = int rand(200);
my $user_num;
my $bool = 0;

print "Computer zagadal chislo ot 0 do 200, poprobuite ygadat ego. \n";

while ($bool == 0) {
	print "\nVvedite 4islo: ";
	$user_num = <STDIN>;
	chomp($user_num);
	if ($comp_num == $user_num) {
		$bool = 1;
		print "Vu ygadali!\n";
	} elsif ($comp_num < $user_num) {
		print "Ne ygadali, Zagadannoe 4islo menwe 4em vawe.\n";
	} elsif ($comp_num > $user_num) {
        	print "Ne ygadali, Zagadannoe 4islo bolwe 4em vawe.\n";
	}
}

