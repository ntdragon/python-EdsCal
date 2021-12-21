#!/usr/bin/env python3

"""
try1 first attempts to write a calender ui
using TCL/TK

Author: Edward Birdsall
"""

from tkinter import Tk, W, E, BOTH
from tkinter.ttk import Frame, Button, Entry, Style, Label

class MCalendar4(Frame):

     def __init__(self):
          super().__init__()

          self.initUI()

     def initUI(self):
          self.master.title("February 2yyy")

          Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

          for  c in range(8):
               self.columnconfigure(c, pad=3)

          for r in range(25):
               self.rowconfigure(r, pad=3)

          st1 = Style()
          st1.configure('W1.TButton', background="limegreen", foreground='black')
          st2 = Style()
          st2.configure('W2.TButton', background="red", foreground='black')
          st3 = Style()
          st3.configure('W3.TButton', background="palegreen", foreground='black')
          st4 = Style()
          st4.configure('W4.TButton', background="violet", foreground='black')
          st5 = Style()
          st5.configure('W5.TButton', background="wheat", foreground='black')
           
          
          ct = Label(self)
          ct.grid(row=0, columnspan=8, sticky=W+E)
          wom = Label(self, text="Week of Year", style='W5.TButton')
          wom.grid(row=1, column=0)
          dow1 = Label(self, text="Monday")
          dow1.grid(row=1, column=1)
          dow2 = Label(self, text="Tuesday")
          dow2.grid(row=1, column=2)
          dow3 = Label(self, text="Wednesday")
          dow3.grid(row=1, column=3)
          dow4 = Label(self, text="Thursday")
          dow4.grid(row=1, column=4)
          dow5 = Label(self, text="Friday")
          dow5.grid(row=1, column=5)
          dow6 = Label(self, text="Saturday")
          dow6.grid(row=1, column=6)
          dow7 = Label(self, text="Sunday")
          dow7.grid(row=1, column=7)


          r1wom = Label(self, text="5")
          r1wom.grid(row=2, column=0)
          r1dow1 = Label(self, text="1")
          r1dow1.grid(row=2, column=1)
          r1dow2 = Label(self, text="2")
          r1dow2.grid(row=2, column=2)
          r1dow3 = Label(self, text="3")
          r1dow3.grid(row=2, column=3)
          r1dow4 = Label(self, text="4")
          r1dow4.grid(row=2, column=4)
          r1dow5 = Label(self, text="5")
          r1dow5.grid(row=2, column=5)
          r1dow6 = Label(self, text="6")
          r1dow6.grid(row=2, column=6)
          r1dow7 = Label(self, text="7")
          r1dow7.grid(row=2, column=7)

          r2dow1 = Button(self, text=" ")
          r2dow1.grid(row=3, column=1)
          r2dow2 = Button(self, text=" ")
          r2dow2.grid(row=3, column=2)
          r2dow3 = Button(self, text=" ")
          r2dow3.grid(row=3, column=3)
          r2dow4 = Button(self, text="PCP at 1400", style='W1.TButton')
          r2dow4.grid(row=3, column=4)
          r2dow5 = Button(self, text=" ")
          r2dow5.grid(row=3, column=5)
          r2dow6 = Button(self, text=" ")
          r2dow6.grid(row=3, column=6)
          r2dow7 = Button(self, text="Mass at 1100", style='W2.TButton')
          r2dow7.grid(row=3, column=7)

          r3dow1 = Button(self, text=" ")
          r3dow1.grid(row=4, column=1)
          r3dow2 = Button(self, text=" ")
          r3dow2.grid(row=4, column=2)
          r3dow3 = Button(self, text=" ")
          r3dow3.grid(row=4, column=3)
          r3dow4 = Button(self, text=" ")
          r3dow4.grid(row=4, column=4)
          r3dow5 = Button(self, text=" ")
          r3dow5.grid(row=4, column=5)
          r3dow6 = Button(self, text=" ")
          r3dow6.grid(row=4, column=6)
          r3dow7 = Button(self, text=" ")
          r3dow7.grid(row=4, column=7)

          r4dow1 = Button(self, text=" ")
          r4dow1.grid(row=5, column=1)
          r4dow2 = Button(self, text=" ")
          r4dow2.grid(row=5, column=2)
          r4dow3 = Button(self, text=" ")
          r4dow3.grid(row=5, column=3)
          r4dow4 = Button(self, text=" ")
          r4dow4.grid(row=5, column=4)
          r4dow5 = Button(self, text=" ")
          r4dow5.grid(row=5, column=5)
          r4dow6 = Button(self, text=" ")
          r4dow6.grid(row=5, column=6)
          r4dow7 = Button(self, text=" ")
          r4dow7.grid(row=5, column=7)

          r5dow1 = Button(self, text=" ")
          r5dow1.grid(row=6, column=1)
          r5dow2 = Button(self, text=" ")
          r5dow2.grid(row=6, column=2)
          r5dow3 = Button(self, text=" ")
          r5dow3.grid(row=6, column=3)
          r5dow4 = Button(self, text=" ")
          r5dow4.grid(row=6, column=4)
          r5dow5 = Button(self, text=" ")
          r5dow5.grid(row=6, column=5)
          r5dow6 = Button(self, text=" ")
          r5dow6.grid(row=6, column=6)
          r5dow7 = Button(self, text=" ")
          r5dow7.grid(row=6, column=7)

          r6wom = Label(self, text="6")
          r6wom.grid(row=7, column=0)
          r6dow1 = Label(self, text="8")
          r6dow1.grid(row=7, column=1)
          r6dow2 = Label(self, text="9")
          r6dow2.grid(row=7, column=2)
          r6dow3 = Label(self, text="10")
          r6dow3.grid(row=7, column=3)
          r6dow4 = Label(self, text="11")
          r6dow4.grid(row=7, column=4)
          r6dow5 = Label(self, text="12")
          r6dow5.grid(row=7, column=5)
          r6dow6 = Label(self, text="13")
          r6dow6.grid(row=7, column=6)
          r6dow7 = Label(self, text="14")
          r6dow7.grid(row=7, column=7)

          r7dow1 = Button(self, text=" ")
          r7dow1.grid(row=8, column=1)
          r7dow2 = Button(self, text="Dentist 1000")
          r7dow2.grid(row=8, column=2)
          r7dow3 = Button(self, text=" ")
          r7dow3.grid(row=8, column=3)
          r7dow4 = Button(self, text=" ")
          r7dow4.grid(row=8, column=4)
          r7dow5 = Button(self, text=" ")
          r7dow5.grid(row=8, column=5)
          r7dow6 = Button(self, text=" ")
          r7dow6.grid(row=8, column=6)
          r7dow7 = Button(self, text="Mass at 1100", style='W2.TButton')
          r7dow7.grid(row=8, column=7)

          r8dow1 = Button(self, text=" ")
          r8dow1.grid(row=9, column=1)
          r8dow2 = Button(self, text=" ")
          r8dow2.grid(row=9, column=2)
          r8dow3 = Button(self, text=" ")
          r8dow3.grid(row=9, column=3)
          r8dow4 = Button(self, text=" ")
          r8dow4.grid(row=9, column=4)
          r8dow5 = Button(self, text=" ")
          r8dow5.grid(row=9, column=5)
          r8dow6 = Button(self, text=" ")
          r8dow6.grid(row=9, column=6)
          r8dow7 = Button(self, text=" ")
          r8dow7.grid(row=9, column=7)

          r9dow1 = Button(self, text=" ")
          r9dow1.grid(row=10, column=1)
          r9dow2 = Button(self, text=" ")
          r9dow2.grid(row=10, column=2)
          r9dow3 = Button(self, text=" ")
          r9dow3.grid(row=10, column=3)
          r9dow4 = Button(self, text=" ")
          r9dow4.grid(row=10, column=4)
          r9dow5 = Button(self, text=" ")
          r9dow5.grid(row=10, column=5)
          r9dow6 = Button(self, text=" ")
          r9dow6.grid(row=10, column=6)
          r9dow7 = Button(self, text=" ")
          r9dow7.grid(row=10, column=7)

          r10dow1 = Button(self, text=" ")
          r10dow1.grid(row=11, column=1)
          r10dow2 = Button(self, text=" ")
          r10dow2.grid(row=11, column=2)
          r10dow3 = Button(self, text=" ")
          r10dow3.grid(row=11, column=3)
          r10dow4 = Button(self, text=" ")
          r10dow4.grid(row=11, column=4)
          r10dow5 = Button(self, text=" ")
          r10dow5.grid(row=11, column=5)
          r10dow6 = Button(self, text=" ")
          r10dow6.grid(row=11, column=6)
          r10dow7 = Button(self, text=" ")
          r10dow7.grid(row=11, column=7)
          
          r11wom = Label(self, text="7")
          r11wom.grid(row=12, column=0)
          r11dow1 = Label(self, text="15")
          r11dow1.grid(row=12, column=1)
          r11dow2 = Label(self, text="16")
          r11dow2.grid(row=12, column=2)
          r11dow3 = Label(self, text="17")
          r11dow3.grid(row=12, column=3)
          r11dow4 = Label(self, text="18")
          r11dow4.grid(row=12, column=4)
          r11dow5 = Label(self, text="19")
          r11dow5.grid(row=12, column=5)
          r11dow6 = Label(self, text="20")
          r11dow6.grid(row=12, column=6)
          r11dow7 = Label(self, text="21")
          r11dow7.grid(row=12, column=7)

          r12dow1 = Button(self, text=" ")
          r12dow1.grid(row=13, column=1)
          r12dow2 = Button(self, text=" ")
          r12dow2.grid(row=13, column=2)
          r12dow3 = Button(self, text=" ")
          r12dow3.grid(row=13, column=3)
          r12dow4 = Button(self, text=" ")
          r12dow4.grid(row=13, column=4)
          r12dow5 = Button(self, text=" ")
          r12dow5.grid(row=13, column=5)
          r12dow6 = Button(self, text=" ")
          r12dow6.grid(row=13, column=6)
          r12dow7 = Button(self, text="Mass at 1100", style='W2.TButton')
          r12dow7.grid(row=13, column=7)

          r13dow1 = Button(self, text=" ")
          r13dow1.grid(row=14, column=1)
          r13dow2 = Button(self, text=" ")
          r13dow2.grid(row=14, column=2)
          r13dow3 = Button(self, text=" ")
          r13dow3.grid(row=14, column=3)
          r13dow4 = Button(self, text=" ")
          r13dow4.grid(row=14, column=4)
          r13dow5 = Button(self, text=" ")
          r13dow5.grid(row=14, column=5)
          r13dow6 = Button(self, text=" ")
          r13dow6.grid(row=14, column=6)
          r13dow7 = Button(self, text=" ")
          r13dow7.grid(row=14, column=7)

          r14dow1 = Button(self, text=" ")
          r14dow1.grid(row=15, column=1)
          r14dow2 = Button(self, text=" ")
          r14dow2.grid(row=15, column=2)
          r14dow3 = Button(self, text=" ")
          r14dow3.grid(row=15, column=3)
          r14dow4 = Button(self, text=" ")
          r14dow4.grid(row=15, column=4)
          r14dow5 = Button(self, text=" ")
          r14dow5.grid(row=15, column=5)
          r14dow6 = Button(self, text=" ")
          r14dow6.grid(row=15, column=6)
          r14dow7 = Button(self, text=" ")
          r14dow7.grid(row=15, column=7)

          r15dow1 = Button(self, text=" ")
          r15dow1.grid(row=16, column=1)
          r15dow2 = Button(self, text=" ")
          r15dow2.grid(row=16, column=2)
          r15dow3 = Button(self, text=" ")
          r15dow3.grid(row=16, column=3)
          r15dow4 = Button(self, text=" ")
          r15dow4.grid(row=16, column=4)
          r15dow5 = Button(self, text=" ")
          r15dow5.grid(row=16, column=5)
          r15dow6 = Button(self, text=" ")
          r15dow6.grid(row=16, column=6)
          r15dow7 = Button(self, text=" ")
          r15dow7.grid(row=16, column=7)

          r16wom = Label(self, text="8")
          r16wom.grid(row=17, column=0)
          r16dow1 = Label(self, text="22")
          r16dow1.grid(row=17, column=1)
          r16dow2 = Label(self, text="23")
          r16dow2.grid(row=17, column=2)
          r16dow3 = Label(self, text="24")
          r16dow3.grid(row=17, column=3)
          r16dow4 = Label(self, text="25")
          r16dow4.grid(row=17, column=4)
          r16dow5 = Label(self, text="26")
          r16dow5.grid(row=17, column=5)
          r16dow6 = Label(self, text="27")
          r16dow6.grid(row=17, column=6)
          r16dow7 = Label(self, text="28")
          r16dow7.grid(row=17, column=7)

          r17dow1 = Button(self, text=" ")
          r17dow1.grid(row=18, column=1)
          r17dow2 = Button(self, text=" ")
          r17dow2.grid(row=18, column=2)
          r17dow3 = Button(self, text=" ")
          r17dow3.grid(row=18, column=3)
          r17dow4 = Button(self, text=" ")
          r17dow4.grid(row=18, column=4)
          r17dow5 = Button(self, text=" ")
          r17dow5.grid(row=18, column=5)
          r17dow6 = Button(self, text=" ")
          r17dow6.grid(row=18, column=6)
          r17dow7 = Button(self, text="Mass at 1100", style='W2.TButton')
          r17dow7.grid(row=18, column=7)

          r18dow1 = Button(self, text=" ")
          r18dow1.grid(row=19, column=1)
          r18dow2 = Button(self, text=" ")
          r18dow2.grid(row=19, column=2)
          r18dow3 = Button(self, text=" ")
          r18dow3.grid(row=19, column=3)
          r18dow4 = Button(self, text=" ")
          r18dow4.grid(row=19, column=4)
          r18dow5 = Button(self, text=" ")
          r18dow5.grid(row=19, column=5)
          r18dow6 = Button(self, text=" ")
          r18dow6.grid(row=19, column=6)
          r18dow7 = Button(self, text=" ")
          r18dow7.grid(row=19, column=7)

          r19dow1 = Button(self, text=" ")
          r19dow1.grid(row=20, column=1)
          r19dow2 = Button(self, text=" ")
          r19dow2.grid(row=20, column=2)
          r19dow3 = Button(self, text=" ")
          r19dow3.grid(row=20, column=3)
          r19dow4 = Button(self, text=" ")
          r19dow4.grid(row=20, column=4)
          r19dow5 = Button(self, text=" ")
          r19dow5.grid(row=20, column=5)
          r19dow6 = Button(self, text=" ")
          r19dow6.grid(row=20, column=6)
          r19dow7 = Button(self, text=" ")
          r19dow7.grid(row=20, column=7)

          r20dow1 = Button(self, text=" ")
          r20dow1.grid(row=21, column=1)
          r20dow2 = Button(self, text=" ")
          r20dow2.grid(row=21, column=2)
          r20dow3 = Button(self, text=" ")
          r20dow3.grid(row=21, column=3)
          r20dow4 = Button(self, text=" ")
          r20dow4.grid(row=21, column=4)
          r20dow5 = Button(self, text=" ")
          r20dow5.grid(row=21, column=5)
          r20dow6 = Button(self, text=" ")
          r20dow6.grid(row=21, column=6)
          r20dow7 = Button(self, text=" ")
          r20dow7.grid(row=21, column=7)

          cb = Label(self)
          ct.grid(row=22, columnspan=8, sticky=W+E)

          cal1 = Label(self, text="Private", style='W1.TButton')
          cal1.grid(row=23, column=1)
          cal2 = Label(self, text="Public", style='W2.TButton')
          cal2.grid(row=23, column=3)
          cal3 = Label(self, text="Family", style='W3.TButton')
          cal3.grid(row=23, column=5)
          cal4 = Label(self, text="Holidays", style='W4.TButton')
          cal4.grid(row=23, column=7)

          lbl1 = Label(self, text=" ")
          lbl1.grid(row=24,column=0)
          bbk = Button(self,text="Previous Month")
          bbk.grid(row=24, column=1, columnspan=2)
          lbl2 = Label(self, text=" ")
          lbl2.grid(row=24,column=3)
          bex = Button(self, text="Exit")
          bex. grid(row=24, column=4)
          lbl3 = Label(self, text=" ")
          lbl3.grid(row=24,column=5)
          bnm = Button(self,text="Next Month")
          bnm.grid(row=24, column=6, columnspan=2) 
          self.pack()


def main():

    root = Tk()
    app = MCalendar4()
    root.mainloop()


if __name__ == '__main__':
    main()
