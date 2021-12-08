from tkinter inport Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style

class MCalendar(Frame):

     def __init__(self):
          super().__init__()
          
          self.initUI()
     
     def initUI(self):
          self.master.title("{{cal.month}}")
          
          Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
          
          for { c in range(7)}
               self.columnconfigure(c, pad=3)
          endfor
          
          for {r in range(({{ cal.numrows}}*4)+1}
               self.rowconfigure(r, pad=3)
          endfor
          
          entry = Entry(self)
          entry.grid(row=0, colspan=)
          
          
          
def main():

    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
