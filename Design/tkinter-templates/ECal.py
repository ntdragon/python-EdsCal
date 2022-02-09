#!/usr/bin/env python3

"""
calender ui using TCL/TK to match what is on gift exchange
One of the goals is to use the same variable structure as the Jinja-HTML versions.

Author: Edward Birdsall

Variables:
     Desired input to structuring page
          hd, hdr, cal, pref
     Internal:
          dts = list of day numbers used to set up tdy[x]["dnum"]
     Desired output to display the page
     Descriptions
     hd:  Web/TC/Tk page
     hdr: dictionary with calendar header information
          name - name of calendar
          page - month year Calendar
          today - day of week and date of current day
     days:days of week
     colorsm - dictionary with colors for background of dates
          priormonth, thisbefore, today, thismonth, nextmonth, site, neutral, calSclr
     tdy - dictionary array of information for the days to be displayed
          bgtclr - background today clear
          bgeclr - background event clear
          dnum - day number
          devt - number of day's events
          devt1t - day event today first title
          devt1c - day event today first calendar color
          devt2t - day event today second title
          devt2c - day event today second calendar color
          devt3t - day event today third title
          devt3c - day event today third calendar color
          devt4t - day event today fourth title
          devt4c - day event today fourth calendar color
     cal - calendar display and control information
          month - Display Month
          year - Display Year
          startwk - week number for first display week
          calrows - number of rows of calendar to be displayed
          calAt - name of first calendar
          calBt - name of second calendar
          calCt - name of third calendar
          calDt - name of fourth calendar
          calEt - name of fifth calendar
     pref - dictionary of user preferences
          startday - the starting day of the week 1=Monday, 0 or 7 is Sunday
          calAclr - color for first calendar
          calBclr - color for second calendar
          calCclr - color for third calendar
          calDclr - color for fourth calendar
          calEclr - color for fifth calendar



"""
import calendar
import datetime
from tkinter import *

