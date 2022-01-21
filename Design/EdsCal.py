#!\bin\python3

"""
Eds Calendar Models

This module contains the code for all my calendar model functions and routines.
Due to python calendar module I will be using the Gregorian calendar as the base
calendar and then computing and using the other calendars on the fly.
"""

module EdsCal(Calendar)

     def Gregorian
     
     def ToJulian
     
     def FromJulian
     
     def ToShire
          """
          Shire calendar
          12 months of 30 days each.  year starts on (Saturday)Sterrendei with 2Yule
          Year pattern is;
               2Yule, Afteryule Solmath, Rethe, Astron, Thrimidge, Forelithe, 1Lithe, Midyear's Day, (Overlithe on \
               leap years and not a day of any week), 2Lithe, Afterlithe, Wedmath, Halimath, Winterfilth, Blotmath, \
               Foreyule, 1Yule
               note that some days are not part of any month though part of the week and Midyear's day and Overlithe \
               are not part of any weekday
          """
          MonthsOfYear={Afteryule Solmath Rethe Astron Thrimidge Forelithe Afterlithe Wedmath Halimath Winterfilth \
                         Blotmath Foreyule}.split()
          DaysOfWeek={Sterrendei Sunnedei Momendei Trewesdei Hevensdei Meresdei Highdei}.split()
     
     def FromShire
          dow={}
     
     def ToJewish
          """
          Reference: Judaism 101:Jewish calendar by Tracey R Rich
          Note 1: Jewish day starts at sundown in Jerusalem so that needs to be computed into the structure
          Note 2: Based on moon cycles and used to be calculated by observation but in 4th century computed
          Note 3: Leap month added vice leap day
          Note 4: Years number from 'Creation' 
          Note 5: Nissan is in the March-April time of the Gregorian Calendar  month names are Babylonian
          Note 6: Jewish 'New Year' is n Tishri
          Note 7: Length of months starting with Nissan - 30,29,30,29,30,29,30, (29 or 30),(30 or 29),29, 30
                    Adar_I = 30 Adar or Adat_II is 29 days
          Note 8: names for days of week can add _Day(English) or Yom_ (Hebrew)
          Note 9: 19 year cycle  Leap years are 3, 6, 8, 11, 14, 17 and 19 years in the cycle
                    current cycle begins with year 1 Tishri 5758 (Gregorian- October 2, 1997)
          Note 10: 14 possible formats for year
          Note 11: Molad is 'New moon" which is the beginning of the month, maladot is 29days 12 hours 793 parts
                    part is 3-1/3 seconds, 18 parts per minute, 1,080 parts per hour
                    ritual hour is 1/12 the time between sunrise and sunset  however molad hours are constant 24/day
          
          Method to the calculations: (Jewish to Jewish)
          1. Start with a known molad and corresponding Gregorian Date
          2. Determine the number of months between the known molad and Tishri of the year of the date being calculated
          3. Multiply the number of months by the length of the molad: 29days 12 hours 793parts (a part=3-1/3 seconds)
          4. Add the result to the known starting molad
          5. Apply the rules of postponement to determine the date of Rosh Hasanah for the current year
          6. to get other dates use this year's and next year' Rosh Hasanah dates to work out the date
          A. For Gregorian date add the number of days to the know starting date and go from there
          
          Step 1
          Known Molads - 1 Tishri 5732 = 2d 7h 743p (6PM Juruslaem is 0 hr) Sept 20 1971
                         1 Tishri 5661 = 2d 11h 9p   Sept 24 1900
                         1 Tishri 5558 = 5d 11h 607p Sept 21 1797
                         1 Tishri 3869 = 7d 8h 957p  Sept 22 108
                         1 Tishri 4120 = 5d 8h 29p   Sept 10 359 start of standardized Jewish calendar
          Step 2
               Determine the number of months from know to desired date
               
          """
          MonthsOfYear={Nissan Iyar Sivan Tammuz Av Elul Tishri Cheshvan Kislev Tevet Shevat Adar }
          MonthsOfLeapYear={Nissan Iyar Sivan Tammuz Av Elul Tishri Cheshvan Kislev Tevet Shevat Adar_I Adar_II }
          DaysOfWeek_English={First Second Third Fourth Fifth Sixth Sabbath}
          DaysOfWeek_Hebrew={Rishon Sheini R'vi'i Chamishi Shishi Shabbat}
     
     def FromJewish
     
     def ToOriental
     
     def FrmOriental

     def ToMayan
     
     def FromMayan
     
     def ToCoptic
     
     def FromCoptic
     
     def ToPersian
     
     def FromPersian
     
     def ToScientific
          """
          I think that is the name of the calendar
          13 months of 28 days with 7 day weeks with MidDay in the 7th month between 14 and 15 and not part of the \
          week.  The additional day for leap year LeapDay follows MidDay
          """
     def FromScientific
     
     def ToMars
     
     def FromMars
     
     def TimeToZulu
     
     def TimeFromZulu
