#!/usr/bin/python3

import calendar
import datetime

gc = calendar.Calendar(0)
#dts = []
#for i in gc.itermonthdates(2019,3):
#     dts.append(i.day)
#     print(dts)
     
#print( len(dts) )
#today = datetime.now()
wk = datetime.date(2019, 3, 2).strftime("%A %B %d, %Y")
print(wk)
print(datetime.datetime.now().strftime("%A %B %d, %Y"))
str = "d"
print (len( str ))
