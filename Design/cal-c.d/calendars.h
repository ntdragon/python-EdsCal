/******************************************************************************/
/* Calendar.h                                                                 */
/*----------------------------------------------------------------------------*/
/* current v1.00 July 2004                                                    */
/*============================================================================*/
/*   Purpose                                                                  */
/*       This program is                                                      */
/*                                                                            */
/*                                                                            */
/* -------------------------------------------------------------------------- */
/*   Platform:  all                                                           */
/*----------------------------------------------------------------------------*/
/*   History                                                                  */
/*   -------                                                                  */

/******************************************************************************/

/******************************************************************************/
/*************************     #includes     **********************************/
/******************************************************************************/
#include ".h"

/******************************************************************************/
/*************************   typedef, define enum   ***************************/
/******************************************************************************/
struct edate {
     float   secs;    /* seconds from midnight  0->86399 */
     short   days;    /* days in year 1->365 or 366      */
     int     year;    /* year                            */
     float   zone;    /* time zone -12->+12              */
} edate;

struct gdate {
     float   secs;
     short   hour;
     short   day;
     int     year;
     float   zone;
} gdate;

struct date
	int month
	int day
	int year
end struct

struct edaet {        /* Internal Earth Date and Time GMT*/
    float   seconds;    /* seconds from midnight  0->86399 */
    short   days;    /* days in year 1->365 or 366      */
    int     year;    /* year  (Gregorian based)         */
} edaet;



struct gdates {                /* Gregorian Date - std 24hr clock */
     struct  etyme     tyme;   /* time of day - 24 hour clock */
     short   day;              /* day in month     1-31           */
     int     month;            /* month in year    1-12           */
     int     year;             /* year             +-nnnnn  CE    */
     float   zone;             /* local time zone  -12 -> + 12    */
     int     diwk;    /* day in week      1-7            */
} gdates;

struct gdatea {       /* Gregorian Date - angular 24hr clock */
	 struct  atyme     tyme;   /* time of day - angular clock */
    short   day;     /* day in month     1-31               */
    int     month;   /* month in year    1-12               */
    int     year;    /* year            +-nnnnn CE          */
    int     diwk;    /* day in week     1-7                 */
} gdatea;

struct hdates {       /* Hobbit Date - std 24hr clock */
	 struct  etyme     tyme;   /* time of day - 24 hour clock */
    short   day;     /* day in month     1-30           */
    int     month;   /* month in year    0-12           */
    int     year;    /* year             +-nnnnn  CE    */
    float   zone;    /* local time zone  -12 -> + 12    */
    int     diwk;    /* day in week      0-7            */
} hdates;

struct hdatea {       /* Hobbit Date - angular 24hr clock    */
	 struct  atyme     tyme;   /* time of day - angular clock */
    short   day;     /* day in month     1-30               */
    int     month;   /* month in year    0-12               */
    int     year;    /* year            +-nnnnn CE          */
    int     diwk;    /* day in week      0-7                */
} hdatea;
    
#define BackSize         50         /* size of backtrack buffer originally 20 */

/******************************************************************************/
/*************************   function prototypes    ***************************/
/******************************************************************************/

/* Public - used by other modules */
/*--------------------------------*/
/* Time */
/*------*/
int main( int argc, char **argv)
int time2zulu (edate itime, edate ftime&)
int zulu2time (edate itime, float newzone, edate ftime&)
int time2secs()
int secs2time ( )
int 12convert24()
int 24convert12()
int angular2zulu (edate itime, edate ftime)
int zulu2angular (edate itime, edate ftime)
int internal2Shire()
int dectime2internal
int Fixed2internal
int world2internal

    SecsTo24
    SecsTo12
    SecsTo10
    SecsFrom24
    SecsFrom12
    SecsFrom10

int Gregorian2Internal (gdate itime, edate tyme&)

/* Private - for use by this module only */
/*---------------------------------------*/

/******************************************************************************/
/*************************   function descriptions    *************************/
/******************************************************************************/

/******************************************************************************/
/*************************     Public functions       *************************/
/******************************************************************************/

/******************************************************************************/
/* module                                                                     */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version:                                                                   */
/* Author:                                                                    */
/* Date:                                                                      */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Operation:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/******************************************************************************/

/******************************************************************************/
/*************************    Private functions       *************************/
/******************************************************************************/




