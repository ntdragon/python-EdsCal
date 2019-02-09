#!/bin/python3

from jinja2 import Environment, FileSystemLoader

hd = {"loc": "Month Calendar"}
hdr = { "name": "Ed",  "page":"March 2019 Calendar", "today":"Saturday  March  2, 2019" }
pref = {  "startDay":1,  "startwk":5}
days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
colorsm = {"previousmonth": "fuschia", "thisbefore": "aqua",  "today": "yellow",  "thismonth": "white",  "nextmonth": "lime", "site":"red" }
colorsc = { "neutral": "silver",  "calAclr": "green",  "calBclr": "blue",  "calCclr": "cyan",  "calDclr": "magenta",  "calEclr": "purple",  "calSclr": "red" }
cal = {"month":"March", "year":"2019"}

bgtclr = [colorsm["thismonth"]]
bgeclr = ["white"]
dnum = [0]
calat = [""]
calbt = [""]
calct = [""]
caldt = [""]
calet = [""]
calst = [""]

for i in range (1, 34):
     bgtclr.append( colorsm["thismonth"])
     bgeclr.append("white")
     dnum.append(0)
     calat.append("")
     calbt.append("")
     calct.append("")
     caldt.append("")
     calet.append("")
     calst.append("")
     
dnum = [25, 26, 27, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 ]
for i in range (0, 4):
          bgtclr[i] = colorsm["previousmonth"]
          bgeclr[i] = colorsm["previousmonth"]

bgtclr[4] = colorsm["thisbefore"]
bgtclr[5] = colorsm["today"]
bgeclr[4] = colorsm["thisbefore"]
bgeclr[5] = colorsm["today"]
calat[9] = "Ash Wednesday"
calbt[13] = "DST begins"
calbt[21] = "President's Day"



input_ = {"hd":hd, "hdr":hdr, "cal":cal, "dnum":dnum, "colorsm":colorsm, "colorsc":colorsc, "bgtclr":bgtclr, "bgeclr":bgeclr, "pref":pref, "days":days, 'calat':calat, 'calbt':calbt, 'calct':calct, 'caldt':caldt,'calet':calet, 'calst':calst}
env = Environment(loader = FileSystemLoader("."))
template=env.get_template("calendar3.html")

output = template.render(input_ )

print(output)

