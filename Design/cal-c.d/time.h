/**********************************************************************************************************************/
/*   HEADER FILE FOR MODULE: time                                                                                     */
/*====================================================================================================================*/
/*   AUTHOR: Edward Birdsall       VERSION:                 DATE:                                                     */
/*                                                                                                                    */
/*   PURPOSE:                                                                                                         */
/*        This module contains a number of functions dealing with time used in variuos calendars.  'Internal' time is */
/*        based on seconds from Midnight on an Earth standard day where seconds is a real number.  The Jewish calendar*/
/*        uses different time and calendars for other celestial bodies will have different time per day.  More        */
/*        information on the various time keeping is explained in greater depth in the function descriptions.         */
/*                                                                                                                    */
/*        In addition to the normal hours, minutes, seconds look at angular time                                      */
/*                                                                                                                    */
/*        Internal time is seconds from midnight at GMT (0-86,400)                                                    */
/*        Angular time is based on the angle (latitude) of the location so has degrees of arc, minutes and seconds of */
/*             of arc in its defintion                                                                                */
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
/*   DESCRIPTION OF FUNCTIONS AND PROTOTYPES:                                                                         */
/*                                                                                                                    */
/*        INPUT and OUTPUT FUNCTIONS:                                                                                 */
/*                                                                                                                    */
/*             User Input Functions:                                                                                  */
/*                                                                                                                    */
/*             Display Functions:                                                                                     */
/*                                                                                                                    */
/*             File Input Functions:                                                                                  */
/*                                                                                                                    */
/*             File Output Functions:                                                                                 */
/*                                                                                                                    */
/*             Compute Functions:                                                                                     */
/*                                                                                                                    */
/*   Every Program Needs one:                                                                                         */
/*        main()                                                                                                      */
/*             This function, like all good "main"s is just a routing function controlling program flow, from         */
/*             beginning to end.                                                                                      */
/*                                                                                                                    */
/*   RESTRICTIONS:                                                                                                    */
/*                                                                                                                    */
/*   VERSION HISTORY:                                                                                                 */
/*                                                                                                                    */
/**********************************************************************************************************************/
/* A few definitions */

struct edate {
     float   secs;    /* seconds from midnight  0->86399 (Earth) */
     short   days;    /* days in year 1->365 or 366      */
     int     year;    /* year                            */
     float   zone;    /* time zone -12->+12              */
} edate;

struct etyme {        /* standard 24 hour Earth Clock    */
	float    seconds;    /* 0-59 seconds in current minute  */
	short    minutes;    /* 0-59 minutes in current hour    */
	short    hour;    /* 0-23 hour in current day        */
} etyme;

struct atyme {        /* angular Earth Clock    */
	float    arc_seconds;    /* 0-59 seconds in current minute  */
	short    arc_minutes;    /* 0-59 minutes in current hour    */
	short    degrees;        /* 0-359 degree in current day     */
} atyme;

struct etyme12 {          /* 12 hour Earth Clock    */
	float    seconds;    /* 00-59 seconds in current minute  */
	short    minutes;    /* 00-59 minutes in current hour    */
	short    hour;       /* 01-12 hour in current day        */
	char     daypart     /* AM or PM */
} etyme12;


/* FUNCTION PROTOTYPES */
/*=====================*/
/* Public - used by other modules */
/*--------------------------------*/
int time2zulu (edate itime, edate ftime&)
int zulu2time (edate itime, float newzone, edate ftime&)
int time2secs(etyme itime, float isecs)
int secs2time ( float isecs, etyme ityme )
int 12convert24( etyme12 time12, etyme time24)
int 24convert12( etyme time24, etyme12 time12)
int angular2zulu (edate itime, edate ftime)
int zulu2angular (edate itime, edate ftime)
int dectime2internal
int Fixed2internal
int world2internal
/* Private - this module only */
/*----------------------------*/


/******************************************************************************/
/*************************   function descriptions    *************************/
/******************************************************************************/

/******************************************************************************/
/*************************     Public functions       *************************/
/******************************************************************************/

/******************************************************************************/
/* function: time2zulu                                                        */
/* -------------------------------------------------------------------------- */
/* Purpose: This function converts a local time to the time at UTC            */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input: local date and time and timezone offset from UTC and pointer to the */
/*        new date and time.  It also returns an error number of zero if good */
/* Returns: date and time UTC via the pointer passed in                       */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/*   Takes the local date and time and adds the offset to the time            */
/*   It then makes any corrections to the date and time to keep it within the */
/*   band for time and date.  That is to say no greater than 86400 seconds in */
/*   a day and the dates within the year.                                     */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:  zulu2time                                                       */
/* -------------------------------------------------------------------------- */
/* Purpose: This converts a date and time UTC to a local zone date and time   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input: zulu date and time, newtime zone offset and pointer to local time   */
/* Returns: error number and updated local time                               */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/*        Adds offset to UTC time and then updates date as necessary          */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function: etime2secs                                                       */
/* -------------------------------------------------------------------------- */
/* Purpose: This converts a hh:mm:secs time format to seconds from midnight   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input: time in hh:mm:secs and pointer to output time                       */
/* Returns: error number and updated time                                     */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/*        Computes the time in seconds from midnight from a 24hour time with  */
/*        hours*3600 + minutes*60 + seconds                                   */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function: secs2etime                                                       */
/* -------------------------------------------------------------------------- */
/* Purpose: Converts a seconds from midnight to Hours,Minutes and Seconds      */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input: seconds from midnights and pointer to output time                   */
/* Returns: errNumber and updated output time                                 */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function: 12convert24                                                      */
/* -------------------------------------------------------------------------- */
/* Purpose: Converts a time in 24 hour format to 12 hour format               */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/*        if 24 hour is less than 12 sets day part to A.M. and moves time     */
/*        information else sets the daypart to P.M. and decrements the hour   */
/*        Checks and accounts for midnight and noon.                          */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function: 24convert12                                                      */
/* -------------------------------------------------------------------------- */
/* Purpose: Converts a 12 hour format time to 24 hour format                  */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/*        If daypart is A.M. then movesthe information over and checks that   */
/*        is set to 0 otherwise moves the information over incrementing the   */
/*        hour and checking that noon is set to 12                            */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
/******************************************************************************/

/******************************************************************************/
/*************************    Private functions       *************************/
/******************************************************************************/


/******************************************************************************/
/* function:                                                                  */
/* -------------------------------------------------------------------------- */
/* Purpose:                                                                   */
/* Version: 1.0                                                               */
/* Author:  Edward Birdsall                                                   */
/* Date:    04/23/2022                                                        */
/* -------------------------------------------------------------------------- */
/* Input:                                                                     */
/* Returns:                                                                   */
/* Other:                                                                     */
/* Functions Used (with module/library):                                      */
/*       Function              - module or library                            */
/* -------------------------------------------------------------------------- */
/* Algorithm:                                                                 */
/* -------------------------------------------------------------------------- */
/* Version history:                                                           */
/* Version - Date    - Author        - Notes                                  */
/* 1.0     - 04/23/2022 - Edward Birdsall - first 'official' version          */
/*        Many different versions in many different programming languages over*/
/*        the years (1990 to present) so I am consolidating the versions into */
/*        the first version in C and Fortran and Python.  Python are a bit    */
/*        different set due to the datetime module in python.                 */
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


/**********************/
/* end of header file */
/**********************/
