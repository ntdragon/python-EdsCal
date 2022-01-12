/******************************************************************************/
/* Main.c                                                                     */
/* -------------------------------------------------------------------------- */
/* Version:                                                                   */
/*
Calendar Program

Calendar structure
	date & time start
	date and time end
	duration
	location - ?URL to location map
	originator
	invitees
	invitees status
	description/agenda
	date&time created
	frequency - interval and end criteria??
	
Inputs
	Mnaual
	Calendar invite
	
Internal calendar used is Gegorian year UTC 
     year:Day in year: Seconds from midnight to milliseconds as of the GMT(UTC) time zone
     time zones in seconds offset
	
*******************************************************************************
*Calendar Program / Script
*
*******************************************************************************
*Main
*-----
* See what was passed as arguements and then do it
*	Options
*   -------
*   day print - then exit
*   input calendar invite then exit
*   engage graphical user interface
* exit
*******************************************************************************
*Day Print
*----------
* Input Calendar(s)
* Determine day schedule and which calendars to print
* Print calendar
* Exit
*******************************************************************************
* Calendar invite input
*----------------------
* Input invite
* Input calendars
* Add invite to appropriate calendar
* ouptput updated calendar
* exit
*******************************************************************************
/******************************************************************************/

/******************************************************************************/
/********************              #includes               ********************/
/******************************************************************************/

/******************************************************************************/
/********************     the functions themselves         ********************/
/******************************************************************************/

/* ********** ********** ********** ********** ********** ********** */

/******************************************************************************/
/********************               end                    ********************/
/******************************************************************************/
# calendar routines in C

int main( int argc, char **argv)
{
     /* a few variables defined here */
     BOOL   done  FALSE;

     /* initialize the machine */
     
     /* initialize graphics */
     
     /* opening screen */
     
     /* where do we go from here */

     /* Main Loop */
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


struct edaet {        /* Internal Earth Date and Time GMT*/
    float   seconds;    /* seconds from midnight  0->86399 */
    short   days;    /* days in year 1->365 or 366      */
    int     year;    /* year  (Gregorian based)         */
} edaet;

struct etyme {        /* standard 24 hour Earth Clock    */
	float    seconds;    /* 0-59 seconds in current minute  */
	short    minutes;    /* 0-59 minutes in current hour    */
	short    hour;    /* 0-23 hour in current day        */
} etyme;

struct atyme {        /* angular Earth Clock    */
	float    arc_seconds;    /* 0-59 seconds in current minute  */
	short    arc_minutes;    /* 0-59 minutes in current hour    */
	short    degrees; /* 0-359 degree in current day     */
} atyme;

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
    
enum Gdow {Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday};
enum GMon {January, February, March, April, May, June, July, August, September, October, November, December}
enum Gry {31,28,31,30,31,30,31,31,30,31,30,31}
enum Gly {31,29,31,30,31,30,31,31,30,31,30,31}

struct date
	int month
	int day
	int year
end struct

     edate   itime, etime;

     exit(0);
}

