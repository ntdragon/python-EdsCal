#!\bin\python3

"""
Thoughts on displays and functions for the program

In python the base calendar used and event calendars are the Gregorian calendar.  This is due to the datetime module
in python.  For C and Fortran I will use year, DayOfYear as an internal calendar and convert to the desired calendar
for display.  Also I will use the 24hour clock and C-Fortran seconds from midnight.

Display (HTML - TCL/TK)
     Day
     Week
     Month
     Quarter
     Year
     Appointment
     Maintenance
     Tasks
     Project
     
Calendars
     Gregorian
     Julian
     Shire
     Jewish
     Oriental - "Chinese-Japanese"  There are a number of these so I'll pick one and use it.
     Mayan
     Coptic
     Persian
     Scientific?
     DaysOfYear - Internal
     Mars
     Lunar (theMoon itself)

Event 'calendars'
     Liturgical
     US Holidays
     Birthdays
     Tasks - Maintenance - Project
     Appointments

Time
     24 hour
     12 hour
     Jewish
     Angular
     Decimal
     ?

Printouts
     Day's Appointment and tasks/Maintenance
     week with appointments and tasks
     Month with appointments

Functions
     Set up Display
     set up Printout
     Printing
     Display ---
     Convert between different calenders
     Add / Edit / Delete Event calendars
"""