/******************************************************************************/
/* module                                                                     */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version:                                                                   */
/* Author:                                                                    */
/* Date:                                                                      */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Operation:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/******************************************************************************/


Calendar Program

This program has a number of different functions
     1) Convert between any two calendar systems that I know
     2) Display a calendar period (month, week, day) of a desired system
     3) Appointments
     4) Compute delta date/time



Calendar systems
     Julian
     Gregorian
     Shire
     'Scientific'-a
     Mars

Structures
     jdate - secs from midnight
             day from year start
             year
             time zone delta hour from Zulu



     

/* ===== * ===== * ===== * ===== ****** ===== * ===== * ===== * ===== * ===== */
/* Calendar systems                                                           */
/* ----------------                                                           */
/* Julian                                                                     */
/*       Year - Day - Time                                                    */
/*                                                                            */
/*     Year - could be Christian or some other - pick is Christian            */
/*     Day - First day of the year is 1 and then sequentially numbered till   */
/*           end of year                                                      */
/*     Time - Earth 24 hour day at Zulu (Greenwich Mean Time)                 */
/*            24 hours/day, 60 minutes/hour, 60 seconds/minute                */
/* ----- -----                                                                */
/* Gregorian                                                                  */
/*       Year - Month - Day of Month - Time - time zone - Day of Week         */
/*              This calendar was started in year      A.D. with a date shift */
/*                   from the existing calendar so need to put that in the    */
/*                   algorithm.                                               */
/*                                                                            */
/*       Year - Christian calendar wih A.D. and B.C.                          */
/*       Month - 12 months of varying days, second month changes number of    */
/*               days if leap year                                            */
/*            January-31, February-28?29, March-31, April-30, May-31, June-30 */
/*            July-31, August-31, September-30, October-31, November-30,      */
/*            December-31                                                     */
/*       Day of Month - see above for days in each month                      */
/*       Time - Earth 24 hour time                                            */
/*       Time Zone - ranges from -12 to +12 with 0 being Zulu                 */
/*       Day of Week - 7 days per week,  each year starts on a different day  */
/*            Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday  */
/* ----- -----                                                                */
/* Shire                                                                      */
/*       Year - Month - Day of Month - Time - time zone - Day of Week         */
/*                                                                            */
/*       Year - ?
/*       Month - 12 months of 30 days - 5 days not part of any month or week  */
/*            Afteryule, Solmath, Rethe, Astron, Thrimidge, Forelithe,        */
/*            Afterlithe, Wedmath, Halimath, Winterfilth, Blotmath, Foreyule  */
/*       Day of month - 1 to 30 with a few days not part of any month         */
/*       Time - Earth 24 hour time                                            */
/*       Time Zone - ranges from -12 to +12 with 0 being Zulu                 */
/*       Day of Week - 7 days per week, each year starts on Sterrendei        */
/*            Sterrendei, Sunnendei, Momendei, Trewesdei, Hevenesdei,         */
/*            Meresdei, Highdei                                               */
/*       Year's progression                                                   */
/*            2Yule, Afteryule, Solmath, Rethe, Astron, Thrimidge, Forelithe, */
/*            1Lithe,                                                         */
/*            Midyear's Day, (OverLithe), - these two are not part of the week*/
/*            2Lithe, Afterlithe, Wedmath, Halimath, Winterfilth, Blotmath,   */
/*            Foreyule, 1Yule                                                 */
/* ----- -----                                                                */
/* Scientific (International Fixed)
/*       Year - Month - Day of Month - Time - time zone - Day of Week         */
/*                                                                            */
/*       Year - ?
/*       Month - 13 months
/*       Day of month - 1 through 28 with MidDay and LeapDay not part of month*/ 
/*       Time - Earth 24 hour time                                            */
/*       Time Zone - ranges from -12 to +12 with 0 being Zulu                 */
/*       Day of Week - 7 days per week,  each year starts on Sunday           */
/*            Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday  */
/*            MidDay and LeapDay not part of any week                         */
/*            MidDay is in the 7th month between the 14th and 15th            */
/*            LeapDay is with MidDay on leap years                            */
/* ----- -----                                                                */
/* perpetual
/*       Year - Month - Day of Month - Time - time zone - Day of Week         */
/*                                                                            */
/*       Year - ?
/*       Month - 12 months 8-30 4-31 
/*       Day of month - 1 through 28 with MidDay and LeapDay not part of month*/ 
/*       Time - Earth 24 hour time                                            */
/*       Time Zone - ranges from -12 to +12 with 0 being Zulu                 */
/*       Day of Week - 7 days per week,  each year starts on Sunday           */
/*            Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday  */
/*            MidDay and LeapDay not part of any week                         */
/*            WorldDay is last day of year except every 4th year              */
/*            LeapDay is with MidDay on leap years                            */
/* ----- -----                                                                */
/* Mars1
/*  MDay = 24 hours, 39 minutes, 35 seconds of ETime
/*  MYear =  668.62... MDays    = 687 EDays

Structures
     jdate - secs from midnight
             day from year start
             year
             time zone delta hour from Zulu




Years divisible by 4 a leap year except divisible by 100 unless divisible by 400

**********************************************************************************    
Internal date:time format is Julian GMT -  year:day:sssss.sss
time zones internal ±sssss
/* */
sub time2zulu { }
/* This subroutine converts a zone julian date:time to zulu given original date:time and time zone
Algorithm:
	add time to original
	if time > 86400 then subtract 86400 from time and increment date
	if time < 0000 then add 2400 to time and decrement date
	if day > year's end then date=1 and increment year
	if day < 1 then day=1 and decrement year
/* */	
sub zulu2time { }
This subroutine converts a zulu date:time to zone given zulu date:time and time zone
Algorithm:
	subtract time from zulu
	if time > 2400 then subtract 2400 from time and increment date
	if time < 0000 then add 2400 to time and decrement date
	if day > year's end then date=1 and increment year
	if day < 1 then day=1 and decrement year