class MCalendar(Frame):

     def __init__(self):
          super().__init__()

          self.initUI()

     def initUI(self):
          #=========================================================================================================
          #Begining of definitions.  Need to remember how to split this into a seperate area that invokes MCalendar
          #=========================================================================================================
          #=================================
          # desired inputs for final version what, when, which event calendars, preferences
          #=================================
          inputs = {"name":"Ed", "date":"March 2, 2019", "startDay":0,}
          #========================================================
          # some kludges for testing and until I get it all working
          #========================================================
          #cyear = int(cal.get("year"))
          cyear = 2019
          cmonth = 3
          cday = 2
          cals= [
               dict(num=0, name="Liturgical", color="yellowgreen"),
               dict(num=1, name="US Holidays", color="lightsteelblue"),
               dict(num=2, name="Birdsall Family", color="cyan"),
               dict(num=3, name="Kirkup Family",color="magenta"),
               dict(num=4, name="", color="purple"),
               dict(num=5, name="Site")
          ]
          eventCal = [
               dict(num=0, cal="Birdsall Family", startDate="March 01, 2019", title="Bryan Kovas B'Day" ),
               dict(num=1, cal="Birdsall Family", startDate="March 03, 2019", title="Greg Kovas B'Day"),
               dict(num=2, cal="Birdsall Family", startDate="March 03, 2019", title="Helen Birdsall B'Day"),
               dict(num=3, cal="Birdsall Family", startDate="March 03, 2019", title="Andrew Noyes B'Day"),
               dict(num=4, cal="Birdsall Family", startDate="March 03, 2019", title="Brielle Balmer B'Day"),
               dict(num=5, cal="Liturgical", startDate="March 03, 2019", title="Ordinary 9th Sunday"),
               dict(num=6, cal="Liturgical", startDate="March 6, 2019", title="Ash Wednesday"),
               dict(num=7, cal="US Holidays", startDate="March 10, 2019", title="DST begins"),
               dict(num=8, cal="Liturgical", startDate="March 10, 2019", title="Lent 1st Sunday"),
               dict(num=9, cal="Liturgical", startDate="March 17, 2019", title="Lent 2nd Sunday"),
               dict(num=10, cal="Liturgical", startDate="March 24, 2019", title="Lent 3rd Sunday"),
               dict(num=11, cal="Liturgical", startDate="March 31, 2019", title="Lent 4th Sunday")
          ]

          #===================================
          # Working code towards final version
          #===================================
          hd = {"loc":"Month Calendar"}
          hdr = { "name":"Ed",  "page":"March 2019 Calendar", "today":"Saturday  March  2, 2019" }
          hdr["name"] = inputs["name"]
          #hdr["page"] = inputs["date"].datetime.strptime("%B %Y")+" Calendar"
          #hdr["today"] = datetime.datetime.now().strftime("%A %B %d, %Y")
          hdr["today"] = "Saturday March 02, 2019"

          
          cal = {"month":"March", "year":"2019", "startwk":0,"calrows":5, "calAt":"Liturgical", "calBt":"US Holidays",
                "calCt":"Birdsall Family", "calDt":"Kirkup Family", "calEt":""}
          pref = {  "startDay":0,  "calAclr": "yellowgreen",  "calBclr": "lightsteelblue",  "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "purple"}
          
          
          if (inputs["startDay"] == 6):  # Week starts on Sunday
               cal["startwk"] = int(datetime.date(cyear, cmonth, cday).strftime("%U"))
          else:                        #Week starts on Monday
               cal["startwk"] = int(datetime.date(cyear, cmonth, cday).strftime("%W"))
          
          glcal = calendar.Calendar(inputs["startDay"])
          days = [calendar.day_name[i] for i in glcal.iterweekdays()]
          dts = []
          dmt = []
          for i in glcal.itermonthdates(cyear, cmonth):
               dts.append( i.day )
               dmt.append( i.month )
          
          numdays = len(dts)
          
          colorsm = {"priormonth": "Orchid", "thisbefore": "Aqua",  "today": "Yellow",  "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", "calSclr": "red" }

          tdy = []
          for i in range(0, 42,1):
               tdy.append({"bgtclr":"white","bgeclr":"white", "dnum":0, "devt":-1, "dev1t":"", "dev1c":"gray85", "dev1e":"",  "dev2t":"", "dev2c":"gray85", "dev2e":"", "dev3t":"", "dev3c":"gray85", "dev3e":"", "dev4t":"", "dev4c":"grey85", "dev4e":"", })

          for i in range(0, numdays, 1):
               tdy[i]["dnum"] = dts[i]
               if (dmt[i] < cmonth):
                    tdy[i]["bgtclr"] = colorsm["priormonth"]
                    tdy[i]["bgeclr"] = colorsm["priormonth"]
               elif (dmt[i] > cmonth ):
                    tdy[i]["bgtclr"] = colorsm["nextmonth"]
                    tdy[i]["bgeclr"] = colorsm["nextmonth"]
               else:
                    if (dts[i] < cday):
                         tdy[i]["bgtclr"] = colorsm["thisbefore"]
                         tdy[i]["beeclr"] = colorsm["thisbefore"]
                    elif (dts[i] == cday):
                         tdy[i]["bgtclr"] = colorsm["today"]
                         tdy[i]["beeclr"] = colorsm["today"]
                    else:
                         tdy[i]["bgtclr"] = colorsm["thismonth"]
                         tdy[i]["beeclr"] = colorsm["thismonth"]
                    

          for  c in range(8):
               self.columnconfigure(c, pad=3)

          for r in range(38):
               self.rowconfigure(r, pad=3)
          
          tdy[4]["devt"] = 1
          tdy[4]["dev1t"] =  "Bryan Kovas B'day"
          tdy[4]["dev1c"] = pref["calCclr"]
          tdy[4]["dev1e"] = "cmd"
          tdy[6]["devt"] = 4
          tdy[6]["dev1t"] =  "Helen Birdsall B'day"
          tdy[6]["dev1c"] = pref["calCclr"]
          tdy[6]["dev1e"] = "cmd"
          tdy[6]["dev2t"] =  "Greg Kovas B'day"
          tdy[6]["dev2c"] = pref["calCclr"]
          tdy[6]["dev2e"] = "cmd"
          tdy[6]["dev3t"] =  "Brielle Balmer B'day"
          tdy[6]["dev3c"] = pref["calCclr"]
          tdy[6]["dev3e"] = "cmd"
          tdy[6]["dev4t"] =  "Andrew Noyes B'day"
          tdy[6]["dev4c"] = pref["calCclr"]
          tdy[6]["dev4e"] = "cmd"
          tdy[9]["devt"] = 0
          tdy[9]["dev1t"] =  "Ash Wednesday"
          tdy[9]["dev1c"] = pref["calAclr"]
          tdy[13]["devt"] = 0
          tdy[13]["dev1t"] =  "DST begins"
          tdy[13]["dev1c"] = pref["calBclr"]
          tdy[14]["devt"] = 0
          tdy[14]["dev1t"] =  "Lent 1st Sunday"
          tdy[14]["dev1c"] = pref["calAclr"]
          tdy[21]["devt"] = 0
          tdy[21]["dev1t"] =  "Lent 2nd Sunday"
          tdy[21]["dev1c"] = pref["calAclr"]
          tdy[28]["devt"] = 0
          tdy[28]["dev1t"] =  "Lent 3rd Sunday"
          tdy[28]["dev1c"] = pref["calAclr"]
          
          #=========================================================================================================
          #Ending of definitions.  Need to remember how to split this into a seperate area that invokes MCalendar
          #=========================================================================================================


          #Window Display
          self.master.title(hd.get("loc"))
          ct = Label(self,text=hdr.get("name")+"'s "+hdr.get("page"), justify=CENTER).grid(row=0, columnspan=8, sticky=W+E)

          #Header Display
          
          wom = Label(self, text="Week", font='serif, 10', bg="white", fg="black", height=1, width=6, borderwidth=3, relief="raised").grid(row=1, column=0)
          for x in range(7):
               dow = Label(self, text=days[x], font='serif, 10', bg="white", fg="black", height=1, width=17, borderwidth=3, relief="raised").grid(row=1, column=x+1)

          
          # Weeks Display
          for r in range(1, cal.get("calrows")+1,1):
               wom =  Label(self, text=cal.get("startwk")+(r-1), background="white", foreground="black", width=8,  borderwidth=3, relief="raised").grid(row=2+((r-1)*5), column=0)
               for d in range(1,8,1):
                    dow = Label(self, text=tdy[(((r-1)*7)+(d-1))].get("dnum"),background=tdy[(((r-1)*7)+(d-1))].get("bgtclr"), width=17, relief="groove").grid(row=(2+((r-1)*5)), column=d)
                    if len(tdy[(((r-1)*7)+(d-1))].get("dev1e")) >0:
                         dow1 = Button(self, text=tdy[(((r-1)*7)+(d-1))].get("dev1t"), bg=tdy[(((r-1)*7)+(d-1))].get("dev1c"), width=15, state=NORMAL, command="").grid(row=(3+((r-1)*5)), column=d)
                    else:
                         dow1 = Label(self, text=tdy[(((r-1)*7)+(d-1))].get("dev1t"), background=tdy[(((r-1)*7)+(d-1))].get("dev1c"), width=17, relief="ridge").grid(row=(3+((r-1)*5)), column=d)
                    if len(tdy[(((r-1)*7)+(d-1))].get("dev2e")) >0:
                         dow2 = Button(self, text=tdy[(((r-1)*7)+(d-1))].get("dev2t"), bg=tdy[(((r-1)*7)+(d-1))].get("dev2c"), width=15, state=NORMAL, command="").grid(row=(4+((r-1)*5)), column=d)
                    else:
                         dow2 = Label(self, text=tdy[(((r-1)*7)+(d-1))].get("dev2t"), background=tdy[(((r-1)*7)+(d-1))].get("dev2c"), width=17, relief="ridge").grid(row=(4+((r-1)*5)), column=d)
                    if len(tdy[(((r-1)*7)+(d-1))].get("dev3e")) >0:
                         dow3 = Button(self, text=tdy[(((r-1)*7)+(d-1))].get("dev3t"), bg=tdy[(((r-1)*7)+(d-1))].get("dev3c"), width=15, state=NORMAL, command="").grid(row=(5+((r-1)*5)), column=d)
                    else:
                         dow3 = Label(self, text=tdy[(((r-1)*7)+(d-1))].get("dev3t"), background=tdy[(((r-1)*7)+(d-1))].get("dev3c"), width=17, relief="ridge").grid(row=(5+((r-1)*5)), column=d)
                    if len(tdy[(((r-1)*7)+(d-1))].get("dev4e")) >0:
                         dow4 = Button(self, text=tdy[(((r-1)*7)+(d-1))].get("dev4t"), bg=tdy[(((r-1)*7)+(d-1))].get("dev4c"), width=15, state=NORMAL, command="").grid(row=(6+((r-1)*5)), column=d)
                    else:
                         dow4 = Label(self, text=tdy[(((r-1)*7)+(d-1))].get("dev4t"), background=tdy[(((r-1)*7)+(d-1))].get("dev4c"), width=17, relief="ridge").grid(row=(6+((r-1)*5)), column=d)

          
          #Bottom of Page

          cb = Label(self,text="Legend").grid(row=32, column=4)

          day1 = Label(self, text="Prior Month", background=colorsm["priormonth"], relief="raised").grid(row=33, column=0)
          day2 = Label(self, text="This Month Prior to today", background=colorsm["thisbefore"], width=30, relief="raised").grid(row=33, column=1, columnspan=2)
          day3 = Label(self, text="Today", background=colorsm["today"],width=17, relief="raised").grid(row=33, column=3)
          day4 = Label(self, text="This Month after today", background=colorsm["thismonth"],width=30, relief="raised").grid(row=33, column=4, columnspan=2)
          day5 = Label(self, text="Next Month", background=colorsm["nextmonth"],width=17, relief="raised").grid(row=33, column=6)
          day6 = Label(self, text="Site Down", background=colorsm["site"], width=17, relief="raised").grid(row=33, column=7)
          
          ca = Label(self, text="Calendars in Use")
          ca.grid(row=34, column=4)

          cal1 = Label(self, text=cal.get("calAt"), background=pref["calAclr"], width=17, relief="raised").grid(row=35, column=1)
          cal2 = Label(self, text=cal.get("calBt"), background=pref["calBclr"], width=17, relief="raised").grid(row=35, column=2)
          cal3 = Label(self, text=cal.get("calCt"), background=pref["calCclr"], width=17, relief="raised").grid(row=35, column=3)
          cal4 = Label(self, text=cal.get("calDt"), background=pref["calDclr"], width=17, relief="raised").grid(row=35, column=4)
          cal5 = Label(self, text=cal.get("calEt"), background=pref["calEclr"], width=17, relief="raised").grid(row=35, column=5)
          cal6 = Label(self, text="Site", background="red", width=17, relief="raised").grid(row=35, column=6)


          cc = Label(self)
          cc.grid(row=36, columnspan=8,  sticky=W+E)

          brt = Button(self,text="Return", command="").grid(row=37, column=0)
          lbl1 = Label(self, text=" ").grid(row=37,column=1)
          bbk = Button(self,text="Prior Month", command="").grid(row=37, column=3)
          bpp = Button(self, text="Print Page", command="").grid(row=37, column=4)
          bnm = Button(self,text="Next Month", command="").grid(row=37, column=5)
          self.pack()


def main():

    root = Tk()
    app = MCalendar()
    root.mainloop()


if __name__ == '__main__':
    main()
