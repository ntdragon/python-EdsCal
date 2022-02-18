#!/usr/bin/python3

import calendar
import datetime
import holidays

gc = calendar.Calendar(0)
#dts = []
#for i in gc.itermonthdates(2019,3):
#     dts.append(i.day)
#     print(dts)
     
#print( len(dts) )
#today = datetime.now()
wk = datetime.date(2019, 3, 2).strftime("%A %B %d, %Y")
#print(wk)
#print(datetime.datetime.now().strftime("%A %B %d, %Y"))

#str = "March 02, 2019"
#d = datetime.datetime.strptime(str, "%B %d, %Y").strftime("%B %Y")
#print (d)

cals= [
               dict(num=0, app="FALSE", name="Liturgical", color="yellowgreen"),
               dict(num=1, app="FALSE", name="US Holidays", color="lightsteelblue"),
               dict(num=2, app="TRUE", name="Birdsall Family", color="cyan"),
               dict(num=3, app="TRUE", name="Kirkup Family",color="magenta"),
               dict(num=4, app="FALSE" name="", color="purple"),
               dict(num=5, app="TRUE", name="Site", color="red")
]
eventCal = [
               dict(num=0, cal="Liturgical", eDate=datetime.date(2019, 3, 3), title="Ordinary 9th Sunday"),
               dict(num=1, cal="Liturgical", eDate=datetime.date(2019, 3, 6), title="Ash Wednesday"),
               dict(num=2, cal="US Holidays", eDate=datetime.date(2019, 3, 9), title="DST begins"),
               dict(num=3, cal="Liturgical", eDate=datetime.date(2019, 3, 10), title="Lent 1st Sunday"),
               dict(num=4, cal="Liturgical", eDate=datetime.date(2019, 3, 17), title="Lent 2nd Sunday"),
               dict(num=5, cal="Liturgical", eDate=datetime.date(2019, 3, 24), title="Lent 3rd Sunday"),
               dict(num=6, cal="Liturgical", eDate=datetime.date(2019, 3, 31), title="Lent 4th Sunday")
               dict(num=7, cal="Birdsall Family", eDate=datetime.date(2019, 3, 1), title="Bryan Kovas B'Day" ),
               dict(num=8, cal="Birdsall Family", eDate=datetime.date(2019, 3, 3), title="Helen Birdsall B'Day"),
               dict(num=9, cal="Birdsall Family", eDate=datetime.date(2019, 3, 4), title="Greg Kovas B'Day"),
               dict(num=10, cal="Birdsall Family", eDate=datetime.date(2019, 3, 4), title="Andrew Noyes B'Day"),
               dict(num=11, cal="Birdsall Family", eDate=datetime.date(2019, 3, 4), title="Brielle Balmer B'Day"),
]


#print(eventCal[8]["eDate"].month)
#print(eventCal[8]["eDate"].day)
#for date in holidays.UnitedStates(years=2022).items():
#     print(date)
cmonth = 3
cday = 2
glcal = calendar.Calendar(0)
days = [calendar.day_name[i] for i in glcal.iterweekdays()]
dts = []
dmt = []
for i in glcal.itermonthdates(2019, 3):
     dts.append( i.day )
     dmt.append( i.month )
          
numdays = len(dts)
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



for i in range(0,42,1):
     for ii in range(0,len(eventCal),1):
          if ((tdy[i]["mnum"] == eventCal[ii]["eDate"].month) and (tdy[i]["dnum"] == eventCal[ii]["eDate"].day)):
               tdy[i]["dev1t"] = eventCal[ii]["title"]
               for iii in range(0,4,1):
                    if (cals[iii]["name"] == eventCal[ii]["cal"]):
                         tdy[i]["dev1c"] = cals[iii]["color"]
               tdy[i]["dev1e"] = "Show "+ eventCal[ii]["title"]
               print(tdy[i]["dev1t"]+" - "+tdy[i]["dev1c"]+" - "+tdy[i]["dev1e"])
