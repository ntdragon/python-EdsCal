#!/usr/bin/env python3

"""
calender ui using TCL/TK to match what is on gift exchange
One of the goals is to use the same variable structure as the Jinja-HTML versions.

Author: Edward Birdsall

Variables:
     hd:  Web/TC/Tk page
     hdr: dictionary with calendar header infomration
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
     dts = list of day numbers used to set up tdy[x]["dnum"]


"""
from calendar import *
from tkinter import *

class MCalendar(Frame):

     def __init__(self):
          super().__init__()

          self.initUI()

     def initUI(self):
          #=========================================================================================================
          #Begining of definitions.  Need to remember how to split this into a seperate area that invokes MCalendar
          #=========================================================================================================
          hd = {"loc":"Month Calendar"}
          hdr = { "name":"Ed",  "page":"March 2019 Calendar", "today":"Saturday  March  2, 2019" }


          days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
          colorsm = {"priormonth": "Orchid", "thisbefore": "Aqua",  "today": "Yellow",  "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", "calSclr": "red" }
          cal = {"month":"March", "year":"2019", "startwk":8,"calrows":5, "calAt":"Liturgical", "calBt":"US Holidays","calCt":"Birdsall Family", "calDt":"Kirkup Family", "calEt":""}
          pref = {  "startDay":1,  "calAclr": "yellowgreen",  "calBclr": "lightsteelblue",  "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "purple"}
          dts = [25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7  ]
          tdy = []
          for i in range(0, 42,1):
               tdy.append({"bgtclr":"white","bgeclr":"white", "dnum":0, "devt":-1, "dev1t":"", "dev1c":"gray90",  "dev2t":"", "dev2c":"gray90",  "dev3t":"", "dev3c":"gray90",  "dev4t":"", "dev4c":"gray90", })

          for i in range(0, 4):
               tdy[i]["bgtclr"] = colorsm["priormonth"]
               tdy[i]["bgeclr"] = colorsm["priormonth"]

          for i in range(35, 42):
               tdy[i]["bgtclr"] = colorsm["nextmonth"]
               tdy[i]["bgeclr"] = colorsm["nextmonth"]

          for i in range(0,42,1):
               tdy[i]["dnum"] = dts[i]
               
          tdy[4]["bgtclr"] = colorsm["thisbefore"]
          tdy[4]["beeclr"] = colorsm["thisbefore"]
          tdy[5]["bgtclr"] = colorsm["today"]
          tdy[5]["beeclr"] = colorsm["today"]

          for  c in range(8):
               self.columnconfigure(c, pad=3)

          for r in range(38):
               self.rowconfigure(r, pad=3)
          
          tdy[4]["devt"] = 1
          tdy[4]["dev1t"] =  "Bryan Kovas B'day"
          tdy[4]["dev1c"] = pref["calCclr"]
          tdy[6]["devt"] = 1
          tdy[6]["dev1t"] =  "Helen Birdsall B'day"
          tdy[6]["dev1c"] = pref["calCclr"]
          tdy[7]["devt"] = 3
          tdy[7]["dev1t"] =  "Greg Kovas B'day"
          tdy[7]["dev1c"] = pref["calCclr"]
          tdy[7]["dev2t"] =  "Brielle Balmer B'day"
          tdy[7]["dev2c"] = pref["calCclr"]
          tdy[7]["dev3t"] =  "Andrew Noyes B'day"
          tdy[7]["dev3c"] = pref["calCclr"]

          tdy[9]["devt"] = 1
          tdy[9]["dev1t"] =  "Ash Wednesday"
          tdy[9]["dev1c"] = pref["calAclr"]
          tdy[13]["devt"] = 1
          tdy[13]["dev1t"] =  "DST begins"
          tdy[13]["dev1c"] = pref["calBclr"]

          #=========================================================================================================
          #Ending of definitions.  Need to remember how to split this into a seperate area that invokes MCalendar
          #=========================================================================================================


          #Window Display
          self.master.title(hd.get("loc"))
          ct = Label(self,text=hdr.get("name")+"'s "+hdr.get("page"), justify=CENTER).grid(row=0, columnspan=8, sticky=W+E)

          #Header Display
          
          wom = Label(self, text="Week", font='serif, 10', bg="white", fg="black", height=1, width=6, borderwidth=3, relief="raised").grid(row=1, column=0)
          for x in range(7):
               dow = Label(self, text=days[pref.get("startDay")+x], font='serif, 10', bg="white", fg="black", height=1, width=17, borderwidth=3, relief="raised").grid(row=1, column=x+1)
          
          # Weeks Display
          for r in range(1, cal.get("calrows")+1,1):
               wom =  Label(self, text=cal.get("startwk")+(r-1), background="white", foreground="black", width=8, relief="raised").grid(row=2+((r-1)*5), column=0)
               for d in range(1,8,1):
                    dow = Label(self, text=tdy[(((r-1)*7)+(d-1))].get("dnum"),background=tdy[(((r-1)*7)+(d-1))].get("bgtclr"), width=17, relief="groove").grid(row=(2+((r-1)*5)), column=d)
                    dow1 = Label(self, text=tdy[(((r-1)*7)+(d-1))].get("dev1t"), background=tdy[(((r-1)*7)+(d-1))].get("dev1c"), width=17, relief="ridge").grid(row=(3+((r-1)*5)), column=d)
                    dow2 = Label(self, text=tdy[(((r-1)*7)+(d-1))].get("dev2t"), background=tdy[(((r-1)*7)+(d-1))].get("dev2c"), width=17, relief="ridge").grid(row=(4+((r-1)*5)), column=d)
                    dow3 = Label(self, text=tdy[(((r-1)*7)+(d-1))].get("dev3t"), background=tdy[(((r-1)*7)+(d-1))].get("dev3c"), width=17, relief="ridge").grid(row=(5+((r-1)*5)), column=d)
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