/* */
int Gregorian2Julian();
/* This subroutine converts a Gregorian date to a Julian date                */
Algorithm:
	Determine if leap year and use appropriate month set
	determine integer month
	return day = day of month plus sum of previous months

sub Julian2Gregorian { }
This subroutine converts a Julian date to a Gregorian date
Algorithm:
	Determine if leap year and use appropriate month set
	While day !inMonth increment month
	Return Gregorian Date
/* */
sub Shire2Julian { }
This subroutine converts a Shire date to a Julian date
Algorithm:
	If special day then set value and return day
	Determine if leap year and use appropriate year set
	determine integer month
	return day = day of month plus sum of previous months
/* */
sub Julian2Shire { }
This subroutine converts a Julian date to a Shire date
Algorithm:
	Determine if leap year and use appropriate year set
	If special day then return Shire date by table
	While day !inMonth increment Month
	return Shire date
/* */
sub ShireDayofWeek { }
This subroutine returns the number of the day of week 0:7 given a Shire date
Algorithm:
/* */
sub GregorianDayofWeek { }
This subroutine returns the number of the day of week 1:7 given a Gregorian Date
Algorithm:
/* */
sub isLeap { }
This returns True if LeapYear otherwise False
Algorithm:
	if year mod 4 ­ 0 then return False
	if year mod 4 = 0 and year mod 400 = 0 return True
	if year mod 4 = 0 and year mod 100 ­ 0 return True else False
/* */
sub time2secs { }
This subroutine converts 24 hour time to seconds from midnight
Algorithm:
/* */
sub secs2time ( )
This subroutine converts seconds from midnight to 24 hour time
Algorithm:
	ss.sss = secs mod 60
	hour = trunc(secs - ss.sss)/3600
	minutes = ((secs - ss.sss) - (hour*3600))/60
/* */
sub 12convert24
This sub converts a 24 hour time to 12 hour time
Algorithm:
	if hh < 13 return time + 'a.m.'
		else hh -= 12 and return time + 'p.m.'
/* */
sub 24convert12
This sub converts a 12 hour time to 24 hour time
Algorithm:
	if 'a.m.' return time else hh += 12 and return time
/* */
sub deltaDates
This subroutine determines the delta time between two dates
Algorithm
	Determine the greater date
	subtract from the greater date the lesser date
		subtract seconds and make necessary day corrections
		subtract days and make any necessarey year corrections
		subtract years
	return delta time

sub dateDelta
This subroutine computes the new date given the original date and delta time
Algorithm
	add delta time to date making corrections as necessary
	return new date
Calendar - c


