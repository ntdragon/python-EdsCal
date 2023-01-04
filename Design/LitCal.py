Liturgical Calendar Generation Module

class LiturgicalDay:
     """ This class is to hold all the information regarding a specific calendar day.
         Since there might be a number of events in a given day I shall allocate for that.
         This liturgical day is hopefully designed well for Liturgy Ministers to have 
         enough information to help with their tasks.  Specifically I have Music Ministers
         and lectors in mind.
     """
     
     def __init__(self, daydate, season, color, rcycle, read1, psalm, read2, gospel, rank, descr, strank=None):
          self.date = daydate    #year, month, day,
          self.season = season   #Advent, Ordinary, Lent, Easter
          self.color = color
          self.rcycle = rcycle   #Sundays-A,B,C, Weekdays-I,II
          self.read1 = read1     #first reading for the day
          self.psalm = psalm
          self.read2 = read2
          self.gospel = gospel
          self.rank = rank
          self.descr = descr
          self.saintrank = strank
          self.omitted=None   #omitted celebration for the day
          self.originalDate=None   #the day this celebration was supposed to take place but was moved
          
     def setReadingCycle(theDate):
          """ Set which readings cycle for the day applies.  If a Sunday the it is one of A,B,C while
               weekdays are either I or II.  For week days it depends on the year being even or odd for
               January 1 in the Liturgical Year while Sundays are in a three year cycle with 20?? being A.
          """ 
          

def initLiturgicalCalendar(year, type='C'):
     """ This initializes a liturgical calendar for year and is by Liturgical calendar starting with
          first Sunday in Advent or Standard year calendar starting January 1.  Type is either L for
          Liturgical Calendar or C for standard calendar which is the default.
     """
     if (type == "L"):
          #figure out what is the date of First Sunday of Advent
          dayOfWeek = date(year-1, 12, 25).weekday()
          #Fill in up through Dec 31
          #Figure number of days to next First Sunday of Advent
          #Fill in the rest of the days
     else:
          #figure out what day January 1 is for year and how many days that year
          dayOfWeek = date(year), 1, 1).weekday()
          #fill in the list
          litCal=[]
          for i in range(0,len(),1):
          
