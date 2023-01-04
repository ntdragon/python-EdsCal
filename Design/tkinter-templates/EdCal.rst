=======================
Ed's Calendar - Tkinter
=======================
:Description: Ed's calendar using Tkinter as user interface and procedural python3
:Author: Edward Birdsall
:Date: 2022 March 30
:Version: 0.1

:Long Description and Goals:  Ulimately this will turn into a calendar program keeping track of appointments and such
     and displaying the information using a number of different calendars.  Currently working with Tkinter and 
     procedural python.  Final 'production' edition will be in Object Oriented python3 using the MVC structure.
     
Goals:
------
* Display a calendar using either Tkinter or HTML
* Day, Week and Month formats
* Command Line calls or tkinter/HTML interactive
* In addition to Gregorian a number of other calendars to display such as
     + Julian
     + Jewish
     + Scientific
     + Shire
     + Oriental
* Use the same call variables for both Tkinter and the Jinja2(HTML) displays

Variables:
----------
Desired input to structuring page:
     hd, hdr, cal, pref
Internal:
     dts = list of day numbers used to set up tdy[x]["dnum"]
     
Desired output to display the page
-------------------------------------
* hd:  Web/TC/Tk page
* hdr: dictionary with calendar header information
          * name: name of calendar
          * page: month year Calendar
          * today: day of week and date of current day
* days:  days of week
* colorsm:  dictionary with colors for background of dates
          priormonth, thisbefore, today, thismonth, nextmonth, site, neutral, calSclr
* tdy:  dictionary array of information for the days to be displayed
          * bgtclr - background today clear
          * bgeclr - background event clear
          * dnum - day number
          * devt - number of day's events
          * devt1t - day event today first title
          * devt1c - day event today first calendar color
          * devt2t - day event today second title
          * devt2c - day event today second calendar color
          * devt3t - day event today third title
          * devt3c - day event today third calendar color
          * devt4t - day event today fourth title
          * devt4c - day event today fourth calendar color
* cal:  calendar display and control information
          * month - Display Month
          * year - Display Year
          * startwk - week number for first display week
          * calrows - number of rows of calendar to be displayed
          * calAt - name of first calendar
          * calBt - name of second calendar
          * calCt - name of third calendar
          * calDt - name of fourth calendar
          * calEt - name of fifth calendar
* pref:  dictionary of user preferences
          * startDay - the starting day of the week 1=Monday, 0 or 7 is Sunday
          * calAclr - color for first calendar
          * calBclr - color for second calendar
          * calCclr - color for third calendar
          * calDclr - color for fourth calendar
          * calEclr - color for fifth calendar

