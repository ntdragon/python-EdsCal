#! perl -w

=pod
=head1 Header

     Name:    calen.pl
  Version:    1.0
     Date:    12/2001
   Author:    Edward Birdsall
  Language:   Perl

=head1 Introduction

This file contains a set of calendar routines used in various programs using the
Perl language.  I find that they come in handy so I develop them in the various
computer languages I wish to use for programming.  The Julian and Gregorian
calendars are the most commonly used and I have added Shire and Alt calendars
for variety.  I may add other calendars later as I get time and interest.

=head1 Notes

#23456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789-
#-------------------------------------------------------------------------------
=head2 internal time formats

These functions use Julian GMT time in the form ($year, $day, $secs) with
seconds in real form.  Time zones are in +/- seconds from 0 to 43200.

=head2 perl time functions of note

Greenwich Time functions

 ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = gmtime(time);
 timegm function use Time::Local;
 $time = timegm($sec, $min, $hour, $mday, $mon, $year);

Localtime functions
 ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
 timelocal function use Time::Local;
 $time = timelocal($sec, $min, $hour, $mday, $mon, $year);

The year 1900 == 0 and most of the variables are 0 indexed vice 1 indexed for
start

= head2 zone2zone

This function converts the time from one time zone to another.

=cut

sub zone2zone {
	my $secs = $time_zone + $secs;
     if (my $secs > 86400) {
          my $secs -= 86400;
          my $day  += 1;
     }
     elseif (my $secs < 0) {
          my $secs += 86400;
          my $day  -= 1;
     }
     maxdays = 365 = is_leap(my $year);
     if (my $days > maxdays) {
          my $days -= maxdays;
          my $year += 1;
     }
     elseif (my $days < 1) {
          my $days += maxdays;
          my $year -= 1;
}

=head2 gregorian2julian
sub gregorian2julian
sub julian2gregorain
sub gregoriandayofweek

=head1 Shire calendar routines

The Shire calendar found in J.R.Tolkein Ring series has twelve months of thirty
days with four days not in a month and one or two not in a month or week.  Each
year starts on 2Yule which is Sterrendei (equivalent to Saturday).  The year
pattern is 2Yule, 1-30 Afteryule, 1-30 Solmath, 1-30 Rethe, 1-30 Astron, 1-30
Thrimidge, 1-30 Forelithe, 1Lithe, [Midyear's Day, (Overlithe)], 2Lithe, 1-30
Afterlithe, 1-30 Wedmath, 1-30 Halimath, 1-30 Winterfilth, 1-30 Blotmath, 
1-30 Foreyule, 1Yule.  Overlithe added for leap years and Midyear's Day are not
part of any week.

Days of the week are; Sterrendei, Sunnendei, Momendei, Trewesdei,Hevenesdei,
Meresdei, and Highdei. 

=head2 shire2julian

This function converts the Shire calendar information back to Julian.

=cut

sub shire2julian

=head2 julian2shire
123456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789-
This converts a time from Julian to the Shire calendar.

=cut
sub julian2shire {
}

sub shire_dow {
}

=head1 Alt calendar

This calendar was proposed a while ago and I don't remmember all the details.
It has thirteen months of twenty eight days with MidDay between the fouteenth and
fifteenth day of the seventh month.  MidDay and LeapDay which is added on leap
years are not part of the week similar to the Shire Calendar.

=head1 Generic calendar routines

These routines apply to all calendars herein and are lumped here.

=head2 isleap

This subroutine determines if the year in question is a leap year.  The rule
applied is that leap years are every fourth year except century years unless
it is every fouth century.

=cut
sub isleap{
}

=head2 time2secs
=cut
sub time2secs {
}
sub secs2time {
}
sub 12convert24 {
}
sub 24convert12 {
}
sub deltadates {
}
sub datedelta {
}