int time2zulu (edate itime, edate ftime&)
/* -------------------------------------------------------------------------- */
/* Convert a time from a local time zone to Greenwich Mean Time (Zulu)(UTC)   */
/* v1.0 eab 12/2000                                                           */
/* Algorithm:                                                                 */
/*     First set the max number of days in the year by using isleap           */
/*     Now add the seconds for time zone correction to current seconds        */
/*     Now we do a series of checks to see if we changed to a different day   */
/*          If so we update the day and seconds, then see if that changes the */
/*          year and if so update the day and year accordingly                */
/*        if time > 86400 then subtract 86400 from time and increment date    */
/*        if time < 0000 then add 2400 to time and decrement date             */
/*        if day > year's end then date=1 and increment year                  */
/*        if day < 1 then day=maxdays and decrement year                      */
/* -------------------------------------------------------------------------- */
{
     edate    tyme;
     int      maxdays;
     int      errNum = 0;
     float    secs_per_day=24.0*60.0*60.0;

     isleap(itime.year) ? maxdays = 366 : maxdays = 365;
     tyme.secs = itime.secs + (itime.zone * 3600)
     if (tyme.secs > (secs_per_day - 1) */
       {
          tyme.secs -= secs_per_day;
          tyme.days += 1;
       }
     else
     if (tyme.secs < 0)  /* before midnight */
       {
          tyme.secs += secs_per_day;
          tyme.days -= 1;
       }
     if (tyme.days > maxdays)   /* next year */
       {
          tyme.days -= maxdays;
          tyme.year += 1;
       }
     else
     if ( tyme.days < 1 )   /* last year */
       {
          tyme.days += maxdays;
          tyme.year -= 1;
       }
     tyme.zone = 0.0;
     ftime = tyme;
     return (errNum);
}

int zulu2time (edate itime, float newzone, edate ftime&)
* -------------------------------------------------------------------------- */
/* Convert a Zulu time to another local time zone                             */
/* v1.0 eab 12/2000                                                           */
/* Algorithm:                                                                 */
/*     First set the max number of days in the year by using isleap           */
/*     Now subtract the seconds for time zone correction to current seconds   */
/*     Now we do a series of checks to see if we changed to a different day   */
/*          If so we update the day and seconds, then see if that changes the */
/*          year and if so update the day and year accordingly                */
/*        if time > 2400 then subtract 2400 from time and increment date      */
/*        if time < 0000 then add 2400 to time and decrement date             */
/*        if day > year's end then date=1 and increment year                  */
/*        if day < 1 then day=year's end and decrement year	                  */
/* -------------------------------------------------------------------------- */
{	
     edate    tyme;
     int      maxdays;
     int      errNum =0;
     float    secs_per_day=24.0*60.0*60.0;

     isleap(itime.year) ? maxdays = 366 : maxdays = 365;
     tyme.secs = itime.secs - (newzone * 3600)
     if (tyme.secs > (secs_per_day - 1)
       {
          tyme.secs -= secs_per_day;
          tyme.days += 1;
       }
     else
     if (tyme.secs < 0)  /* before midnight */
       {
          tyme.secs += secs_per_day;
          tyme.days -= 1;
       }
     if (tyme.days > maxdays)   /* next year */
       {
          tyme.days -= maxdays;
          tyme.year += 1;
       }
     else
     if ( tyme.days < 1 )   /* last year */
       {
          tyme.days += maxdays;
          tyme.year -= 1;
       }
     tyme.zone = newzone;
     ftyme = tyme;
     return (errNum);
}

int Gregorian2Internal (gdate itime, edate tyme&)
/* -------------------------------------------------------------------------- */
/* This function converts a Gregorian date to an Internal date.               */
/*                                                                            */
/* Gregorian Calendar                                                         */
/* ==================                                                         */
/* The Gregorian calendar consists of 12 months of varying lengths and        */
/*   starting days,  has leap years                                           */
/* Month Names = January, February, March, April, May, June, July August,     */
/*               September, October, November, December                       */
/* Month lengths = 31, 28?29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31          */
/* Day Names = Sunday, Monday, Tuesay, Wednesday, Thursday, Friday, Saturday  */
/*           User selects which day is the starting day for the week          */
/*Algorithm:                                                                  */
/*   Determine if leap year and use appropriate month set                     */
/*   Determine Integer month                                                  */
/*   Return da = day of month plus sum of previous months                     */
/*============================================================================*/
{
     int   errNum = 0;
     short maxdays;

     short leapdays [31,29,31,30,31,30,31,31,30,31,30,31];
     short regdays  [31,28,31,30,31,30,31,31,30,31,30,31];

     isleap(itime.year) ? dayinmonth = leapdays : regdays ;
     tyme.secs = itime.secs + (60.0 * itime.hours);
     tyme.year = itime.year;
     tyme.zone = itime.zone;
     if ( itime.month == 0 )
       {
          tyme.days = itime.day
       }
     else
       {
          tyme.days = 0;
          for (i=1 : i < (itime.month-1) : i++)
             {
               tyme.days += dayinmonth[i-1];
             }
          tyme.days += itime.day;
     return(errNum);
}

int Internal2Gregorian (edate itime, gdate ftyme&)
/* -------------------------------------------------------------------------- */
/* This function converts a Internal date to a Gregorian date.                */
/*                                                                            */
/* Gregorian Calendar                                                         */
/* ==================                                                         */
/* The Gregorian calendar consists of 12 months of varying lengths and        */
/*   starting days,  has leap years                                           */
/* Month Names = January, February, March, April, May, June, July August,     */
/*               September, October, November, December                       */
/* Month lengths = 31, 28?29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31          */
/* Day Names = Sunday, Monday, Tuesay, Wednesday, Thursday, Friday, Saturday  */
/*           User selects which day is the starting day for the week          */
/*Algorithm:                                                                  */
/*   Determine if leap year and use appropriate month set                     */
/*   While day !inMonth increment month                                       */
/*   Return Gregorian Date                                                    */
/*============================================================================*/
{
}

edate Shire2Internal (sdate itime)
/* -------------------------------------------------------------------------- */
/* This function converts a Shire date to an Internal date.                   */
/*                                                                            */
/* Shire Calendar                                                             */
/* ===============                                                            */
/* 12 months of 30 days and 5?6 days outside of the months 2 of which are not */
/*   part of any week but are their own days,  has leap years                 */
/* Month Names = Afteryule, Solmath, Rethe, Astron, Thrimidge, Forelithe,     */
/*               Afterlithe, Wedmath, Halimath, Winterfilth, Blotmath, Foryule*/
/* Day Names = Sterrendei, Sunnedei, Momendei, Trewsdei, Hevensdei, Meresdei, */
/*             Highdei                                                        */
/* Year progression 2Yule(on Sterrendei), Solmath(), Rethe(), Astron(),       */
/*                  Thrimidge(),Forelithe(), 1Lithe,                          */
/*                  Midyear's Day[Not a day of the week]                      */
/*                  Overlithe[On leap year's only and not a day of the week]  */
/*                  2Lithe, Afterlithe(), Wedmath(), Holimath(), Winterfilth()*/
/*                  Blotmath(), Foreyule(), 1Yule                             */
/* Algorithm:                                                                 */
/*   If special day then set value and return                                 */
/*   Determine if leap year and use appropriate year set                      */
/*   determine integer month                                                  */
/*   return day = day of month plus sum of previous months                    */
/*============================================================================*/
{
}

sdate Internal2Shire (edate itime)
/* -------------------------------------------------------------------------- */
/* This function converts a Internal date to a Shire date.                    */
/*                                                                            */
/* Shire Calendar                                                             */
/* ===============                                                            */
/* 12 months of 30 days and 5?6 days outside of the months 2 of which are not */
/*   part of any week but are their own days                                  */
/* Month Names = Afteryule, Solmath, Rethe, Astron, Thrimidge, Forelithe,     */
/*               Afterlithe, Wedmath, Halimath, Winterfilth, Blotmath, Foryule*/
/* Day Names = Sterrendei, Sunnedei, Momendei, Trewsdei, Hevensdei, Meresdei, */
/*             Highdei                                                        */
/* Year progression 2Yule(on Sterrendei), Solmath(), Rethe(), Astron(),       */
/*                  Thrimidge(),Forelithe(), 1Lithe,                          */
/*                  Midyear's Day[Not a day of the week]                      */
/*                  Overlithe[On leap year's only and not a day of the week]  */
/*                  2Lithe, Afterlithe(), Wedmath(), Holimath(), Winterfilth()*/
/*                  Blotmath(), Foreyule(), 1Yule                             */
/* Algorithm:                                                                 */
/*   Determine if leap year and use appropriate year set                      */
/*   If special day then return Shire date by table                           */
/*   While day !inMonth increment Month                                       */
/*   return Shire date                                                        */
/*============================================================================/
}

string ShireDayofWeek()
/*--------------------------------------------------------------------------- */
/* This function returns the name of the day of week 0:7 given a Shire date   */
/* Shire Calendar                                                             */
/* ===============                                                            */
/* 12 months of 30 days and 5?6 days outside of the months 2 of which are not */
/*   part of any week but are their own days                                  */
/* Month Names = Afteryule, Solmath, Rethe, Astron, Thrimidge, Forelithe,     */
/*               Afterlithe, Wedmath, Halimath, Winterfilth, Blotmath, Foryule*/
/* Day Names = Sterrendei, Sunnedei, Momendei, Trewsdei, Hevensdei, Meresdei, */
/*             Highdei                                                        */
/* Year progression 2Yule(on Sterrendei), Solmath(), Rethe(), Astron(),       */
/*                  Thrimidge(),Forelithe(), 1Lithe,                          */
/*                  Midyear's Day[Not a day of the week]                      */
/*                  Overlithe[On leap year's only and not a day of the week]  */
/*                  2Lithe, Afterlithe(), Wedmath(), Holimath(), Winterfilth()*/
/*                  Blotmath(), Foreyule(), 1Yule                             */

/*   Algorithm:                                                                */
/*   ==========                                                                */
/*=============================================================================*/
{
}

string GregorianDayofWeek()
This subroutine returns the name of the day of week 1:7 given a Gregorian Date
Algorithm:

Boolean isleap(int year)
/* -------------------------------------------------------------------------- */
/* The algorithm used here is simplistic, refinement will be done later       */
/* Algorith:                                                                  */
/*      First return False for all years not divisible by 4                   */
/*            All years left are now evenly divisible by 4 so maybe leap year */
/*      Second return True for all years not divisible by 100                 */
/*            left is just the century years                                  */
/*      Return true if divisible by 400 otherwise return false                */
/* -------------------------------------------------------------------------- */
{
/*     if (year mod 4 != 0) return (False);  */
/*     if (year mod 100 != 0) return (True); */
/*     if (year mod 400 == 0) return (True); */
/*     return(False);                        */

	If (year mod 4) <> 0 then
		isaLeapYear = FALSE;
	else 
		isaLeapYear = TRUE;
	If (((year mod 100) == 0) and ((year mod 400) <> 0)) then
		isaLeapYear = FALSE;
	return isaLeapYear;
}

float secs2time()
This subroutine converts seconds from midnight to 24 hour time
Algorithm:
	ss.sss = secs mod 60
	hour = trunc(secs - ss.sss)/3600

float time2secs()
/* -------------------------------------------------------------------------- */
/* This function converts 24 hour time to seconds from midnight               */
/*                                                                            */
/*   Algorithm:                                                               */
/*   ==========                                                               */
/*        seconds = (hours * 3600) + (minutes * 60) + seconds                 */
/*============================================================================*/

nn 12convert24
/* -------------------------------------------------------------------------- */
/* This function converts 24 hour time format to 12 hour time format          */
/*                                                                            */
/*   Algorithm:                                                               */
/*   ==========                                                               */
/*   If hour is less than 13 then returns time plus "A.M." otherwise it       */
/*        subtracts 12 hours and returns resultant time plus "P.M."           */
/*============================================================================*/
{
}

nn 24convert12
/* -------------------------------------------------------------------------- */
/* This function converts 12 hour time format to 24 hour time format          */
/*                                                                            */
/*   Algorithm:                                                               */
/*   ==========                                                               */
/*   if "A.M." returns time with 12->00 otherwise it adds 12 hours and returns*/
/*============================================================================*/
{
}


nn deltaDates(edate itime, edate ftyme)
/* -------------------------------------------------------------------------- */
/*  This function determines the delta time between two dates                 */
/*                                                                            */
/*   Algorithm:                                                               */
/*   ==========                                                               */
/*   Determine the greater date                                               */
/*        subtract from the greater date the lesser date                      */
/*        subtract seconds and make necessary day corrections                 */
/*        subtract days and make any necessarey year corrections              */
/*        subtract years                                                      */
/*        return delta time                                                   */
/*============================================================================*/
{
}

sub dateDelta()
/* -------------------------------------------------------------------------- */
/*  This function computes the new date given the original date and delta time*/
/*                                                                            */
/*   Algorithm:                                                               */
/*        add delta time to date making corrections as necessary              */
/*        return new date                                                     */
/*============================================================================*/
{
}

C notes for calendar

string ShireDayofWeek()
string GregorianDayofWeek()


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

date Julian_2_Hobbit(int day, int year)
int Hobbit_2_Julian(int month, int day, int year)

int day_of_week_Gregorian(date)
int day_of_week_Hobbit(date)
int day_of_week_Julian(date)

Appointment_by_day()
Appointment_by_date()

Display_week
Display_day
int time2zulu (edate itime, edate ftime&);

Internal date:time format is UTC -  year:day:sssss.sss
time zones internal sssss
/* */

/* */	

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
	if year mod 4  0 then return False
	if year mod 4 = 0 and year mod 400 = 0 return True
	if year mod 4 = 0 and year mod 100  0 return True else False
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
	
	
#Chinese Zodiac animals

year = int(input("Enter a year: "))
zodiacYear = year % 12 
if zodiacYear == 0:
    print("monkey")
elif zodiacYear == 1:
    print("rooster")
elif zodiacYear == 2:
    print("dog")
elif zodiacYear == 3:
    print("pig")
elif zodiacYear == 4: 
    print("rat")
elif zodiacYear == 5: 
    print("ox")
elif zodiacYear == 6:
    print("tiger")
elif zodiacYear == 7:
    print("rabbit")
elif zodiacYear == 8:
    print("dragon")
elif zodiacYear == 9:
    print("snake")
elif zodiacYear == 10:
    print("horse")
else: 
    print("sheep")	
	
Base Reference - January 1 1901 Gregorian was a Tuesday
	
Mars day is 24hours 37 minutes Earth time and is called a sol.  There are 668.5991 sols per
Mars year.  Invent caledar having 668 or 669(leap) sols per year.  Perhaps 8 day weeks so 83
weeks 4 days per year.   depends if months to be equal length of week or a bit varied.
perhaps quarter year is about 20 weeks with 3 weeks 4 days extra.  Quarter is 4 months of
5 weeks with one month each quarter having 6 weeks for three quarters and one month in
the fourth quarter having 5 weeks 4 or 5 days. 	
	
Jewish cal year 5758 begins on Gregorian Oct 2, 1997	

A program for time and calendars

Time:
	24hour clock standard
	24hour world clock - AngularTime

	
Time:
	Internal time is seconds from midnight at GMT (0-86,400) 
	Functions:
		Internal to standard 24 hour clock GMT (0-24,0-60,0-60)
			secsrm = current seconds from midnight GMT
			hours = trunc(secsrm/3600)
			secrm = secsrm - (hours * 3600)
			minutes = trunc(secsrm/60)
			seconds = secsrm - (minutes * 60)
		GMT to local time
			Hours = Hours + TimeZone  (+12 to -12)
			if hours > 24 then day++ && hours=hours-24
			if hours < 00 then day-- && hours=hours+24
		Internal to world clock (0-360,0-60,0-60)
			secsrm = current seconds from midnight GMT
			degrees = trunc(secsrm/240)
			secrm = secsrm - (degrees * 240)
			minutes = trunc(secsrm/60)
			seconds = secsrm - (minutes * 60)
			

Calendars
	Internal date is days from start of Gregorian year GMT
	Functions:
	

/* ********** ********** ********** ********** ********** ********** */
/* Convert etyme to seconds                                          */
int etime2seconds(etyme itime, float secs)
{
	int errNum = 0;
	secs = itime.seconds + (60 * itime.minutes) + (3600 * itime.hours);
	return(errNum)
}

/* ********** ********** ********** ********** ********** ********** */
/* Seconds in day to 24 hour Earth time GMT                          */
int seconds2etime(float seconds, etyme theTime)
{
	int errNum = 0;
	
	if (seconds < 0) return(-1);    // negative time in date
	if (seconds >= 86400) return (1);  // more seconds than allowed in Earth day
	
	theTime.hour = (int)(seconds / 3600);
	seconds -= (theTime.hours * 3600);
	theTime.minutes = (int)(seconds / 60);
	theTime.seconds = seconds - (theTime.minutes * 60);
	return(errNum);
}

/* ********** ********** ********** ********** ********** ********** */
/* Convert angular time to seconds                                   */
int atime2seconds(atyme itime, float seconds)
{
	int errNum = 0;

	seconds = (itime.degrees * 240) + (itime.arc_minutes * 4) + (itime.arc_seconds / 15.0));
	return(errNum)
}

/* ********** ********** ********** ********** ********** ********** */
/* Convert seconds to angular time                                   */
int seconds2atime(float seconds, atyme theTime)
{
	int	errNum = 0;

	if (seconds < 0) return(-1);    // negative time in date
	if (seconds >= 86400) return (1);  // more seconds than allowed in Earth day
	
	theTime.degrees = (int)(seconds / 360);
	seconds -= (theTime.degrees * 360);
	theTime.arc_minutes = (int)(seconds / 60);
	theTime.arc_seconds = seconds - (theTime.arc_minutes * 60);
	return(errNum);
}

/* ********** ********** ********** ********** ********** ********** */
/* Convert a standard 24 hour Earth local time to zulu time          */
int local2zulu (etyme itime, float timeZone etyme ftime&)
{
	int errNum = 0;
	
	ftime.hour = itime + timeZone;
	return (errNum)
}

/* ********** ********** ********** ********** ********** ********** */
/* Convert a standard 24 hour Earth zulu time to local time          */
int zulu2local (etyme itime, float timeZone etyme ftime&)
{
	int errNum = 0;
	
	ftime.hour = itime - timeZone;
	return (errNum);
}

/* ********** ********** ********** ********** ********** ********** */
/* convert a zulu Earth time to a local Earth time zone */
int local2zulu (edate itime, float newzone, edate ftime&)   
{
     edate    tyme;
     int      maxdays;
     int      errNum = 0;
     float    secs_per_day=24.0*60.0*60.0;

     isleap(itime.year) ? maxdays = 366 : maxdays = 365;
     tyme.secs = itime.secs + (newzone * 3600)
     if (tyme.secs > (secs_per_day - 1)
       {
          tyme.secs -= secs_per_day;
          tyme.days += 1;
       }
     else
     if (tyme.secs < 0)  /* before midnight */
       {
          tyme.secs += secs_per_day;
          tyme.days -= 1;
       }
     if (tyme.days > maxdays)   /* next year */
       {
          tyme.days -= maxdays;
          tyme.year += 1;
       }
     else
     if ( tyme.days < 1 )   /* last year */
       {
          tyme.days += maxdays;
          tyme.year -= 1;
       }
     tyme.zone = 0;
     ftime = tyme;
     return (errNum);
}

/* ********** ********** ********** ********** ********** ********** */
/* convert a zulu Earth time to a local Earth time zone */
int zulu2local (edate itime, float newzone, edate ftime&)   
{
     edate    tyme;
     int      maxdays;
     int      errNum =0;
     float    secs_per_day=24.0*60.0*60.0;

     isleap(itime.year) ? maxdays = 366 : maxdays = 365;
     tyme.secs = itime.secs - (newzone * 3600)
     if (tyme.secs > (secs_per_day - 1)
       {
          tyme.secs -= secs_per_day;
          tyme.days += 1;
       }
     else
     if (tyme.secs < 0)  /* before midnight */
       {
          tyme.secs += secs_per_day;
          tyme.days -= 1;
       }
     if (tyme.days > maxdays)   /* next year */
       {
          tyme.days -= maxdays;
          tyme.year += 1;
       }
     else
     if ( tyme.days < 1 )   /* last year */
       {
          tyme.days += maxdays;
          tyme.year -= 1;
       }
     tyme.zone = newzone;
     ftyme = tyme;
     return (errNum);
}

//* ********** ********** ********** ********** ********** ********** */
/* Convert a Gregorian Calendar date and time to internal date&time  */
int gregorian2internal(gdates itime, edaet ftime)
{
	int	errNum = 0;
	int maxdays;
	struct etyme theTime;
	
	isleap(itime.year) ? maxdays = 366 : maxdays = 365;
	if (itime.zone != 0)
	{
		errNum = local2zulu(itime.etyme, itime.zone, theTyme);
		if (theTyme.hour > 23) 
		{
			itime.day += 1;
			theTyme.hour -= 24;
		}
		if (theTyme.hour < 0 )
		{
			itime.day -= 1;
			theTyme.hour += 24;
		}
	}
	errNum = etime2seconds(theTyme, ftime.seconds);
	ftime.year = itime.year;
	switch (itime.month)
	{
		case  1: // January - 31
				ftime.days = itime.day;
				if (itime.day == 0 )
				{
					isleap((itime.year - 1)) ? ftime.days = 366 : ftime.days = 365;
					ftime.year -= 1;
				}
				break;
		case  2: // February - 28 ? 29
				ftime.days = itime.day + 31;
				break;
		case  3: // March - 31
				isleap(itime.year) ? ftime.days = 59 + itime.day : ftime.days = 60 + itime.day;
				break;
		case  4: // April - 30
				isleap(itime.year) ? ftime.days = 90 + itime.day : ftime.days = 91 + itime.day;
				break;
		case  5: // May - 31
				isleap(itime.year) ? ftime.days = 120 + itime.day : ftime.days = 121 + itime.day;
				break;
		case  6: // June - 30
				isleap(itime.year) ? ftime.days = 151 + itime.day : ftime.days = 152 + itime.day;
				break;
		case  7: // July - 31
				isleap(itime.year) ? ftime.days = 181 + itime.day : ftime.days = 182 + itime.day;
				break;
		case  8: // August - 31
				isleap(itime.year) ? ftime.days = 212 + itime.day : ftime.days = 213 + itime.day;
				break;
		case  9: // September - 30
				isleap(itime.year) ? ftime.days = 243 + itime.day : ftime.days = 244 + itime.day;
				break;
		case 10: // October - 31
				isleap(itime.year) ? ftime.days = 273 + itime.day : ftime.days = 274 + itime.day;
				break;
		case 11: // November - 30
				isleap(itime.year) ? ftime.days = 304 + itime.day : ftime.days = 305 + itime.day;
				break;
		case 12: // December - 31
				isleap(itime.year) ? ftime.days = 334 + itime.day : ftime.days = 335 + itime.day;
				if (ftime.days > maxdays)
				{
					ftime.year += 1;
					ftime.days = 1;
				}
				break;
	}
	return (errNum);
}

/* ********** ********** ********** ********** ********** ********** */
/* Convert an internal date and time to Gregorian date and time      */
/* Note that if year == 1582 10/5==10/15
{
}

/* ********** ********** ********** ********** ********** ********** */
int angular2zulu (edate itime, edate ftime)
/* ********** ********** ********** ********** ********** ********** */
int zulu2angular (edate itime, edate ftime)
/* ********** ********** ********** ********** ********** ********** */
i/* ********** ********** ********** ********** ********** ********** */
int internal2Shire()
/* ********** ********** ********** ********** ********** ********** */
int dectime2internal
/* ********** ********** ********** ********** ********** ********** */
int Fixed2internal
/* ********** ********** ********** ********** ********** ********** */
int world2internal
/* ********** ********** ********** ********** ********** ********** */

int Gregorian2Julian (gdate itime, edate tyme&)
/* -------------------------------------------------------------------------- */
/* Convert a Gregorian date to a Julian date                                  */
/* v1.0 eab 12/2000                                                           */
/* Algorithm:                                                                 */
/*      First determine if the year is a leap year and set days/month array   */
/*                                                                            */
{
	 int   errNum = 0;
     short maxdays;

     short leapdays [31,29,31,30,31,30,31,31,30,30,30,31];
     short regdays  [31,29,31,30,31,30,31,31,30,30,30,31];

     isleap(itime.year) ? dayinmonth = leapdays : regdays ;
     tyme.secs = itime.secs + (60.0 * itime.hours);
     tyme.year = itime.year;
     tyme.zone = itime.zone;
     if ( itime.month == 0 )
       {
          tyme.days = itime.day
       }
     else
       {
          tyme.days = 0;
          for (i=1 : i < (itime.month-1) : i++)
             {
               tyme.days += dayinmonth[i-1];
             }
          tyme.days += itime.day;
     return(errNum);
}

ALso Mars days, Mars years (invent if not found a mars day clock and calendar year based 
totally on Mars )  import only seconds as small unit of time


calendar -w
#include.calendar.__>
mo/day<tab>description of day
Thursday  every Thursday -4 +5 aliass last, first second
/* */ comments
nn  nn of every month
<tab> at beginning of line uses last date
* match every month
* after date
Easter is recognized  so can specify a date like Easter-46

mayan calendar

three calendars
     Long Count
     Tzolkin(divine)
     Haab(civil)

used together in order above
     long count ex 13.0.0.0.0
     Tzolkin ex 4 Ahau
     Haab 8 Kumku

Haab
     365 day solar calendar 18 months of 20 days each and one month of 5 days(Uayeb
     day then month
Tzolkin
     260 day calendar with 20 periods of 13 days
Long Count
     cycle is 2,880,000 days long (about 7885 solar years)
     Baktun.Katun.Tun.Uinal.Kin
          Kin=1 day 0-19
          Uinal=20 kin = 20 days   0-17
          Tun = 18 uinal = 360 days  0-19*
          Katun = 20 tun = 360 uinal = 7200 days  0-19
          Baktun = 20 katun = 400 tun = 7200 uinal = 144,000 days  1-13
creation date is 4 Ahau, 8 Kumku == August 11, 3114 BCE Gregorian

date is combo of Tzolkin and Haab and extended by the long count

A calendar round is comprised of both the Haab and Tzolkin calendars and is 52 years

Persian Calendar - solar calendar
     6 31 day months followed by 5 30 day months and ends with a month of 29 or 30 days
     based on observation of the sun at vernal equinox in Iran about 250 miles east of Tehran

Chinese calendar - lunisolar
     60 year cycle
          10 celestial stem
          12 terrestial branch (zodiac)

Coptic Calendar
     12 30day months and 1 5 or 6 day month  leap years evey 4 years

