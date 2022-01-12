/******************************************************************************/
/* Etyme.m                                                                    */
/* -------------------------------------------------------------------------- */
/* Version: 1.0                                                               */
/******************************************************************************/

/******************************************************************************/
/********************              #includes               ********************/
/******************************************************************************/
import 'Etyme.h'

@implementation
/******************************************************************************/
/********************      the methods themselves          ********************/
/******************************************************************************/
+ (NSOpenGLPixelFormat*) basicPixelFormat
{
	static NSOpenGLPixelFormatAttribute attributes[]=
		{
			NSOpenGLPFAWindow,
			NSOpenGLPFADoubleBuffer,
			NSOpenGLFPADepthSize, (NSOpenGLPixelFormatAttribute)16,
			(NSOpenGLPixelFormatAttribute)nil
		};
	return ([[[NSOpenGLLPixelFormat alloc] initWithAttributes:attributes] autorelease]);
}
/* ********** ********** ********** ********** ********** ********** */
- (void) resizeGL
{
}
/* ********** ********** ********** ********** ********** ********** */
- (void)drawRect:(NSREct)rect
{

}

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

/* ********** ********** ********** ********** ********** ********** */
/* Is this a Earth Gregorian calendar leap year                      */
Boolean isleap(int year)
{
	Boolean isaLeapYear;
	
	 if (year mod 4) <> 0 then
		isaLeapYear = FALSE;
	else 
		isaLeapYear = TRUE;
	If (((year mod 100) == 0) and ((year mod 400) <> 0)) then
		isaLeapYear = FALSE;
	return (isaLeapYear);
}

/* ********** ********** ********** ********** ********** ********** */
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
int Shire2internal(gdates itime, edaet ftime)int gregorian2internal(gdates itime, edaet ftime)
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
		case  0: // Days outside of months
				if (itime.day == 1) ftime.days = 1;
		case  1: // Yule
				ftime.days = itime.day + 1;
				if (itime.day < 0 )
				{
					isleap((itime.year - 1)) ? ftime.days = 366 : ftime.days = 365;
					ftime.year -= 1;
				}
				break;
		case  2: // Solmath
				ftime.days = itime.day + 31;
				break;
		case  3: // Rethe
				ftime.days = itime.day + 61;
				break;
		case  4: // Astron
				ftime.days = itime.day + 91;
				break;
		case  5: // May - 31
				ftime.days = itime.day + 121;
				break;
		case  6: // June - 30
				ftime.days = itime.day + 151;
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
int internal2Shire()
/* ********** ********** ********** ********** ********** ********** */
int dectime2internal
/* ********** ********** ********** ********** ********** ********** */
int Fixed2internal
/* ********** ********** ********** ********** ********** ********** */
int world2internal
/* ********** ********** ********** ********** ********** ********** */

/* ********** ********** ********** ********** ********** ********** */

/* ********** ********** ********** ********** ********** ********** */

/* ********** ********** ********** ********** ********** ********** */

/* ********** ********** ********** ********** ********** ********** */

@end
/******************************************************************************/
/********************               end                    ********************/
/******************************************************************************/

# calendar routines in C?C++




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
{
}

string GregorianDayofWeek()
{
}

float secs2time()
float time2secs()
nn 12convert24
nn 24convert12
nn deltaDates(edate itime, edate ftyme)