/* */
int Gregorian_2_Julian(int month, int day, int year)

/* */
date Julian_2_Gregorian(int day, int year)


struct date
	int month
	int day
	int year
end struct

date Julian_2_Hobbit(int day, int year)
int Hobbit_2_Julian(int month, int day, int year)

int day_of_week_Gregorian(date)
int day_of_week_Hobbit(date)
int day_of_week_Julian(date)

Appointment_by_day()
Appointment_by_date()

Display_week
Display_day

Boolean isaLeapYear(int year)

*/
# calendar routines in C



struct edate {
     float   secs;    /* seconds from midnight  0->86399 */
     short   days;    /* days in year 1->365 or 366      */
     int     year;    /* year                            */
     float   zone;    /* time zone -12->+12              */
} edate;

struct gdate {
     float   secs;
     short   hour;
     short   day;
     int     year;
     float   zone;
} gdate;

     edate   itime,etime;
     
enum Gdow {Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday};
enum GMon {January, February, March, April, May, June, July, August, September, October, November, December}
enum Gry {31,28,31,30,31,30,31,31,30,31,30,31}
enum Gly {31,29,31,30,31,30,31,31,30,31,30,31}

}

int time2zulu (edate itime, edate ftime&);
.........1.........2.........3.........4.........5.........6.........7.........8
/* -------------------------------------------------------------------------- */
/* Convert a time from a local time zone to Greenwich Mean Time (Zulu)        */
/* v1.0 eab 12/2000                                                           */
/* Algorithm:                                                                 */
/*     First set the max number of days in the year by using isleap           */
/*     Now add the seconds for time zone correction to current seconds        */
/*     Now we do a series of checks to see if we changed to a different day   */
/*          If so we update the day and seconds, then see if that changes the */
/*          year and if so update the day and year accordingly                */
/* -------------------------------------------------------------------------- */

int zulu2time (edate itime, float newzone, edate ftime&);
/* -------------------------------------------------------------------------- */
/* Convert a Zulu time to anothor local time zone                             */
/* v1.0 eab 12/2000                                                           */
/* Algorithm:                                                                 */
/*     First set the max number of days in the year by using isleap           */
/*     Now subtract the seconds for time zone correction to current seconds   */
/*     Now we do a series of checks to see if we changed to a different day   */
/*          If so we update the day and seconds, then see if that changes the */
/*          year and if so update the day and year accordingly                */
/* -------------------------------------------------------------------------- */

int Gregorian2Julian (gdate itime, edate ftime&);
/* -------------------------------------------------------------------------- */
/* Convert a Gregorian date to a Julian date                                  */
/* v1.0 eab 12/2000                                                           */
/* Algorithm:                                                                 */
/*      First determine if the year is a leap year and set days/month array   */
/*                                                                            */

gdate Julian2Gregprium (edate itime)
{
}

edate Shire2Julian (sdate itime)
{
}

sdate Julian2Shire (edate itime)
{
}

string ShireDayofWeek()
string GregorianDayofWeek()

Boolean isleap(int year);
/* -------------------------------------------------------------------------- */
/* The algorithm used here is simplistic, refinement will be done later       */
/* Algorith:                                                                  */
/*      First return False for all years not divisible by 4                   */
/*            All years left are now evenly divisible by 4 so maybe leap year */
/*      Second return True for all years not divisible by 100                 */
/*            left is just the century years                                  */
/*      Return true if divisible by 400 otherwise return false                */
/* -------------------------------------------------------------------------- */

float secs2time()
float time2secs()
nn 12convert24
nn 24convert12
nn deltaDates(edate itime, edate ftyme)
Functions
     FromGregorian
     ToGregorian
     GregorianDayofWeek
     FromShire
     ToShire
     ShireDayofWeek
     
     SecsTo24
     SecsTo12
     SecsTo10
     SecsFrom24
     SecsFrom12
     SecsFrom10
     
     IsLeap
     DeltaDates
     Functions
     FromGregorian
     ToGregorian
     GregorianDayofWeek
     FromShire
     ToShire
     ShireDayofWeek
     
     SecsTo24
     SecsTo12
     SecsTo10
     SecsFrom24
     SecsFrom12
     SecsFrom10
     
     IsLeap
     DeltaDates
/******************************************************************************/
/*******************************   end   **************************************/
/******************************************************************************/

