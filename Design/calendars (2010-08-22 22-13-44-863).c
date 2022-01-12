/******************************************************************************/
/* Main.c                                                                     */
/* -------------------------------------------------------------------------- */
/* Version:                                                                   */
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
# calendar routines in C?C++

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

     edate   itime, etime;

     exit(0);
}

int time2zulu (edate itime, edate ftime&)   /* Convert a time to zulu time */
{
     edate    tyme;
     int      maxdays;
     int      errNum = 0;
     float    secs_per_day=24.0*60.0*60.0;

     isleap(itime.year) ? maxdays = 366 : maxdays = 365;
     tyme.secs = itime.secs + (itime.zone * 3600)
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
     tyme.zone = 0.0;
     ftime = tyme;
     return (errNum);
}

int zulu2time (edate itime, float newzone, edate ftime&)   /* convert a zulu time to a local time zone */

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

int Julian2Gregoriam (edate itime, gdate ftyme&)
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

Boolean isleap(int year)
{
     if (year mod 4 != 0) return (False);
     if (year mod 100 != 0) return (True);
     if (year mod 400 == 0) return (True);
     return(False);
}
	If (year mod 4) <> 0 then
		isaLeapYear = FALSE;
	else 
		isaLeapYear = TRUE;
	If (((year mod 100) == 0) and ((year mod 400) <> 0)) then
		isaLeapYear = FALSE;
	return isaLeapYear;

float secs2time()
float time2secs()
nn 12convert24
nn 24convert12
nn deltaDates(edate itime, edate ftyme)

C notes for calendar

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

Internal date:time format is Julian GMT -  year:day:sssss.sss
time zones internal sssss
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
