#!/usr/bin/env python3

"""
try1 first attempts to write a calender ui using TCL/TK to match what is on gift exchange initially
One of the goals is to use the same variable structure as the Jinja-HTML versions.

Author: Edward Birdsall

Variables:
     hd:
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
from tkinter import *
#from tkinter import Tk, W, E, BOTH
#from tkinter.ttk import Frame, Button, Entry, Style, Label
#from tkinter.ttk import Frame, Button, Entry, Label

class MGCalendar4(Frame):

     def __init__(self):
          super().__init__()

          self.initUI()

     def initUI(self):


          hd = {"loc":"Month Calendar"}
          hdr = { "name":"Ed",  "page":"March 2019 Calendar", "today":"Saturday  March  2, 2019" }


          days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
          colorsm = {"priormonth": "Orchid", "thisbefore": "Aqua",  "today": "Yellow",  "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", "calSclr": "red" }
          cal = {"month":"March", "year":"2019", "startwk":10,"calrows":5, "calAt":"Liturgical", "calBt":"US Holidays","calCt":"Birdsall Family", "calDt":"Kirkup Family", "calEt":""}
          pref = {  "startDay":1,  "calAclr": "yellowgreen",  "calBclr": "lightsteelblue",  "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "purple"}
          dts = [25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7  ]
          tdy = []
          for i in range(0, 42,1):
               tdy.append({"bgtclr":"white","bgeclr":"white", "dnum":0, "devt":-1, "devt1t":"", "devt1c":"",  "devt2t":"", "devt2c":"",  "devt3t":"", "devt3c":"",  "devt4t":"", "devt4c":"", })

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
          tdy[6]["devt"] = 3
          tdy[6]["dev1t"] =  "Greg Kovas B'day"
          tdy[6]["dev1c"] = pref["calCclr"]
          tdy[6]["dev2t"] =  "Brielle Balmer B'day"
          tdy[6]["dev2c"] = pref["calCclr"]
          tdy[6]["dev3t"] =  "Andrew Noyes B'day"
          tdy[6]["dev3c"] = pref["calCclr"]

          tdy[9]["devt"] = 1
          tdy[9]["dev1t"] =  "Ash Wednesday"
          tdy[9]["dev1c"] = pref["calAclr"]
          tdy[13]["devt"] = 1
          tdy[13]["dev1t"] =  "DST begins"
          tdy[13]["dev1c"] = pref["calBclr"]
          tdy[21]["devt"] = 1

          """
          caldy0 = Style()
          caldy0.configure('CD0.TButton', background="white", foreground='black')
          caldy1 = Style()
          caldy1.configure('CD1.TButton', background=colorsm.get("priormonth"), foreground='black')
          caldy2 = Style()
          caldy2.configure('CD2.TButton', background=colorsm.get("thisbefore"), foreground='black')
          caldy3 = Style()
          caldy3.configure('CD3.TButton', background=colorsm.get("today"), foreground='black')
          caldy4 = Style()
          caldy4.configure('CD4.TButton', background=colorsm.get("thismonth"), foreground='black')
          caldy5 = Style()
          caldy5.configure('CD5.TButton', background=colorsm.get("nextmonth"), foreground='black')
          caldy6 = Style()
          caldy6.configure('CD6.TButton', background=colorsm.get("site"), foreground='black')


          buttonStyle = Style()
          buttonStyle.configure(style='a.TButton', background="white", foreground='black')

          cal1 = Style()
          cal1.configure('C1.TButton', background=pref.get("calAclr"), foreground='black')
          cal2 = Style()
          cal2.configure('C2.TButton', background=pref.get("calBclr"), foreground='black')
          cal3 = Style()
          cal3.configure('C3.TButton', background=pref.get("calCclr"), foreground='black')
          cal4 = Style()
          cal4.configure('C4.TButton', background=pref.get("calDclr"), foreground='black')
          cal5 = Style()
          cal5.configure('C5.TButton', background=pref.get("calEclr"), foreground='black')
          cal6 = Style()
          cal6.configure('C6.TButton', background="red", foreground='black')
          
          #Calendar Button Styles
          cbs = []
          for i in range(0, 42,1):
               cbs.append({"r1":"buttonStyle.style", "r2":buttonStyle, "r3":buttonStyle, "r4":buttonStyle, })
          """
          self.master.title(hd.get("loc"))
          ct = Label(self,text=hdr.get("name")+"'s "+hdr.get("page"), justify=CENTER).grid(row=0, columnspan=8, sticky=W+E)

          #Header Display
          
          #dow = [] #List assignment index is out of range??
          
          wom = Label(self, text="Week", font='serif, 10', bg="white", fg="black", height=1, width=6, borderwidth=3).grid(row=1, column=0)
          for x in range(6):
               dow[x] = Label(self, text=days[pref.get("startDay")+x], font='serif, 10', bg="white", fg="black", height=1, width=17, borderwidth=3).grid(row=1, column=x+1)
          
          #dow2 = Label(self, text=days[pref.get("startDay")+1], font='serif, 10', bg="white", fg="black", height=1, width=17, borderwidth=3).grid(row=1, column=2)
          #dow3 = Label(self, text=days[pref.get("startDay")+2], font='serif, 10', bg="white", fg="black", height=1, width=17, borderwidth=3).grid(row=1, column=3)
          #dow4 = Label(self, text=days[pref.get("startDay")+3], font='serif, 10', bg="white", fg="black", height=1, width=17, borderwidth=3).grid(row=1, column=4)
          #dow5 = Label(self, text=days[pref.get("startDay")+4], font='serif, 10', bg="white", fg="black", height=1, width=17, borderwidth=3).grid(row=1, column=5)
          #dow6 = Label(self, text=days[pref.get("startDay")+5], font='serif, 10', bg="white", fg="black", height=1, width=17, borderwidth=3).grid(row=1, column=6)
          #dow7 = Label(self, text=days[pref.get("startDay")+6], font='serif, 10', bg="white", fg="black", height=1, width=17).grid(row=1, column=7)


          #Week 1 Display

          r1wom = Label(self, text=cal.get("startwk"), background="white", foreground="black", width=8).grid(row=2, column=0)
          r1dow1 = Label(self, text=tdy[0].get("dnum"),background=tdy[0].get("bgtclr"), width=17).grid(row=2, column=1)
          r1dow2 = Label(self, text=tdy[1].get("dnum"),background=tdy[1].get("bgtclr"), width=17).grid(row=2, column=2)
          r1dow3 = Label(self, text=tdy[2].get("dnum"),background=tdy[2].get("bgtclr"), width=17).grid(row=2, column=3)
          r1dow4 = Label(self, text=tdy[3].get("dnum"),background=tdy[3].get("bgtclr"), width=17).grid(row=2, column=4)
          r1dow5 = Label(self, text=tdy[4].get("dnum"),background=tdy[4].get("bgtclr"), width=17).grid(row=2, column=5)
          r1dow6 = Label(self, text=tdy[5].get("dnum"),background=tdy[5].get("bgtclr"), width=17).grid(row=2, column=6)
          r1dow7 = Label(self, text=tdy[6].get("dnum"),background=tdy[6].get("bgtclr"), width=17).grid(row=2, column=7)

          r2dow1 = Button(self, text=tdy[0].get("dev1t"), bg=tdy[0].get("dev1c"), width=15, state=NORMAL).grid(row=3, column=1)
          r2dow2 = Button(self, text=tdy[1].get("dev1t"), bg=tdy[1].get("dev1c"), width=15, state=NORMAL).grid(row=3, column=2)
          r2dow3 = Button(self, text=tdy[2].get("dev1t"), bg=tdy[2].get("dev1c"), width=15, state=NORMAL).grid(row=3, column=3)
          r2dow4 = Button(self, text=tdy[3].get("dev1t"), bg=tdy[3].get("dev1c"), width=15, state=NORMAL).grid(row=3, column=4)
          r2dow5 = Button(self, text=tdy[4].get("dev1t"), bg=tdy[4].get("dev1c"), width=15, state=NORMAL).grid(row=3, column=5)
          r2dow6 = Button(self, text=tdy[5].get("dev1t"), bg=tdy[5].get("dev1c"), width=15, state=NORMAL).grid(row=3, column=6)
          r2dow7 = Button(self, text=tdy[6].get("dev1t"), bg=tdy[6].get("dev1c"), width=15, state=NORMAL).grid(row=3, column=7)

          r3dow1 = Button(self, text=tdy[0].get("dev2t"), bg=tdy[0].get("dev2c"), width=15, state=NORMAL).grid(row=4, column=1)
          r3dow2 = Button(self, text=tdy[1].get("dev2t"), bg=tdy[1].get("dev2c"), width=15, state=NORMAL).grid(row=4, column=2)
          r3dow3 = Button(self, text=tdy[2].get("dev2t"), bg=tdy[2].get("dev2c"), width=15, state=NORMAL).grid(row=4, column=3)
          r3dow4 = Button(self, text=tdy[3].get("dev2t"), bg=tdy[3].get("dev2c"), width=15, state=NORMAL).grid(row=4, column=4)
          r3dow5 = Button(self, text=tdy[4].get("dev2t"), bg=tdy[4].get("dev2c"), width=15, state=NORMAL).grid(row=4, column=5)
          r3dow6 = Button(self, text=tdy[5].get("dev2t"), bg=tdy[5].get("dev2c"), width=15, state=NORMAL).grid(row=4, column=6)
          r3dow7 = Button(self, text=tdy[6].get("dev2t"), bg=tdy[6].get("dev2c"), width=15, state=NORMAL).grid(row=4, column=7)

          r4dow1 = Button(self, text=tdy[0].get("dev3t"), bg=tdy[0].get("dev3c"), width=15, state=NORMAL).grid(row=5, column=1)
          r4dow2 = Button(self, text=tdy[1].get("dev3t"), bg=tdy[1].get("dev3c"), width=15, state=NORMAL).grid(row=5, column=2)
          r4dow3 = Button(self, text=tdy[2].get("dev3t"), bg=tdy[2].get("dev3c"), width=15, state=NORMAL).grid(row=5, column=3)
          r4dow4 = Button(self, text=tdy[3].get("dev3t"), bg=tdy[3].get("dev3c"), width=15, state=NORMAL).grid(row=5, column=4)
          r4dow5 = Button(self, text=tdy[4].get("dev3t"), bg=tdy[4].get("dev3c"), width=15, state=NORMAL).grid(row=5, column=5)
          r4dow6 = Button(self, text=tdy[5].get("dev3t"), bg=tdy[5].get("dev3c"), width=15, state=NORMAL).grid(row=5, column=6)
          r4dow7 = Button(self, text=tdy[6].get("dev3t"), bg=tdy[6].get("dev3c"), width=15, state=NORMAL).grid(row=5, column=7)

          r5dow1 = Button(self, text=tdy[0].get("dev4t"), bg=tdy[0].get("dev4c"), width=15, state=NORMAL).grid(row=6, column=1)
          r5dow2 = Button(self, text=tdy[1].get("dev4t"), bg=tdy[1].get("dev4c"), width=15, state=NORMAL).grid(row=6, column=2)
          r5dow3 = Button(self, text=tdy[2].get("dev4t"), bg=tdy[2].get("dev4c"), width=15, state=NORMAL).grid(row=6, column=3)
          r5dow4 = Button(self, text=tdy[3].get("dev4t"), bg=tdy[3].get("dev4c"), width=15, state=NORMAL).grid(row=6, column=4)
          r5dow5 = Button(self, text=tdy[4].get("dev4t"), bg=tdy[4].get("dev4c"), width=15, state=NORMAL).grid(row=6, column=5)
          r5dow6 = Button(self, text=tdy[5].get("dev4t"), bg=tdy[5].get("dev4c"), width=15, state=NORMAL).grid(row=6, column=6)
          r5dow7 = Button(self, text=tdy[6].get("dev4t"), bg=tdy[6].get("dev4c"), width=15, state=NORMAL).grid(row=6, column=7)

          #Week 2 Display

          r6wom = Label(self, text=cal.get("startwk")+1, background="white", foreground="black", width=8).grid(row=7, column=0)
          r6dow1 = Label(self, text=tdy[7].get("dnum"),background=tdy[7].get("bgtclr"), width=17).grid(row=7, column=1)
          r6dow2 = Label(self, text=tdy[8].get("dnum"),background=tdy[8].get("bgtclr"), width=17).grid(row=7, column=2)
          r6dow3 = Label(self, text=tdy[9].get("dnum"),background=tdy[9].get("bgtclr"), width=17).grid(row=7, column=3)
          r6dow4 = Label(self, text=tdy[10].get("dnum"),background=tdy[10].get("bgtclr"), width=17).grid(row=7, column=4)
          r6dow5 = Label(self, text=tdy[11].get("dnum"),background=tdy[11].get("bgtclr"), width=17).grid(row=7, column=5)
          r6dow6 = Label(self, text=tdy[12].get("dnum"),background=tdy[12].get("bgtclr"), width=17).grid(row=7, column=6)
          r6dow7 = Label(self, text=tdy[13].get("dnum"),background=tdy[13].get("bgtclr"), width=17).grid(row=7, column=7)

          r7dow1 = Button(self, text=tdy[7].get("dev1t"), bg=tdy[7].get("dev1c"), width=15, state=NORMAL).grid(row=8, column=1)
          r7dow2 = Button(self, text=tdy[8].get("dev1t"), bg=tdy[8].get("dev1c"), width=15, state=NORMAL).grid(row=8, column=2)
          r7dow3 = Button(self, text=tdy[9].get("dev1t"), bg=tdy[9].get("dev1c"), width=15, state=NORMAL).grid(row=8, column=3)
          r7dow4 = Button(self, text=tdy[10].get("dev1t"), bg=tdy[10].get("dev1c"), width=15, state=NORMAL).grid(row=8, column=4)
          r7dow5 = Button(self, text=tdy[11].get("dev1t"), bg=tdy[11].get("dev1c"), width=15, state=NORMAL).grid(row=8, column=5)
          r7dow6 = Button(self, text=tdy[12].get("dev1t"), bg=tdy[12].get("dev1c"), width=15, state=NORMAL).grid(row=8, column=6)
          r7dow7 = Button(self, text=tdy[13].get("dev1t"), bg=tdy[13].get("dev1c"), width=15, state=NORMAL).grid(row=8, column=7)

          r8dow1 = Button(self, text=tdy[7].get("dev2t"), bg=tdy[7].get("dev2c"), width=15, state=NORMAL).grid(row=9, column=1)
          r8dow2 = Button(self, text=tdy[8].get("dev2t"), bg=tdy[8].get("dev2c"), width=15, state=NORMAL).grid(row=9, column=2)
          r8dow3 = Button(self, text=tdy[9].get("dev2t"), bg=tdy[9].get("dev2c"), width=15, state=NORMAL).grid(row=9, column=3)
          r8dow4 = Button(self, text=tdy[10].get("dev2t"), bg=tdy[10].get("dev2c"), width=15, state=NORMAL).grid(row=9, column=4)
          r8dow5 = Button(self, text=tdy[11].get("dev2t"), bg=tdy[11].get("dev2c"), width=15, state=NORMAL).grid(row=9, column=5)
          r8dow6 = Button(self, text=tdy[12].get("dev2t"), bg=tdy[12].get("dev2c"), width=15, state=NORMAL).grid(row=9, column=6)
          r8dow7 = Button(self, text=tdy[13].get("dev2t"), bg=tdy[13].get("dev2c"), width=15, state=NORMAL).grid(row=9, column=7)

          r9dow1 = Button(self, text=tdy[7].get("dev3t"), bg=tdy[7].get("dev3c"), width=15, state=NORMAL).grid(row=10, column=1)
          r9dow2 = Button(self, text=tdy[8].get("dev3t"), bg=tdy[8].get("dev3c"), width=15, state=NORMAL).grid(row=10, column=2)
          r9dow3 = Button(self, text=tdy[9].get("dev3t"), bg=tdy[9].get("dev3c"), width=15, state=NORMAL).grid(row=10, column=3)
          r9dow4 = Button(self, text=tdy[10].get("dev3t"), bg=tdy[10].get("dev3c"), width=15, state=NORMAL).grid(row=10, column=4)
          r9dow5 = Button(self, text=tdy[11].get("dev3t"), bg=tdy[11].get("dev3c"), width=15, state=NORMAL).grid(row=10, column=5)
          r9dow6 = Button(self, text=tdy[12].get("dev3t"), bg=tdy[12].get("dev3c"), width=15, state=NORMAL).grid(row=10, column=6)
          r9dow7 = Button(self, text=tdy[13].get("dev3t"), bg=tdy[13].get("dev3c"), width=15, state=NORMAL).grid(row=10, column=7)

          r10dow1 = Button(self, text=tdy[7].get("dev4t"), bg=tdy[7].get("dev4c"), width=15, state=NORMAL).grid(row=11, column=1)
          r10dow2 = Button(self, text=tdy[8].get("dev4t"), bg=tdy[8].get("dev4c"), width=15, state=NORMAL).grid(row=11, column=2)
          r10dow3 = Button(self, text=tdy[9].get("dev4t"), bg=tdy[9].get("dev4c"), width=15, state=NORMAL).grid(row=11, column=3)
          r10dow4 = Button(self, text=tdy[10].get("dev4t"), bg=tdy[10].get("dev4c"), width=15, state=NORMAL).grid(row=11, column=4)
          r10dow5 = Button(self, text=tdy[11].get("dev4t"), bg=tdy[11].get("dev4c"), width=15, state=NORMAL).grid(row=11, column=5)
          r10dow6 = Button(self, text=tdy[12].get("dev4t"), bg=tdy[12].get("dev4c"), width=15, state=NORMAL).grid(row=11, column=6)
          r10dow7 = Button(self, text=tdy[13].get("dev4t"), bg=tdy[13].get("dev4c"), width=15, state=NORMAL).grid(row=11, column=7)

          #Week 3 Display

          r11wom = Label(self, text=cal.get("startwk")+2, background="white", foreground="black", width=8).grid(row=12, column=0)
          r11dow1 = Label(self, text=tdy[14].get("dnum"),background=tdy[14].get("bgtclr"), width=17).grid(row=12, column=1)
          r11dow2 = Label(self, text=tdy[15].get("dnum"),background=tdy[15].get("bgtclr"), width=17).grid(row=12, column=2)
          r11dow3 = Label(self, text=tdy[16].get("dnum"),background=tdy[16].get("bgtclr"), width=17).grid(row=12, column=3)
          r11dow4 = Label(self, text=tdy[17].get("dnum"),background=tdy[17].get("bgtclr"), width=17).grid(row=12, column=4)
          r11dow5 = Label(self, text=tdy[18].get("dnum"),background=tdy[18].get("bgtclr"), width=17).grid(row=12, column=5)
          r11dow6 = Label(self, text=tdy[19].get("dnum"),background=tdy[19].get("bgtclr"), width=17).grid(row=12, column=6)
          r11dow7 = Label(self, text=tdy[20].get("dnum"),background=tdy[20].get("bgtclr"), width=17).grid(row=12, column=7)

          r12dow1 = Button(self, text=tdy[14].get("dev1t"), bg=tdy[14].get("dev1c"), width=15, state=NORMAL).grid(row=13, column=1)
          r12dow2 = Button(self, text=tdy[15].get("dev1t"), bg=tdy[15].get("dev1c"), width=15, state=NORMAL).grid(row=13, column=2)
          r12dow3 = Button(self, text=tdy[16].get("dev1t"), bg=tdy[16].get("dev1c"), width=15, state=NORMAL).grid(row=13, column=3)
          r12dow4 = Button(self, text=tdy[17].get("dev1t"), bg=tdy[17].get("dev1c"), width=15, state=NORMAL).grid(row=13, column=4)
          r12dow5 = Button(self, text=tdy[18].get("dev1t"), bg=tdy[18].get("dev1c"), width=15, state=NORMAL).grid(row=13, column=5)
          r12dow6 = Button(self, text=tdy[19].get("dev1t"), bg=tdy[19].get("dev1c"), width=15, state=NORMAL).grid(row=13, column=6)
          r12dow7 = Button(self, text=tdy[20].get("dev1t"), bg=tdy[20].get("dev1c"), width=15, state=NORMAL).grid(row=13, column=7)

          r13dow1 = Button(self, text=tdy[14].get("dev2t"), bg=tdy[14].get("dev2c"), width=15, state=NORMAL).grid(row=14, column=1)
          r13dow2 = Button(self, text=tdy[15].get("dev2t"), bg=tdy[15].get("dev2c"), width=15, state=NORMAL).grid(row=14, column=2)
          r13dow3 = Button(self, text=tdy[16].get("dev2t"), bg=tdy[16].get("dev2c"), width=15, state=NORMAL).grid(row=14, column=3)
          r13dow4 = Button(self, text=tdy[17].get("dev2t"), bg=tdy[19].get("dev2c"), width=15, state=NORMAL).grid(row=14, column=4)
          r13dow5 = Button(self, text=tdy[18].get("dev2t"), bg=tdy[18].get("dev2c"), width=15, state=NORMAL).grid(row=14, column=5)
          r13dow6 = Button(self, text=tdy[19].get("dev2t"), bg=tdy[13].get("dev2c"), width=15, state=NORMAL).grid(row=14, column=6)
          r13dow7 = Button(self, text=tdy[20].get("dev2t"), bg=tdy[20].get("dev2c"), width=15, state=NORMAL).grid(row=14, column=7)

          r14dow1 = Button(self, text=tdy[14].get("dev3t"), bg=tdy[14].get("dev3c"), width=15, state=NORMAL).grid(row=15, column=1)
          r14dow2 = Button(self, text=tdy[15].get("dev3t"), bg=tdy[15].get("dev3c"), width=15, state=NORMAL).grid(row=15, column=2)
          r14dow3 = Button(self, text=tdy[16].get("dev3t"), bg=tdy[16].get("dev3c"), width=15, state=NORMAL).grid(row=15, column=3)
          r14dow4 = Button(self, text=tdy[17].get("dev3t"), bg=tdy[17].get("dev3c"), width=15, state=NORMAL).grid(row=15, column=4)
          r14dow5 = Button(self, text=tdy[18].get("dev3t"), bg=tdy[18].get("dev3c"), width=15, state=NORMAL).grid(row=15, column=5)
          r14dow6 = Button(self, text=tdy[19].get("dev3t"), bg=tdy[19].get("dev3c"), width=15, state=NORMAL).grid(row=15, column=6)
          r14dow7 = Button(self, text=tdy[20].get("dev3t"), bg=tdy[20].get("dev3c"), width=15, state=NORMAL).grid(row=15, column=7)

          r15dow1 = Button(self, text=tdy[14].get("dev4t"), bg=tdy[14].get("dev4c"), width=15, state=NORMAL).grid(row=16, column=1)
          r15dow2 = Button(self, text=tdy[15].get("dev4t"), bg=tdy[15].get("dev4c"), width=15, state=NORMAL).grid(row=16, column=2)
          r15dow3 = Button(self, text=tdy[16].get("dev4t"), bg=tdy[16].get("dev4c"), width=15, state=NORMAL).grid(row=16, column=3)
          r15dow4 = Button(self, text=tdy[17].get("dev4t"), bg=tdy[17].get("dev4c"), width=15, state=NORMAL).grid(row=16, column=4)
          r15dow5 = Button(self, text=tdy[18].get("dev4t"), bg=tdy[18].get("dev4c"), width=15, state=NORMAL).grid(row=16, column=5)
          r15dow6 = Button(self, text=tdy[19].get("dev4t"), bg=tdy[19].get("dev4c"), width=15, state=NORMAL).grid(row=16, column=6)
          r15dow7 = Button(self, text=tdy[20].get("dev4t"), bg=tdy[20].get("dev4c"), width=15, state=NORMAL).grid(row=16, column=7)

          #Week 4 Display

          r16wom = Label(self, text=cal.get("startwk")+3, background="white", foreground="black", width=8).grid(row=17, column=0)
          r16dow1 = Label(self, text=tdy[21].get("dnum"),background=tdy[21].get("bgtclr"), width=17).grid(row=17, column=1)
          r16dow2 = Label(self, text=tdy[22].get("dnum"),background=tdy[22].get("bgtclr"), width=17).grid(row=17, column=2)
          r16dow3 = Label(self, text=tdy[23].get("dnum"),background=tdy[23].get("bgtclr"), width=17).grid(row=17, column=3)
          r16dow4 = Label(self, text=tdy[24].get("dnum"),background=tdy[24].get("bgtclr"), width=17).grid(row=17, column=4)
          r16dow5 = Label(self, text=tdy[25].get("dnum"),background=tdy[25].get("bgtclr"), width=17).grid(row=17, column=5)
          r16dow6 = Label(self, text=tdy[26].get("dnum"),background=tdy[26].get("bgtclr"), width=17).grid(row=17, column=6)
          r16dow7 = Label(self, text=tdy[27].get("dnum"),background=tdy[27].get("bgtclr"), width=17).grid(row=17, column=7)

          r17dow1 = Button(self, text=tdy[21].get("dev1t"), bg=tdy[21].get("dev1c"), width=15, state=NORMAL).grid(row=18, column=1)
          r17dow2 = Button(self, text=tdy[22].get("dev1t"), bg=tdy[22].get("dev1c"), width=15, state=NORMAL).grid(row=18, column=2)
          r17dow3 = Button(self, text=tdy[23].get("dev1t"), bg=tdy[23].get("dev1c"), width=15, state=NORMAL).grid(row=18, column=3)
          r17dow4 = Button(self, text=tdy[24].get("dev1t"), bg=tdy[24].get("dev1c"), width=15, state=NORMAL).grid(row=18, column=4)
          r17dow5 = Button(self, text=tdy[25].get("dev1t"), bg=tdy[25].get("dev1c"), width=15, state=NORMAL).grid(row=18, column=5)
          r17dow6 = Button(self, text=tdy[26].get("dev1t"), bg=tdy[26].get("dev1c"), width=15, state=NORMAL).grid(row=18, column=6)
          r17dow7 = Button(self, text=tdy[27].get("dev1t"), bg=tdy[27].get("dev1c"), width=15, state=NORMAL).grid(row=18, column=7)

          r18dow1 = Button(self, text=tdy[21].get("dev2t"), bg=tdy[21].get("dev2c"), width=15, state=NORMAL).grid(row=19, column=1)
          r18dow2 = Button(self, text=tdy[22].get("dev2t"), bg=tdy[22].get("dev2c"), width=15, state=NORMAL).grid(row=19, column=2)
          r18dow3 = Button(self, text=tdy[23].get("dev2t"), bg=tdy[23].get("dev2c"), width=15, state=NORMAL).grid(row=19, column=3)
          r18dow4 = Button(self, text=tdy[24].get("dev2t"), bg=tdy[24].get("dev2c"), width=15, state=NORMAL).grid(row=19, column=4)
          r18dow5 = Button(self, text=tdy[25].get("dev2t"), bg=tdy[25].get("dev2c"), width=15, state=NORMAL).grid(row=19, column=5)
          r18dow6 = Button(self, text=tdy[26].get("dev2t"), bg=tdy[26].get("dev2c"), width=15, state=NORMAL).grid(row=19, column=6)
          r18dow7 = Button(self, text=tdy[27].get("dev2t"), bg=tdy[27].get("dev2c"), width=15, state=NORMAL).grid(row=19, column=7)

          r19dow1 = Button(self, text=tdy[21].get("dev3t"), bg=tdy[21].get("dev3c"), width=15, state=NORMAL).grid(row=20, column=1)
          r19dow2 = Button(self, text=tdy[22].get("dev3t"), bg=tdy[22].get("dev3c"), width=15, state=NORMAL).grid(row=20, column=2)
          r19dow3 = Button(self, text=tdy[23].get("dev3t"), bg=tdy[23].get("dev3c"), width=15, state=NORMAL).grid(row=20, column=3)
          r19dow4 = Button(self, text=tdy[24].get("dev3t"), bg=tdy[24].get("dev3c"), width=15, state=NORMAL).grid(row=20, column=4)
          r19dow5 = Button(self, text=tdy[25].get("dev3t"), bg=tdy[25].get("dev3c"), width=15, state=NORMAL).grid(row=20, column=5)
          r19dow6 = Button(self, text=tdy[26].get("dev3t"), bg=tdy[26].get("dev3c"), width=15, state=NORMAL).grid(row=20, column=6)
          r19dow7 = Button(self, text=tdy[27].get("dev3t"), bg=tdy[27].get("dev3c"), width=15, state=NORMAL).grid(row=20, column=7)

          r20dow1 = Button(self, text=tdy[21].get("dev4t"), bg=tdy[21].get("dev4c"), width=15, state=NORMAL).grid(row=21, column=1)
          r20dow2 = Button(self, text=tdy[22].get("dev4t"), bg=tdy[22].get("dev4c"), width=15, state=NORMAL).grid(row=21, column=2)
          r20dow3 = Button(self, text=tdy[23].get("dev4t"), bg=tdy[23].get("dev4c"), width=15, state=NORMAL).grid(row=21, column=3)
          r20dow4 = Button(self, text=tdy[24].get("dev4t"), bg=tdy[24].get("dev4c"), width=15, state=NORMAL).grid(row=21, column=4)
          r20dow5 = Button(self, text=tdy[25].get("dev4t"), bg=tdy[25].get("dev4c"), width=15, state=NORMAL).grid(row=21, column=5)
          r20dow6 = Button(self, text=tdy[26].get("dev4t"), bg=tdy[26].get("dev4c"), width=15, state=NORMAL).grid(row=21, column=6)
          r20dow7 = Button(self, text=tdy[27].get("dev4t"), bg=tdy[27].get("dev4c"), width=15, state=NORMAL).grid(row=21, column=7)

          #Week 5 Display

          r21wom = Label(self, text=cal.get("startwk")+4, background="white", foreground="black", width=8).grid(row=22, column=0)
          r21dow1 = Label(self, text=tdy[28].get("dnum"),background=tdy[28].get("bgtclr"), width=17).grid(row=22, column=1)
          r21dow2 = Label(self, text=tdy[29].get("dnum"),background=tdy[29].get("bgtclr"), width=17).grid(row=22, column=2)
          r21dow3 = Label(self, text=tdy[30].get("dnum"),background=tdy[30].get("bgtclr"), width=17).grid(row=22, column=3)
          r21dow4 = Label(self, text=tdy[31].get("dnum"),background=tdy[31].get("bgtclr"), width=17).grid(row=22, column=4)
          r21dow5 = Label(self, text=tdy[32].get("dnum"),background=tdy[32].get("bgtclr"), width=17).grid(row=22, column=5)
          r21dow6 = Label(self, text=tdy[33].get("dnum"),background=tdy[33].get("bgtclr"), width=17).grid(row=22, column=6)
          r21dow7 = Label(self, text=tdy[34].get("dnum"),background=tdy[34].get("bgtclr"), width=17).grid(row=22, column=7)

          r22dow1 = Button(self, text=tdy[28].get("dev1t"), bg=tdy[28].get("dev1c"), width=15, state=NORMAL).grid(row=23, column=1)
          r22dow2 = Button(self, text=tdy[29].get("dev1t"), bg=tdy[29].get("dev1c"), width=15, state=NORMAL).grid(row=23, column=2)
          r22dow3 = Button(self, text=tdy[30].get("dev1t"), bg=tdy[30].get("dev1c"), width=15, state=NORMAL).grid(row=23, column=3)
          r22dow4 = Button(self, text=tdy[31].get("dev1t"), bg=tdy[31].get("dev1c"), width=15, state=NORMAL).grid(row=23, column=4)
          r22dow5 = Button(self, text=tdy[32].get("dev1t"), bg=tdy[32].get("dev1c"), width=15, state=NORMAL).grid(row=23, column=5)
          r22dow6 = Button(self, text=tdy[33].get("dev1t"), bg=tdy[33].get("dev1c"), width=15, state=NORMAL).grid(row=23, column=6)
          r22dow7 = Button(self, text=tdy[34].get("dev1t"), bg=tdy[34].get("dev1c"), width=15, state=NORMAL).grid(row=23, column=7)

          r23dow1 = Button(self, text=tdy[28].get("dev2t"), bg=tdy[28].get("dev2c"), width=15, state=NORMAL).grid(row=24, column=1)
          r23dow2 = Button(self, text=tdy[29].get("dev2t"), bg=tdy[29].get("dev2c"), width=15, state=NORMAL).grid(row=24, column=2)
          r23dow3 = Button(self, text=tdy[30].get("dev2t"), bg=tdy[30].get("dev2c"), width=15, state=NORMAL).grid(row=24, column=3)
          r23dow4 = Button(self, text=tdy[31].get("dev2t"), bg=tdy[31].get("dev2c"), width=15, state=NORMAL).grid(row=24, column=4)
          r23dow5 = Button(self, text=tdy[32].get("dev2t"), bg=tdy[32].get("dev2c"), width=15, state=NORMAL).grid(row=24, column=5)
          r23dow6 = Button(self, text=tdy[33].get("dev2t"), bg=tdy[33].get("dev2c"), width=15, state=NORMAL).grid(row=24, column=6)
          r23dow7 = Button(self, text=tdy[34].get("dev2t"), bg=tdy[34].get("dev2c"), width=15, state=NORMAL).grid(row=24, column=7)

          r24dow1 = Button(self, text=tdy[28].get("dev3t"), bg=tdy[28].get("dev3c"), width=15, state=NORMAL).grid(row=25, column=1)
          r24dow2 = Button(self, text=tdy[29].get("dev3t"), bg=tdy[29].get("dev3c"), width=15, state=NORMAL).grid(row=25, column=2)
          r24dow3 = Button(self, text=tdy[30].get("dev3t"), bg=tdy[30].get("dev3c"), width=15, state=NORMAL).grid(row=25, column=3)
          r24dow4 = Button(self, text=tdy[31].get("dev3t"), bg=tdy[31].get("dev3c"), width=15, state=NORMAL).grid(row=25, column=4)
          r24dow5 = Button(self, text=tdy[32].get("dev3t"), bg=tdy[32].get("dev3c"), width=15, state=NORMAL).grid(row=25, column=5)
          r24dow6 = Button(self, text=tdy[33].get("dev3t"), bg=tdy[33].get("dev3c"), width=15, state=NORMAL).grid(row=25, column=6)
          r24dow7 = Button(self, text=tdy[34].get("dev3t"), bg=tdy[34].get("dev3c"), width=15, state=NORMAL).grid(row=25, column=7)

          r25dow1 = Button(self, text=tdy[28].get("dev4t"), bg=tdy[28].get("dev4c"), width=15, state=NORMAL).grid(row=26, column=1)
          r25dow2 = Button(self, text=tdy[29].get("dev4t"), bg=tdy[29].get("dev4c"), width=15, state=NORMAL).grid(row=26, column=2)
          r25dow3 = Button(self, text=tdy[30].get("dev4t"), bg=tdy[30].get("dev4c"), width=15, state=NORMAL).grid(row=26, column=3)
          r25dow4 = Button(self, text=tdy[31].get("dev4t"), bg=tdy[31].get("dev4c"), width=15, state=NORMAL).grid(row=26, column=4)
          r25dow5 = Button(self, text=tdy[32].get("dev4t"), bg=tdy[32].get("dev4c"), width=15, state=NORMAL).grid(row=26, column=5)
          r25dow6 = Button(self, text=tdy[33].get("dev4t"), bg=tdy[33].get("dev4c"), width=15, state=NORMAL).grid(row=26, column=6)
          r25dow7 = Button(self, text=tdy[34].get("dev4t"), bg=tdy[34].get("dev4c"), width=15, state=NORMAL).grid(row=26, column=7)

          #Week 6 Display

          r26wom = Label(self, text=cal.get("startwk")+5, background="white", foreground="black", width=8).grid(row=27, column=0)
          r26dow1 = Label(self, text=tdy[35].get("dnum"),background=tdy[35].get("bgtclr"), width=17).grid(row=27, column=1)
          r26dow2 = Label(self, text=tdy[36].get("dnum"),background=tdy[36].get("bgtclr"), width=17).grid(row=27, column=2)
          r26dow3 = Label(self, text=tdy[37].get("dnum"),background=tdy[37].get("bgtclr"), width=17).grid(row=27, column=3)
          r26dow4 = Label(self, text=tdy[38].get("dnum"),background=tdy[38].get("bgtclr"), width=17).grid(row=27, column=4)
          r26dow5 = Label(self, text=tdy[39].get("dnum"),background=tdy[39].get("bgtclr"), width=17).grid(row=27, column=5)
          r26dow6 = Label(self, text=tdy[40].get("dnum"),background=tdy[40].get("bgtclr"), width=17).grid(row=27, column=6)
          r26dow7 = Label(self, text=tdy[41].get("dnum"),background=tdy[41].get("bgtclr"), width=17).grid(row=27, column=7)

          r27dow1 = Button(self, text=tdy[35].get("dev1t"), bg=tdy[35].get("dev1c"), width=15, state=NORMAL).grid(row=28, column=1)
          r27dow2 = Button(self, text=tdy[36].get("dev1t"), bg=tdy[36].get("dev1c"), width=15, state=NORMAL).grid(row=28, column=2)
          r27dow3 = Button(self, text=tdy[37].get("dev1t"), bg=tdy[37].get("dev1c"), width=15, state=NORMAL).grid(row=28, column=3)
          r27dow4 = Button(self, text=tdy[38].get("dev1t"), bg=tdy[38].get("dev1c"), width=15, state=NORMAL).grid(row=28, column=4)
          r27dow5 = Button(self, text=tdy[39].get("dev1t"), bg=tdy[39].get("dev1c"), width=15, state=NORMAL).grid(row=28, column=5)
          r27dow6 = Button(self, text=tdy[40].get("dev1t"), bg=tdy[40].get("dev1c"), width=15, state=NORMAL).grid(row=28, column=6)
          r27dow7 = Button(self, text=tdy[41].get("dev1t"), bg=tdy[41].get("dev1c"), width=15, state=NORMAL).grid(row=28, column=7)

          r28dow1 = Button(self, text=tdy[35].get("dev2t"), bg=tdy[35].get("dev2c"), width=15, state=NORMAL).grid(row=29, column=1)
          r28dow2 = Button(self, text=tdy[36].get("dev2t"), bg=tdy[36].get("dev2c"), width=15, state=NORMAL).grid(row=29, column=2)
          r28dow3 = Button(self, text=tdy[37].get("dev2t"), bg=tdy[37].get("dev2c"), width=15, state=NORMAL).grid(row=29, column=3)
          r28dow4 = Button(self, text=tdy[38].get("dev2t"), bg=tdy[38].get("dev2c"), width=15, state=NORMAL).grid(row=29, column=4)
          r28dow5 = Button(self, text=tdy[39].get("dev2t"), bg=tdy[39].get("dev2c"), width=15, state=NORMAL).grid(row=29, column=5)
          r28dow6 = Button(self, text=tdy[40].get("dev2t"), bg=tdy[40].get("dev2c"), width=15, state=NORMAL).grid(row=29, column=6)
          r28dow7 = Button(self, text=tdy[41].get("dev2t"), bg=tdy[41].get("dev2c"), width=15, state=NORMAL).grid(row=29, column=7)

          r29dow1 = Button(self, text=tdy[35].get("dev3t"), bg=tdy[35].get("dev3c"), width=15, state=NORMAL).grid(row=30, column=1)
          r29dow2 = Button(self, text=tdy[36].get("dev3t"), bg=tdy[36].get("dev3c"), width=15, state=NORMAL).grid(row=30, column=2)
          r29dow3 = Button(self, text=tdy[37].get("dev3t"), bg=tdy[37].get("dev3c"), width=15, state=NORMAL).grid(row=30, column=3)
          r29dow4 = Button(self, text=tdy[38].get("dev3t"), bg=tdy[38].get("dev3c"), width=15, state=NORMAL).grid(row=30, column=4)
          r29dow5 = Button(self, text=tdy[39].get("dev3t"), bg=tdy[39].get("dev3c"), width=15, state=NORMAL).grid(row=30, column=5)
          r29dow6 = Button(self, text=tdy[40].get("dev3t"), bg=tdy[40].get("dev3c"), width=15, state=NORMAL).grid(row=30, column=6)
          r29dow7 = Button(self, text=tdy[41].get("dev3t"), bg=tdy[41].get("dev3c"), width=15, state=NORMAL).grid(row=30, column=7)

          r30dow1 = Button(self, text=tdy[35].get("dev4t"), bg=tdy[35].get("dev4c"), width=15, state=NORMAL).grid(row=31, column=1)
          r30dow2 = Button(self, text=tdy[36].get("dev4t"), bg=tdy[36].get("dev4c"), width=15, state=NORMAL).grid(row=31, column=2)
          r30dow3 = Button(self, text=tdy[37].get("dev4t"), bg=tdy[37].get("dev4c"), width=15, state=NORMAL).grid(row=31, column=3)
          r30dow4 = Button(self, text=tdy[38].get("dev4t"), bg=tdy[38].get("dev4c"), width=15, state=NORMAL).grid(row=31, column=4)
          r30dow5 = Button(self, text=tdy[39].get("dev4t"), bg=tdy[39].get("dev4c"), width=15, state=NORMAL).grid(row=31, column=5)
          r30dow6 = Button(self, text=tdy[40].get("dev4t"), bg=tdy[40].get("dev4c"), width=15, state=NORMAL).grid(row=31, column=6)
          r30dow7 = Button(self, text=tdy[41].get("dev4t"), bg=tdy[41].get("dev4c"), width=15, state=NORMAL).grid(row=31, column=7)

          #Bottom of Page

          cb = Label(self,text="Legend").grid(row=32, column=4)

          day1 = Label(self, text="Prior Month", background=colorsm["priormonth"]).grid(row=33, column=0)
          day2 = Label(self, text="This Month Prior to today", background=colorsm["thisbefore"], width=30).grid(row=33, column=1, columnspan=2)
          day3 = Label(self, text="Today", background=colorsm["today"],width=17).grid(row=33, column=3)
          day4 = Label(self, text="This Month after today", background=colorsm["thismonth"],width=30).grid(row=33, column=4, columnspan=2)
          day5 = Label(self, text="Next Month", background=colorsm["nextmonth"],width=17).grid(row=33, column=6)
          day6 = Label(self, text="Site Down", background=colorsm["site"], width=17).grid(row=33, column=7)

          ca = Label(self, text="Calendars in Use")
          ca.grid(row=34, column=4)

          cal1 = Label(self, text=cal.get("calAt"), background=pref["calAclr"], width=17).grid(row=35, column=1)
          cal2 = Label(self, text=cal.get("calBt"), background=pref["calBclr"], width=17).grid(row=35, column=2)
          cal3 = Label(self, text=cal.get("calCt"), background=pref["calCclr"], width=17).grid(row=35, column=3)
          cal4 = Label(self, text=cal.get("calDt"), background=pref["calDclr"], width=17).grid(row=35, column=4)
          cal5 = Label(self, text=cal.get("calEt"), background=pref["calEclr"], width=17).grid(row=35, column=5)
          cal6 = Label(self, text="Site", background="red", width=17).grid(row=35, column=6)


          cc = Label(self)
          cc.grid(row=36, columnspan=8,  sticky=W+E)

          brt = Button(self,text="Return")
          brt.grid(row=37, column=0)
          lbl1 = Label(self, text=" ")
          lbl1.grid(row=37,column=1)
          bbk = Button(self,text="Prior Month")
          bbk.grid(row=37, column=3)
          bpp = Button(self, text="Print Page")
          bpp.grid(row=37, column=4)
          bnm = Button(self,text="Next Month")
          bnm.grid(row=37, column=5) 
          lbl2 = Label(self, text="")
          lbl2.grid(row=37,column=6)
          bnm = Button(self,text="Exit")
          bnm.grid(row=37, column=7) 
          self.pack()


def main():

    root = Tk()
    app = MGCalendar4()
    root.mainloop()


if __name__ == '__main__':
    main()
