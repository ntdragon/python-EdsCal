/**********************************************************************************************************************/
/*   Module: time                                                                                                     */
/*====================================================================================================================*/
/*   AUTHOR: Edward Birdsall       VERSION:                 DATE:                                                     */
/*                                                                                                                    */
/*   PURPOSE:                                                                                                         */
/*        This module contains a number of functions dealing with time used in variuos calendars.  'Internal' time is */
/*        based on seconds from Midnight on an Earth standard day where seconds is a real number.  The Jewish calendar*/
/*        uses different time and calendars for other celestial bodies will have different time per day.  More        */
/*        information on the various time keeping is explained in greater depth in the function descriptions.         */
/*                                                                                                                    */
/*                                                                                                                    */
/*                                                                                                                    */
/*   INPUT FROM:                                                                                                      */ 
/*   OUTPUT TO:                                                                                                       */
/*                                                                                                                 .  */
/*                                                                                                                    */
/*   COMPILOR USED:                                                                                                   */
/*                                                                                                                    */
/*   COMPUTER HARDWARE USED:                                                                                          */
/*                                                                                                                    */
/*   DESCRIPTION OF FUNCTIONS:                                                                                        */
/*                                                                                                                    */
/*                                                                                                                    */
/*   RESTRICTIONS:                                                                                                    */
/*                                                                                                                    */
/*   VERSION HISTORY:                                                                                                 */
/*                                                                                                                    */
/**********************************************************************************************************************/


/********************************************************************************/
/*********************************   include    *********************************/
/********************************************************************************/
/* Library headers */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Local headers */
#include "time.h"
#include "calendar.h"


/********************************************************************************/
/*****************************     the functions     ****************************/
/********************************************************************************/
int time2zulu (edate itime, edate ftime&)
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
/* ---------------------------------------------------------------------------- */
int zulu2time (edate itime, float newzone, edate ftime&)
{
     edate    tyme;
     int      maxdays;
     int      errNum = 0;
     float    secs_per_day=24.0*60.0*60.0;

     isleap(itime.year) ? maxdays = 366 : maxdays = 365;
     tyme.secs = itime.secs + (lzone * 3600)
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
/* ---------------------------------------------------------------------------- */
int etime2seconds(etyme itime, float secs)
{
	int errNum = 0;
	secs = itime.seconds + (60 * itime.minutes) + (3600 * itime.hours);
	return(errNum)
}
/* ---------------------------------------------------------------------------- */
int secs2etime(float secs, etime dtime& )
{
     float tsecs;
     int  errNum = 0;
     
	if (seconds < 0) return(-1);    // negative time in date
	if (seconds >= 86400) return (1);  // more seconds than allowed in Earth day
	
     tsecs = secs mod 60
     dtime.hour = trunc(secs-tsecs)/3600
     dtime.minutes = ((secs-tsecs) - (dtime.hour*3600))/60
     dtime.seconds = tsecs
     return(errNum)
}
/* ---------------------------------------------------------------------------- */
int 12convert24(etyme itime, etyme12 ftime)
{
     int  errNum = 0;
     
     if (itime.hour < 12) then 
          ftime.hour = itime.hour
          ftime.minute - itime.minute
          ftime.seconds = itime.seconds
          ftime. daypart = "A.M."
          if itime.hour = 0) then ftime.hour=12
     else
          ftime.hour = itime.hour - 12;
          ftime.minute - itime.minute
          ftime.seconds = itime.seconds
          ftime. daypart = "P.M."
          if itime.hour=12 then ftime.hour=12
     endif
     return(errNum);
}
/* ---------------------------------------------------------------------------- */
int 24convert12(etyme12 itime, etyme ftime)
{
     int  errNum = 0;
     if itime.daypart = "A.M." then
          ftime.hour = itime.hour
          ftime.minute - itime.minute
          ftime.seconds = itime.seconds
          if itime.hour = 12 ftime.hour = 0
    else
          ftime.hour = itime.hour + 12;
          ftime.minute - itime.minute
          ftime.seconds = itime.seconds
          if itime.hour = 12 then ftime.hour = 12;
   endif
   return(errNum);
}
/* ---------------------------------------------------------------------------- */
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


int dectime2internal
/* ********** ********** ********** ********** ********** ********** */
int Fixed2internal
/* ********** ********** ********** ********** ********** ********** */
int world2internal
/* ********** ********** ********** ********** ********** ********** */
int Jtime2internal
int Mtime2internal

Mars day is 24hours 37 minutes Earth time and is called a sol.  There are 668.5991 sols per
Mars year.  Invent caledar having 668 or 669(leap) sols per year.  Perhaps 8 day weeks so 83
weeks 4 days per year.   depends if months to be equal length of week or a bit varied.
perhaps quarter year is about 20 weeks with 3 weeks 4 days extra.  Quarter is 4 months of
5 weeks with one month each quarter having 6 weeks for three quarters and one month in
the fourth quarter having 5 weeks 4 or 5 days. 	

/********************************************************************************/
/********************************     end     ***********************************/
/********************************************************************************/
