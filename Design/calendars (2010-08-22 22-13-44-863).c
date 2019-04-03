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
