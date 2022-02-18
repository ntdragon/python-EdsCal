#!/bin/python3

from jinja2 import Environment, FileSystemLoader
import calendar
import datetime

#=========================================================================================================
#Begining of definitions.  Need to remember how to split this into a seperate area that invokes MCalendar
#=========================================================================================================
#=================================
# desired inputs for final version what, when, which event calendars, preferences
#=================================
inputs = {"name":"Ed", "date":"March 2, 2019", "startDay":0, "dispWeek":1}
#========================================================
# some kludges for testing and until I get it all working
#========================================================
#cyear = int(cal.get("year"))
cyear = 2019
cmonth = 3
cday = 2
cals= [
      dict(num=0, app="FALSE", name="Liturgical", color="yellowgreen"),
      dict(num=1, app="FALSE", name="US Holidays", color="lightsteelblue"),
      dict(num=2, app="TRUE", name="Birdsall Family", color="cyan"),
      dict(num=3, app="TRUE", name="Kirkup Family",color="magenta"),
      dict(num=4, app="FALSE", name="", color="purple"),
      dict(num=5, app="TRUE", name="Site", color="red")
]
eventCal = [
           dict(num=0, cal="Liturgical", eDate=datetime.date(2019, 2, 24), title="Ordinary 8th Sunday"),
           dict(num=1, cal="Liturgical", eDate=datetime.date(2019, 3, 3), title="Ordinary 9th Sunday"),
           dict(num=2, cal="Liturgical", eDate=datetime.date(2019, 3, 6), title="Ash Wednesday"),
           dict(num=3, cal="US Holidays", eDate=datetime.date(2019, 3, 9), title="DST begins"),
           dict(num=4, cal="Liturgical", eDate=datetime.date(2019, 3, 10), title="Lent 1st Sunday"),
           dict(num=5, cal="Liturgical", eDate=datetime.date(2019, 3, 17), title="Lent 2nd Sunday"),
           dict(num=6, cal="Liturgical", eDate=datetime.date(2019, 3, 24), title="Lent 3rd Sunday"),
           dict(num=7, cal="Liturgical", eDate=datetime.date(2019, 3, 31), title="Lent 4th Sunday"),
           dict(num=8, cal="Birdsall Family", eDate=datetime.date(2019, 3, 1), title="Bryan Kovas B'Day" ),
           dict(num=9, cal="Birdsall Family", eDate=datetime.date(2019, 3, 3), title="Helen Birdsall B'Day"),
           dict(num=10, cal="Birdsall Family", eDate=datetime.date(2019, 3, 4), title="Greg Kovas B'Day"),
           dict(num=11, cal="Birdsall Family", eDate=datetime.date(2019, 3, 4), title="Andrew Noyes B'Day"),
           dict(num=12, cal="Birdsall Family", eDate=datetime.date(2019, 3, 4), title="Brielle Balmer B'Day"),
]

#===================================
# Working code towards final version
#===================================

hd = {"loc":"Week Calendar"}
hdr = { "name":"Ed",  "page":"Week of  Calendar", "today":"Saturday  March  2, 2019" }
hdr["name"] = inputs["name"]
hdr["page"] = datetime.datetime.strptime(inputs["date"], "%B %d, %Y").strftime("%B %Y")+" Calendar"
#hdr["today"] = datetime.datetime.now().strftime("%A %B %d, %Y")
hdr["today"] = "Saturday March 02, 2019"  #for testing

cal = {"month":"March", "year":"2019", "startwk":5,"calrows":5, "calAt":"Liturgical", "calBt":"US Holidays","calCt":"Birdsall Family", "calDt":"Kirkup Family", "calEt":""}
pref = {  "startDay":1, "dispWeek":0, "calAclr": "yellowgreen",  "calBclr": "lightsteelblue",  "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "purple"}
pref["startDay"] = inputs["startDay"]
pref["dispWeek"] = inputs["dispWeek"]

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
cal["calrows"] = numdays//7

#days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
colorsm = {"priormonth": "Orchid", "thisbefore": "Aqua",  "today": "Yellow",  "thismonth": "White",  "nextmonth": "Lime", "site":"Red" , "neutral": "silver", "calSclr": "red" }

tdy = []
for i in range(0, 42,1):
     tdy.append({"bgtclr":"white","bgeclr":"white", "mnum":0, "dnum":0, "devt":-1, "dev1t":"", "dev1c":"gray85", "dev1e":"",  "dev2t":"", "dev2c":"gray85", "dev2e":"", "dev3t":"", "dev3c":"gray85", "dev3e":"", "dev4t":"", "dev4c":"grey85", "dev4e":"", })
 
for i in range(0, numdays, 1):
     tdy[i]["mnum"] = dmt[i]
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

for i in range(0, 42, 1):
     for ii in range(0,len(eventCal),1):
          if ((tdy[i]["mnum"] == eventCal[ii]["eDate"].month) and (tdy[i]["dnum"] == eventCal[ii]["eDate"].day)):
               if (tdy[i]["devt"]<1):
                    tdy[i]["devt"] = 1
               else:
                    tdy[i]["devt"] = tdy[i]["devt"] + 1
               if (tdy[i]["devt"] == 1):
                    tdy[i]["dev1t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev1c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev1e"] = "Show "+ eventCal[ii]["title"]
               elif (tdy[i]["devt"] == 2):
                    tdy[i]["dev2t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev2c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev2e"] = "Show "+ eventCal[ii]["title"]
               elif (tdy[i]["devt"] == 3):
                    tdy[i]["dev3t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev3c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev3e"] = "Show "+ eventCal[ii]["title"]
               elif (tdy[i]["devt"] == 4):
                    tdy[i]["dev4t"] = eventCal[ii]["title"]
                    for iii in range(0,len(cals),1):
                         if (cals[iii]["name"] == eventCal[ii]["cal"]):
                              tdy[i]["dev4c"] = cals[iii]["color"]
                              if (cals[iii]["app"] == "TRUE"):
                                   tdy[i]["dev4e"] = "Show "+ eventCal[ii]["title"]
               else:
                    tdy[i]["devt"] = 4


input_ = {"hd":hd, "hdr":hdr, "cal":cal, "days":days, "colorsm":colorsm, "pref":pref, "tdy":tdy }
env = Environment(loader = FileSystemLoader("../templates/"))
template=env.get_template("wcalendar.jhtml")

output = template.render(input_ )

print(output)

